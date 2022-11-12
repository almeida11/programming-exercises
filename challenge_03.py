class ServicoLimpeza():
    def __init__(self):
        self.tipo_limpeza = {
            "B": ["Básica", 1],
            "C": ["Completa", 1.3]
            }

        self.adicionais = {
            0: ["Não desejo mais nada", 0],
            1: ["Passar 10 peças de roupas - R$ 10,00", 10],
            2: ["Limpeza de 1 Forno/Micro-ondas - R$ 12,00", 12],
            3: ["Limpeza de 1 Geladeira/Freezer - R$ 20,00", 20],
        }

    def pegaMetragem(self):
        self.valor_limpeza = 0
        while True:
            try:
                #recebe o valor da metragem
                self.metragem = int(input('Digite a metragem da casa (m²): '))
                if (300 <= self.metragem < 700):
                    self.valor_limpeza = 120 + (0.5 * self.metragem)
                elif (30 <= self.metragem < 300):
                    self.valor_limpeza = 60 + (0.3 * self.metragem)
                # verifica se o valor digitado atende as condições para proseguir
                if type(self.metragem) == int and 30 <= self.metragem < 700: # se for um numero, segue o programa
                    return
                print('Digite um valor válido!')
            except ValueError: # não foi digitado um número
                print('Digite um número válido!')
        
    def pegaTipoLimpeza(self):
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
                    print("Digite um código válido!")
            except ValueError: # não foi digitado um código válido
                print('O valor digitado não está dentro da lista!')

    def pegaAdicionaisLimpeza(self):
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
                    #se o adicional for 1, mostra o adicional selecionado e determina o valor a somar
                    elif (i == self.adicional_selecionado and i == 2):
                        print((self.adicionais[i])[0] + " selecionada!")
                        print("-" * 52)
                    #se o adicional for 1, mostra o adicional selecionado e determina o valor a somar
                    elif (i == self.adicional_selecionado and i == 3):
                        print((self.adicionais[i])[0] + " selecionada!")
                        print("-" * 52)
                if (self.adicional_selecionado == 0):
                    return
            except:
                print("Adicional não existe!!")

#total = metragem * tipo + adicionais
LimpezaAlmeida = ServicoLimpeza()
LimpezaAlmeida.pegaMetragem()
LimpezaAlmeida.pegaTipoLimpeza()
LimpezaAlmeida.pegaAdicionaisLimpeza()