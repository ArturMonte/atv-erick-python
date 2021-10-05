from menus import contatos, musicas, produtos
import db
from ajudantes import montar_menu


def programa():
    executar = True

    while executar:
        opcoes = ['Contatos', 'Músicas', 'Produtos', 'Sair']

        opcao = montar_menu(opcoes)

        if opcao == 1:
            contatos.menu()

        if opcao == 2:
            musicas.menu()

        if opcao == 3:
            produtos.menu()

        if opcao == len(opcoes):
            executar = False


if __name__ == '__main__':
    db.iniciar()
    programa()
