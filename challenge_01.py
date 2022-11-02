class Produtos():
    def __init__(self):
        self.id = id
        self.lista_de_produtos = {'Café': 100, 'Açúcar': 200, 'MATEUS': 0}

        if(not self.lista_de_produtos): raise Exception('Lista de Produtos Vazia!')

    def listaProdutos(self):
        lista = 'ID - PRODUTO - PREÇO'
        for n, i in enumerate(self.lista_de_produtos):
            if((n + 1) <= len(self.lista_de_produtos)): lista += '\n'
            lista += ('{} - {} | R$ {}'.format((n + 1), i, self.lista_de_produtos[i]))
        return lista

    def pegaId(self):
        id = int(input('\nSelecione o produto: '))
        if((id <= 0) or (id > len(self.lista_de_produtos))):
            print('Passe um ID correto!')
            id = Produtos.pegaId(self)
        return id

    def pegaQuantidade(self):
        quantidade = int(input('\nPasse a quantidade: '))
        if((quantidade < 0)):
            print('Passe uma quantidade correta!')
            quantidade = Produtos.pegaQuantidade(self)
        return quantidade

    def nomeProduto(self, id = 0):
        for n, i in enumerate(self.lista_de_produtos):
            if((n + 1) == id):
                return i
        return 'Error'

    def valorProduto(self, id = 0):
        preco = 0
        for n, i in enumerate(self.lista_de_produtos):
            if((n + 1) == id):
                preco = self.lista_de_produtos[i]
        return preco

    def valorFrete(self, quantidade = 0):
        if(quantidade >= 1001): return 240
        elif(quantidade >= 101): return 120
        elif(quantidade >= 11): return 60
        elif(quantidade >= 0): return 30
        return 0

def main():
    loja = Produtos()
    print(loja.listaProdutos())
    id = loja.pegaId()
    quantidade = loja.pegaQuantidade()
    nome = (loja.nomeProduto(id))
    valor = (loja.valorProduto(id))
    frete = (loja.valorFrete(quantidade))
    print('Nome do produto: {}, valor do produto: {}, valor do frete: {}.'.format(nome, valor, frete))

main()