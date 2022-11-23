
lista_funcionarios = []
#cadastro de funcionario
def menuPrograma():
    matricula_funcionario = 0
    while True:
        try:
            print("""
    1) Cadastrar Funcionário
    2) Visualizar Funcionário(s)
    3) Remover Funcionário
    4) Sair
            """)
            selecao = int(input("Entre com a opção: "))
            if selecao == 1:
                matricula_funcionario = matricula_funcionario + 1
                cadastrarFuncionario(matricula_funcionario)
            elif selecao == 2:
                visualizarFuncionario()
            elif selecao == 3:
                removerFuncionario()
            elif selecao == 4:
                break
            else:
                print("Opção Inválida!")
                menuPrograma()
        except ValueError:
            print("Digite um valor válido!")
def cadastrarFuncionario(ID):
    print("---JANELA DE CADASTRO DE FUNCIONÁRIO---")
    print(f"A matrícula do funcionário é: {ID}")
    nome = input("Entre com o NOME do funcionário: ")
    setor = input("Entre com o SETOR do funcionário: ")
    salario = input("Entre com o SALÁRIO do funcionário: ")

    dados_funcionario = {
        "MATRICULA": ID,
        "NOME": nome,
        "SETOR": setor,
        "SALARIO": salario
    }
    lista_funcionarios.append(dados_funcionario.copy())
#visualização de informações do funcionário
def visualizarFuncionario():
    while True:
        try:
            print("""
            1) Consultar Todas as Funcionários
            2) Consultar Funcionário por Id
            3) Consultar Funcionário(s) por Setor
            4) Retornar 
                    """)
            selecao = int(input("Entre com a opção: "))
            #mostrar todos os funcionarios
            if selecao == 1:
                print(lista_funcionarios) #apenas para visualizar o formato da lista

                for i in lista_funcionarios:
                    for keys in i:
                        print(f"{keys}: ")
                        for value in keys:
                            print(value)
            #mostrar funcionario por ID
            elif selecao == 2:
                pass
            #mostrar funcionarios por setor
            elif selecao == 3:
                pass
            #retornar ao menu
            elif selecao == 4:
                break
            else:
                print("Opção Inválida!")
                visualizarFuncionario()
        except ValueError:
            print("Digite um valor válido!")
#remover dados de um funcionário
def removerFuncionario():
    pass

menuPrograma()
cadastrarFuncionario()
visualizarFuncionario()
removerFuncionario()