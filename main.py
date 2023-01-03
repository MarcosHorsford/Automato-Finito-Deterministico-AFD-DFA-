from automato import AFD


def main():
    var_afd = AFD()
    var_afd.add_estado()
    var_afd.add_alfabeto()
    var_afd.add_transition()
    var_afd.add_palavra()
    var_afd.verif_alfabeto()
    var_afd.afd()
    print(f'Estados >>> {var_afd.estados}\nΣ >>> {var_afd.alfabeto}\nEstado Inicial >>> {var_afd.estado_inicial}'
          f'\nEstados Finais >>> {var_afd.estado_final}\nTransição >>> {var_afd.trasicao}\n\n\nA palavra é aceita?'
          f' {var_afd.afd()}')
    option = int(input(f'0 - Sair\n1 - Testar nova entrada'))
    while option != 0:
        var_afd.add_palavra()
        var_afd.verif_alfabeto()
        var_afd.afd()
        print(f'Estados >>> {var_afd.estados}\nΣ >>> {var_afd.alfabeto}\nEstado Inicial >>> {var_afd.estado_inicial}'
              f'\nEstados Finais >>> {var_afd.estado_final}\nTransição >>> {var_afd.trasicao}\n\n\nA palavra é aceita?'
              f' {var_afd.afd()}\n')
        option = int(input(f'0 - Sair\n1 - Testar nova entrada \n>>>>> '))


main()
