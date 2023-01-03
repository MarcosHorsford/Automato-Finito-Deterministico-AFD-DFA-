def null(var):
    return var == []


class AFD:
    def __init__(self):
        self.estados = []
        self.estado_final = []
        self.estado_inicial = None
        self.palavra = None
        self.alfabeto = []
        self.trasicao = {}

    def add_alfabeto(self):
        while True:
            menu_alfa = int(input('1 - adicionar alfabeto\n0 - sair\n>>>>>'))
            if menu_alfa == 1:
                alfa = str(input('alfabeto(Σ) >>>>> '))
                self.alfabeto.append(alfa)
                continue
            else:
                return False

    def add_estado(self):

        while True:

            menu_add_estado = int(input("\n1 - para adicionar estado\n0 - executar\n>>>>> "))

            if menu_add_estado == 1:

                add_state = input("\nAdicione o estado: ")
                self.estados.append(add_state)  # Essa linha adiciona estados na lista de estados
                is_inti_or_final = int(input("\n1 - Estado Inicial\n2 - Estado Final\n3 - Estado Final e Inicial\n"
                                             "0 - se for comum\n>>>>> "))
                # esse bloco define estados inicial e finais:
                if is_inti_or_final == 1:
                    self.estado_inicial = add_state
                elif is_inti_or_final == 2:
                    self.estado_final.append(add_state)
                elif is_inti_or_final == 3:
                    self.estado_inicial = add_state
                    self.estado_final.append(add_state)
                elif is_inti_or_final == 0:
                    continue
            elif menu_add_estado == 0:
                return False

    def add_transition(self):
        print('\nTransição:')
        menu_add_trasicao = int(input('\nAdicionar Transição - 1\nManter a atual - 0\n>>>> '))
        if menu_add_trasicao == 1:
            for estado_index in self.estados:
                for _ in self.alfabeto:
                    origem = estado_index
                    entrada = str(input(f'{estado_index} lendo -> '))
                    destino = str(input(f'({estado_index}, {entrada})>>>> '))
                    self.trasicao.update({(origem, entrada): destino})
        elif menu_add_trasicao == 0:
            return self.trasicao

    def add_palavra(self):
        word = str(input('\nPalavra >>> '))
        self.palavra = word

    def verif_alfabeto(self):  # Faz a verificação se os simbolos da palavra pertencem ao alfabeto
        for simbolo_atual in self.palavra:
            if simbolo_atual in self.alfabeto:
                continue
            else:
                print(f'{simbolo_atual} -> não pertence aos simbolos da linguagem!!!')
                exit()

    def afd(self):  # AFD
        qA = self.estado_inicial
        for simbolo_atual in self.palavra:
            qA = self.trasicao[(qA, simbolo_atual)]
        return qA in self.estado_final


if __name__ == '__main__':   # Teste de execução
    var_afd = AFD()
    var_afd.add_estado()
    var_afd.add_alfabeto()
    var_afd.add_transition()
    var_afd.add_palavra()
    var_afd.afd()

    print(f'Estados >>> {var_afd.estados}\nΣ >>> {var_afd.alfabeto}\nEstado Inicial >>> {var_afd.estado_inicial}'
          f'\nEstados Finais >>> {var_afd.estado_final}\nTransição >>> {var_afd.trasicao}\n\n\nA palavra é aceita?'
          f' {var_afd.afd()}')
