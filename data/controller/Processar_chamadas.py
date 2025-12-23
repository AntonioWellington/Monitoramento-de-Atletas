from ..model.Json import Json
from sql.DML.Insert import Inserir
from ..model.Relatorio import Relatorio
from ..model.Atleta import Atleta
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class Controller(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/cadastrar":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body)

            atleta = Atleta(idade=data["idade"], sexo=data["sexo"], cpf=data["cpf"])
            inserir = Inserir()
            inserir.inserir_tabelas(atleta)
            '''salvar = Json(atleta.transformar_em_dicionario())
            salvar.gravar_dados()'''

            response = {"message": f"Atleta {atleta.cpf} inserido com sucesso"}
            self.send_response(201)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

          
    '''def GET(self):
        if self.PATCH == "/relatorio":'''
             

    '''def PUT(self):
    def DELETE(self):
    def PATCH(self):'''
  
        