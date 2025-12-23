from . import Atleta, Covid, Medalhas
import re

class Cadastro():
    def cadastrar_atletas(self) -> Atleta:
        cpf = questionary.text(
            "CPF",
            validate = self.validar_cpf
        ).ask()
        idade = questionary.text(
            "Idade",
            validate = self.validar_inteiro
        ).ask()
        sexo = self.opcoes("Sexo do atleta", ["M", "F"])
        questonario_covid = self.covid()
        questionario_medalhas = self.medalhas()

        atleta = Atleta.Atleta(int(idade), sexo, self.formatar_cpf(cpf), questonario_covid, questionario_medalhas)

        return atleta

    def covid(self) -> Covid:
        teve_febre = self.opcoes("Teve febre?", ["S", "N"])
        match teve_febre:
            case "S":
                temperatura_corporal = questionary.text(
                    "Temperatura corporal",
                    validate = self.validar_float
                ).ask()
            case "N":
                temperatura_corporal = None

        teve_outro_sintoma = self.opcoes("Teve_outro_sintoma?", ["S", "N"])
        kit_covid = self.opcoes("Tomou kit covid?", ["S", "N"])
        
        covid = Covid.Covid(teve_febre, temperatura_corporal, teve_outro_sintoma, kit_covid)

        return covid
    
    def opcoes(self, texto: str, lista_de_opcoes: list) -> str:
        opcao = questionary.select(
            texto,
            choices = lista_de_opcoes
        ).ask()

        return opcao
    
    def medalhas(self) -> Medalhas:
        ganhou_medalhas = self.opcoes("Ganhou medalhas?", ["S", "N"])
        match ganhou_medalhas:
            case "S":
                ouro = questionary.text(
                            "Ouro",
                            validate = self.validar_inteiro
                        )
                prata = questionary.text(
                            "Prata",
                            validate = self.validar_inteiro
                        )
                bronze = questionary.text(
                            "Bronze",
                            validate = self.validar_inteiro
                        )
            case "N":
                ouro = 0
                prata = 0
                bronze = 0
        
        medalhas = Medalhas.Medalhas(int(ouro), int(prata), int(bronze))

        return medalhas

    def validar_inteiro(self, text):
        try:
            valor = int(text)
            return True
        except ValueError:
            return "Digite um numero valido"

    def validar_cpf(self, text):
        try:
            if len(text) != 11 or not text.isdigit():
                return "Digite um cpf valido."
            return True
        except:
            return "Digite um CPF valido"
    
    def validar_float(self, text):
        try:
            valor = float(text)
            return True
        except ValueError:
            return "Digite um numero valido"

    def formatar_cpf(self, cpf: str) -> str:
        formatado = re.sub(r"(\d{3})(\d{3})(\d{3})(\d{2})", r"\1.\2.\3-\4", cpf)
        return formatado