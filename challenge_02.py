#Painel de produtos e preços
print('''
Bem-vindo a Sorveteria do Mateus de Almeida
______________________________________________CARDÁPIO_________________________________________________
_______________________________________________________________________________________________________
|  CÓDIGO  |      DESCRIÇÃO       |  Tamanho P (500ml)  |  Tamanho M (1000ml)  |  Tamanho G (1500ml)  |
|---------------------------------|---------------------|----------------------|----------------------|
|    TR    | Sabores Tradicionais |       R$ 6,00       |       R$ 10,00       |       R$ 18,00       |
|    ES    | Sabores Especiais    |       R$ 7,00       |       R$ 12,00       |       R$ 21,00       |
|    PR    | Sabores Premium      |       R$ 8,00       |       R$ 14,00       |       R$ 24,00       |
|----------|----------------------|---------------------|----------------------|----------------------|
''')
class Sorveteria():
    def __init__(self):
        self.preco_total = 0
        self.pedido2 = ''
        #dicionário com produtos e preços
        self.lista_produtos = {
            'TR': {'Descrição': ['Sabores Tradicionais', 'Tradicional'], 'Preços': {'P': 6, 'M': 10, 'G': 18}},
            'ES': {'Descrição': ['Sabores Especiais', 'Especial'], 'Preços': {'P': 7, 'M': 12, 'G': 21}},
            'PR': {'Descrição': ['Sabores Premium', 'Premium'], 'Preços': {'P': 10, 'M': 14, 'G': 24}},
        }

    def pegaPedido(self):
        codigos = ""
        #recebe o tamanho do pote de sorvete
        self.tamanho = input("Entre com o TAMANHO do pote desejado (P/M/G): ").upper().split()[0] 
        if (self.tamanho == 'P' or self.tamanho == 'M' or self.tamanho == 'G'): 
            for i, j in enumerate(self.lista_produtos):
                if (i > 0):
                    codigos += '/'
                codigos += str(j)
            #recebe o codigo do pote de sorvete
            self.codigo = input("Entre com o CÓDIGO do pote desejado ({}): ".format(codigos)).upper().split()[0]
            #verifica se o código digitado está presente no dicionário
            for j in self.lista_produtos: 
                if(str(self.codigo)== str(j)): return
            print("!!!!!! TAMANHO OU CÓDIGO DE SORVETE INVÁLIDO !!!!!!")
            #se o código for inválido solicita novamente as informações do pedido
            Sorveteria.pegaPedido(self) 
        else:
            print("!!!!!! TAMANHO OU CÓDIGO DE SORVETE INVÁLIDO !!!!!!")
            # se o tamanho for inválido solicita novamente as informações do pedido
            Sorveteria.pegaPedido(self) 
            
    def calculaValor(self):
        while(True):
            sabor = ''
            preco = 0
            
            for i in self.lista_produtos:
                if(i == self.codigo):
                    #pega a descrição do sorvete do dicionario
                    sabor = self.lista_produtos[i]['Descrição'][1] 
                    #pega o preço do produto do dicionario
                    preco = self.lista_produtos[i]['Preços'][self.tamanho] 
                    #soma os valores dos sorvetes pedidos
                    self.preco_total += int(self.lista_produtos[i]['Preços'][self.tamanho])
            texto = ('Você pediu um sorvete sabor {} de R$ {},00'.format(sabor, preco))
            print(texto)
            print('-' * len(texto))
            #pergunta se o cliente quer mais alguma coisa
            self.pedido2 = input("Deseja pedir mais alguma coisa? (S/N): ").upper().split()[0]
            #caso queira, chama novamente a função pegaPedido para selecionar os tamanhos
            if(self.pedido2 == 'S'): 
                Sorveteria.pegaPedido(self)
            #caso nao queira para o laço de repetição e o pedido é finalizado
            elif(self.pedido2 == 'N'): 
                print("O preço total a ser pago é de R$ {},00".format(self.preco_total))
                break

MinhaSorveteria = Sorveteria()
MinhaSorveteria.pegaPedido()
MinhaSorveteria.calculaValor()