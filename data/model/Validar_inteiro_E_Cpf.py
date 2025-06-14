class Validar_Inteiro_E_Cpf:
    def __init__(self, inteiro: int) -> None:
        self._inteiro = inteiro

    def validar_inteiro(self) -> None:
        if self._inteiro.isdigit():
            self._inteiro = int(self.inteiro)
        else:
            print("Digite um numero válido: ")
    
    def cpf(self, inteiro: int) -> str:
        if len(inteiro) == 11:
            cpf_formatado = re.sub(r"(\d{3})(\d{3})(\d{3})(\d{2})", r"\1.\2.\3-\4", Validar_Inteiro_E_Cpf.inteiro())
            return cpf_formatado
        else:
            print("digite 11 numeros: ")