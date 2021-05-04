import tornado.web
import tornado.ioloop
import json

class mainRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html") # render html content

class queryParamRequestHandler(tornado.web.RequestHandler): # uses a query parameter
    def get(self):
        num = self.get_argument("num") # retrieve the query parameter from the request URL

        if (num.isdigit()): # checking parameter and conditionally executing based on the results
            r = "odd" if int(num) % 2 else "even"
            self.write(f"the number {num} is {r}")
        else:
            self.write(f"{num} is not a valid number")

class resourceParamRequestHandler(tornado.web.RequestHandler): # uses a resource parameter
    def get(self, studentName, courseID): # resource parameters become inputs for the get method
        self.write(f"welcome {studentName} to class #{courseID}")

class listRequestHandler(tornado.web.RequestHandler): # API
    def get(self):
        fileHandler = open("list.txt", "r") # r for read?
        fruits = fileHandler.read().splitlines()
        fileHandler.close()
        self.write(json.dumps(fruits))
    def post(self): # defining the post request
        fruit = self.get_argument("fruit") # use the query string parameters to receive the new content
        fileHandler = open("list.txt", "a") # a for append
        fileHandler.write(f"{fruit}\n")
        fileHandler.close()
        self.write(json.dumps({ "message": "Fruit added successfully" }))

if __name__ == "__main__": 
    app = tornado.web.Application([ # create initial tornado app, pass in endpoints for the requests we will create handlers for
        (r"/", mainRequestHandler),
        (r"/isEven", queryParamRequestHandler), # uses a query parameter
        (r"/students/([a-z]+)/([1-9]+)", resourceParamRequestHandler), # uses a resource parameter + regex, 
        (r"/list", listRequestHandler)
    ]) 

    port = 8882
    app.listen(port)
    print(f"App is listening on port {port}")
    tornado.ioloop.IOLoop.current().start() # put in the loop so the app keeps listening/running