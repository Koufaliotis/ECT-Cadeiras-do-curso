import cherrypy

class Root:
    @cherrypy.expose
    def index(self):
        return "Bem-vindo à aplicação! Use /form para acessar o formulário."

    @cherrypy.expose
    def form(self):
        # Define o tipo de conteúdo como HTML
        cherrypy.response.headers["Content-Type"] = "text/html"
        # Retorna o conteúdo do arquivo HTML
        try:
            with open("formulario.html", "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "Erro: O arquivo 'formulario.html' não foi encontrado."
        except Exception as e:
            return f"Erro ao carregar o formulário: {str(e)}"

if __name__ == "__main__":
    # Inicializa o servidor CherryPy
    cherrypy.quickstart(Root(), "/")
