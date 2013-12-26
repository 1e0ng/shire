from handlers import BaseHandler
class HelloHandler(BaseHandler):
    def get(self):
        self.render('hello.html', word='Hello world!')
