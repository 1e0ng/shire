#!/usr/bin/env python
#encoding=utf-8
import os

from shireweb import ShireWeb

if __name__ == "__main__":
    routes = [
        (r'/', 'controller.HelloHandler'),

        (r'/users/?', 'handlers.UserListHandler'),
        (r'/user/?(\w*)', 'handlers.UserHandler'),
        (r'/account', 'handlers.AccountHandler'),

        (r'/signin', 'handlers.SigninHandler'),
        (r'/signout', 'handlers.SignoutHandler'),
        ]
    template_path = os.path.abspath(__file__ + '/../templates')
    server = ShireWeb(routes, template_path)
    server.run()
