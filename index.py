import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler): 
    def get(self): # define get method
        self.write("this is a python command executed from the back end")

if __name__ == "__main__": 
    app = tornado.web.Application([ # create initial tornado app, pass in endpoints for the requests we will create handlers for
        (r"/", basicRequestHandler)
    ]) 

    port = 8882
    app.listen(port)
    print(f"App is listening on port {port}")
    tornado.ioloop.IOLoop.current().start() # put in the loop so the app keeps listening/running