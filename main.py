from http.server import BaseHTTPRequestHandler, HTTPServer
from data.controller.Processar_dados import Controller

def run(server_class=HTTPServer, handler_class=Controller):
    server_address = ('', 8000)  # rodar na porta 8000
    httpd = server_class(server_address, handler_class)
    print("Servidor rodando em http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run()