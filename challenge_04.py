class Cadastrador():
    def __init__(self):
        dados_funcionario = {
            "ID": 0,
            "NOME": "",
            "SETOR": "",
            "SALARIO": 0
        }
    def cadastra_funcionario(self, ID):
        self.ID = ID
        while True:
            try:
                nome_funcionario = str(input("Entre com o nome do funcionário: ")).upper()
                setor_funcionario = str(input("Entre com o setor do funcionário: ")).upper()
                salario_funcionario = float(input("Entre com o salário do funcionário: "))
                if (type(nome_funcionario)) == str: continue
                if (type(setor_funcionario)) == str: continue
                if (type(salario_funcionario)) == float: continue
                else:
                    print("Valores digitados não são válidos!")
            except ValueError: pass

    def visualiza_funcionario(self):
        pass
    def remove_funcionario(self):
        pass