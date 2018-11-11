import tornado
import tornado.ioloop
import tornado.websocket

class WebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        print('on websoket open')

    def on_message(self,message):
        self.write_message("I have receive your message:",message)

    def on_close(self):
        print("on websocket close")

    def check_orgin(self,orgin):
        return True


patterns = [
    (r"/ws",WebSocket)
]

settings = {
    "debug":True
}
app = tornado.web.Application(patterns,**settings);
app.listen(7000,xheaders = True)

tornado.ioloop.IOLoop.current().start()

print("server listen on 7000");