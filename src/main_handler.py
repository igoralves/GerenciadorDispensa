import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from src.model import *

class Delete(webapp.RequestHandler):

    def get(self):
        it = item()
        no_banco = item.all().filter("nome =", self.request.get('nome')).fetch(1)
        no_banco[0].delete()
        
        self.redirect('/')

class Create(webapp.RequestHandler):
    
    def post(self):
        
        novo_item = item()
        
        novo_item.nome = self.request.get('nome')
        novo_item.descricao = self.request.get('descricao')
        novo_item.put()
        
        self.redirect('/')
    
    def get(self):
        
        render(self.response, 'html/create.html')

class Index(webapp.RequestHandler):

    def get(self):
        
        items_query = item.all().order('nome')
        items = items_query.fetch(10)
        
        template_values = {'itens': items,
                           'num_items': len(items)}
        
        render(self.response, 'html/index.html', template_values)

application = webapp.WSGIApplication(
                                     [('/', Index),
                                     ('/create', Create),
                                     ('/delete', Delete)],
                                     debug=True)

def render(response, caminho, template_values = {}):
    path = os.path.join(os.path.dirname(__file__), caminho)
    response.out.write(template.render(path, template_values))


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
