from argparse import Action
import cherrypy
class Node():
    @cherrypy.expose
    def index(self):
        return "Eu sou o índice do Node (Node.index)"
    @cherrypy.expose
    def page(self):
        return "Eu sou um método do Node (Node.page)"
class Actions:
        @cherrypy.expose
        def doLogin(self, username=None, password=None):
            return "Verificar as credenciais do utilizador " + username


class HTMLDocument():
    
    @cherrypy.expose
    def HtmlPage(self):
        return open("TutorialWEB1/html/index.html")

    @cherrypy.expose
    def form(self):
        cherrypy.response.headers["Content-Type"] = "text/html"
        return open("formulario.html")

    def __init__(self):
        self.actions = Actions()
    
    @cherrypy.expose
    def actions(self):
        return self.actions
    
class Root():
    def __init__(self):
        self.node = Node()
        self.pageSel = HTMLDocument()
    @cherrypy.expose
    def index(self):
        return """welcome to the index
            \n    o
            \n  / | \\ 
            \n   / \\"""
    
cherrypy.quickstart(Root(),"/")