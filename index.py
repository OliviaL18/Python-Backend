import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler): # create request handler
    def get(self): # define get method
        self.write("this is a python command executed from the back end")

class helloRequestHandler(tornado.web.RequestHandler):
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
        

if __name__ == "__main__": 
    app = tornado.web.Application([ # create initial tornado app, pass in endpoints for the requests we will create handlers for
        (r"/", basicRequestHandler),
        (r"/hello", helloRequestHandler), 
        (r"/isEven", queryParamRequestHandler), # uses a query parameter
        (r"/students/([a-z]+)/([1-9]+)", resourceParamRequestHandler) # uses a resource parameter + regex
    ]) 

    port = 8882
    app.listen(port)
    print(f"App is listening on port {port}")
    tornado.ioloop.IOLoop.current().start() # put in the loop so the app keeps listening/running