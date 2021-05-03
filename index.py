import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler): 
    def get(self): # define get method
        self.write("this is a python command executed from the back end")

class helloRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class numRequestHandler(tornado.web.RequestHandler): # 
    def get(self):
        num = self.get_argument("num") # retrieve the query parameter from the request URL

        if (num.isdigit()):
            r = "odd" if int(num) % 2 else "even"
            self.write(f"the number {num} is {r}")
        else:
            self.write(f"{num} is not a valid number")

if __name__ == "__main__": 
    app = tornado.web.Application([ # create initial tornado app, pass in endpoints for the requests we will create handlers for
        (r"/", basicRequestHandler),
        (r"/hello", helloRequestHandler), 
        (r"/isEven", numRequestHandler)
    ]) 

    port = 8882
    app.listen(port)
    print(f"App is listening on port {port}")
    tornado.ioloop.IOLoop.current().start() # put in the loop so the app keeps listening/running