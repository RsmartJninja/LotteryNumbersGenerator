#!/usr/bin/env python
import os
import jinja2
import webapp2
from random import randint


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

class LotteryHandler(BaseHandler):
    def get(self):
        rand = randint(1,45)
        rand1 = randint(1,45)
        rand2 = randint(1,45)
        rand3 = randint(1, 45)
        rand4 = randint(1, 45)
        rand5 = randint(1, 45)
        quote = [rand, rand1, rand2, rand3, rand4, rand5]
        return self.write(quote)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/lottery', LotteryHandler),
], debug=True)
