def montar_menu(opcoes: list, nome=None, voltar=False) -> int:
    print(f'\n{nome}: ' if nome else '\nMenu:')

    if voltar:
        opcoes.append('Voltar para o menu anterior')

    for opcao in range(len(opcoes)):
        print(f'\t{opcao + 1} - {opcoes[opcao]}')

    opcao = input('\nDigite o número da opção: ')
    while True:

        try:
            if (int(opcao) - 1) in range(len(opcoes)):
                break
        except ValueError:
            pass

        opcao = input('Digite uma opção válida: ')

    return int(opcao)
