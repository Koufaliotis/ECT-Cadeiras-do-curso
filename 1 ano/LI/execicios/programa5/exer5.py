import cherrypy
import psutil

class Node():
    @cherrypy.expose
    def index(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        return "Eu sou o indice do Node (Node.index),cpu: {}".format(cpu_percent)
    @cherrypy.expose
    def page(self):
        return "Eu sou o metodo do node"
    
class HtmlFile():
    @cherrypy.expose
    def htmlfile(self):
        with open("htmlfile.html",'r',encoding="utf-8") as myfile:
            
            return myfile.read()
    
class Root():
    def __init__(self): #this is how to assosiate difrent classes
        self.node = Node() ##what is node?
        self.html = HtmlFile()
    @cherrypy.expose
    def index(self):
        return "Eu sou o índice do Root (Root.index)"
    @cherrypy.expose
    def page(self):
        return "Eu sou um método do Root (Root.page)"

if __name__ == "__main__":
    cherrypy.quickstart(Root(), "/")