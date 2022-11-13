class ServicoLimpeza():
    def __init__(self):
        #tabela dos tipos de limpeza e multiplicador
        self.tipo_limpeza = {
            "B": ["Básica", 1],
            "C": ["Completa", 1.3]
            }
        #tabela de adicionais e valores 
        self.adicionais = {
            0: ["Não desejo mais nada", 0],
            1: ["Passar 10 peças de roupas - R$ 10,00", 10],
            2: ["Limpeza de 1 Forno/Micro-ondas - R$ 12,00", 12],
            3: ["Limpeza de 1 Geladeira/Freezer - R$ 20,00", 20],
        }

    def metragem_limpeza(self):
        self.valor_metragem = 0
        while True:
            try:
                #recebe o valor da metragem
                self.metragem = int(input('Digite a metragem da casa (m²): '))
                #valida se o valor da metragem está entre 300 e 700
                if (300 <= self.metragem < 700):
                    self.valor_metragem = 120 + (0.5 * self.metragem)
                    print(f"O valor por metragem é de R$ {self.valor_metragem}")
                    print("-" * 52)
                #valida se o valor da metragem está entre 30 e 300
                elif (30 <= self.metragem < 300):
                    self.valor_metragem = 60 + (0.3 * self.metragem)
                    print(f"O valor por metragem é de R$ {self.valor_metragem}")
                    print("-" * 52)
                # verifica se o valor digitado atende as condições para proseguir
                # se for um numero e dentro do limite, segue o programa
                if type(self.metragem) == int and 30 <= self.metragem < 700: 
                    return
                print('Digite uma metragem válida!')
            except ValueError: # não foi digitado um número
                print('Digite um número!')
        
    def tipos_limpeza(self):
        self.multiplicador_tipo_limpeza = 0
        while True:
            try:
                self.tipo_limpeza_selecionada = str(input("Selecione o tipo de limpeza desejada (B - Básica / C - Completa): ")).upper().split()[0]
                for i in self.tipo_limpeza:
                    #se o tipo selecionado estiver na lista e for tipo básico atribui o valor multiplicador
                    if (i == self.tipo_limpeza_selecionada and i == "B"):
                        self.multiplicador_tipo_limpeza = self.tipo_limpeza[i][1]
                        print("O tipo de limpeza selecionada foi: " + self.tipo_limpeza[i][0])
                    #se o tipo selecionado estiver na lista e for tipo completa atribui o valor multiplicador
                    elif (i == self.tipo_limpeza_selecionada and i == "C"):
                        self.multiplicador_tipo_limpeza = self.tipo_limpeza[i][1]
                        print("O tipo de limpeza selecionada foi: " + self.tipo_limpeza[i][0])
                #verifica se o valor digitado é válido para seguir o programa
                if (self.tipo_limpeza_selecionada == "B" or self.tipo_limpeza_selecionada == "C"):
                    return
                else:
                    print("Digite um tipo de limpeza válida!")
            except ValueError: # não foi digitado um código válido
                print('O valor digitado não está dentro da lista!')

    def adicional_limpeza(self):
        self.valor_adicionais = 0
        while True:
            try:
                print("-" * 52)
                print("DESEJA ALGUM ADIDICIONAL:")
                print("-" * 52)
                #mostra os adicionais na tela
                for i in self.adicionais:
                    ID = str(i)
                    print(ID + "-" + (self.adicionais[i])[0])
                #pega o adicional desejado          
                self.adicional_selecionado = int(input("Selecione um adicional: "))
                for i in self.adicionais:
                    #se o adicional for 1, mostra o adicional selecionado e determina o valor a somar
                    if (i == self.adicional_selecionado and i == 1):
                        print((self.adicionais[i])[0] + " selecionada!")
                        print("-" * 52)
                        self.valor_adicionais = self.valor_adicionais + int(self.adicionais[i][1])
                    #se o adicional for 1, mostra o adicional selecionado e determina o valor a somar
                    elif (i == self.adicional_selecionado and i == 2):
                        print((self.adicionais[i])[0] + " selecionada!")
                        print("-" * 52)
                        self.valor_adicionais = self.valor_adicionais + int(self.adicionais[i][1])
                    #se o adicional for 1, mostra o adicional selecionado e determina o valor a somar
                    elif (i == self.adicional_selecionado and i == 3):
                        print((self.adicionais[i])[0] + " selecionada!")
                        print("-" * 52)
                        self.valor_adicionais = self.valor_adicionais + int(self.adicionais[i][1])
                if (self.adicional_selecionado == 0):
                    return
            except: #se digitado um valor fora inteiro retorna o erro
                print("Adicional não existe!!")

    def calculaTotal(self):
        #calcula o valor total da limpeza
        total = self.valor_metragem * self.multiplicador_tipo_limpeza + self.valor_adicionais
        #imprime os valores de cada passo separados
        print("(O valor da metragem: R$ {} * Tipo de metragem: {} + Valor dos adicionais: R$ {})".format(self.valor_metragem, self.multiplicador_tipo_limpeza, self.valor_adicionais))
        print("O valor total é de: R$ {}".format(total)) #imprime o valor total da limpeza

LimpezaAlmeida = ServicoLimpeza()
LimpezaAlmeida.metragem_limpeza()
LimpezaAlmeida.tipos_limpeza()
LimpezaAlmeida.adicional_limpeza()
LimpezaAlmeida.calculaTotal()