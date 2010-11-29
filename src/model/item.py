
from google.appengine.ext import db

class item(db.Model):
    nome = db.StringProperty(required=False)
    descricao = db.StringProperty(required=False)
    usuario = db.UserProperty()

