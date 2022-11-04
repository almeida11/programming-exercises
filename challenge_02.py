class Loja():
    def _init_(self, nome):
        self.preco_total = 0
        self.op = 'S'
        print('Bem-vindos a Sorveteria do {}'.format(nome))
        self.lista_de_produtos = {
            'TR': {'Descrição': ['Sabores Tradicionais', 'Tradicional'], 'Preços': {'P': 6, 'M': 10, 'G': 18}},
            'ES': {'Descrição': ['Sabores Especiais', 'Especial'], 'Preços': {'P': 7, 'M': 12, 'G': 21}},
            'PR': {'Descrição': ['Sabores Premium', 'Premium'], 'Preços': {'P': 10, 'M': 14, 'G': 24}},
            #'MS': {'Descrição': ['Sabores Master', 'Master'], 'Preços': {'P': 500, 'M': 750, 'G': 1000}}
        }

        desc_len = 0
        for i in self.lista_de_produtos:
            if desc_len < len(self.lista_de_produtos[i]['Descrição'][0]):
                desc_len = len(self.lista_de_produtos[i]['Descrição'][0])

        cod_text = 'Código'
        cod_len = len(cod_text)

        desc_text = 'Descrição'
        desc_text = ' ' * int((desc_len - (len(desc_text))) / 2) + desc_text + ' ' * int((desc_len - (len(desc_text))) / 2)
        desc_text += ' ' if (len(desc_text) < (desc_len + 2)) else ''
        
        tamp_text = 'Tamanho P (500ml)'
        tamm_text = 'Tamanho M (1000ml)'
        tamg_text = 'Tamanho G (1500ml)'

        title = '| {} | {} | {} | {} | {} |'.format(cod_text, desc_text, tamp_text, tamm_text, tamg_text)
        dash = '-'*int((len(title) - 8)/2) + 'Cardápio' + '-'*int((len(title) - 8)/2)
        if len(dash) < len(title): dash += '-'

        print(dash)
        print(title)

        for i in self.lista_de_produtos:
            print('|' + ' ' * int(1 * (cod_len / 2)) + i + ' ' * (1 * int(cod_len / 2)) + '|', end='')
            desc_temp_len = len(self.lista_de_produtos[i]['Descrição'][0])
            text = (' ' * (1 + int((desc_len - desc_temp_len) / 2)) + self.lista_de_produtos[i]['Descrição'][0] + ' ' * (1 + int((desc_len - desc_temp_len) / 2)))
            text += ' |' if (len(text) < (desc_len + 2)) else '|'
            print(text, end='')

            for j, k in enumerate(self.lista_de_produtos[i]['Preços']):
                if j == 0: tam_len = len(tamp_text)
                elif j == 1: tam_len = len(tamm_text)
                elif j == 2: tam_len = len(tamg_text)
                preco = 'R$ {},00'.format(self.lista_de_produtos[i]['Preços'][k])
                tam_temp_len = len(str(preco))
                text = ' ' * (1 + int((tam_len - tam_temp_len) / 2)) + str(preco) + ' ' * (1 + int((tam_len - tam_temp_len) / 2))
                text += ' |' if (len(text) < (tam_len + 2)) else '|'
                if(j != 2): print(text, end='')
                elif(j == 2): print(text)
    
    def getTamanho(self):
        self.tamanho = input('Entre com o TAMANHO do pote desejado (P/M/G): ')
        self.tamanho = self.tamanho.upper()
        if (self.tamanho == 'P' or self.tamanho == 'M' or self.tamanho == 'G'): return
        print('!!!!!! TAMANHO DE POTE INVÁLIDO !!!!!!')
        Loja.getTamanho(self)
    
    def getCodigo(self):
        codigos = ''
        for i, j in enumerate(self.lista_de_produtos):
            if (i > 0):
                codigos += '/'
            codigos += str(j)

        self.codigo = input('Entre com o CÓDIGO do pote desejado ({}): '.format(codigos))
        self.codigo = self.codigo.upper()
    
        for j in self.lista_de_produtos:
            if(str(self.codigo) == str(j)): return

        print('!!!!!! CÓDIGO DE SORVETE INVÁLIDO !!!!!!')
        Loja.getCodigo(self)

    def getOp(self):
        self.op = input('Desja pedir mais alguma coisa? (S/N): ')
        self.op = self.op.upper()
        if(self.op == 'S' or self.op == 'N'): return
        print('!!!!!! OPÇÃO INVÁLIDA !!!!!!')
        Loja.getOp(self)

    def pedido(self):
        while(True):
            Loja.getTamanho(self)
            Loja.getCodigo(self)
            sabor = ''
            preco = 0
            for i in self.lista_de_produtos:
                if(i == self.codigo):
                    sabor = self.lista_de_produtos[i]['Descrição'][1]
                    preco = self.lista_de_produtos[i]['Preços'][self.tamanho]
                    self.preco_total += int(self.lista_de_produtos[i]['Preços'][self.tamanho])
            texto = ('Você pediu um sorvete sabor {} de R$ {},00'.format(sabor, preco))
            print(texto)
            print('-' * len(texto))
            Loja.getOp(self)
            if(self.op == 'S'): continue
            elif(self.op == 'N'): break
    
    def main(self):
        Loja.pedido(self)
        
        print('O total a ser pago é: R$ {},00'.format(self.preco_total))

lojaDoMateus = Loja('Matheus de Almeida')
lojaDoMateus.main()