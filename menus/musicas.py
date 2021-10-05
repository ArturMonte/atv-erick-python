import db
from ajudantes import montar_menu
from menus import playlists


def __listar():
    con = db.conexao()
    cur = con.cursor()

    sql = 'SELECT * FROM musicas'

    cur.execute(sql)

    musicas = cur.fetchall()

    print(f'\nMúsicas [Total:{len(musicas)}]')

    for musica in musicas:
        print(f'\nID: {musica[0]}')
        print(f'NOME: {musica[1]}')
        print(f'ARTISTA: {musica[2]}')
        print(f'ÁLBUM: {musica[3]}')
        print(f'ANO: {musica[4]}')
        print(f'ARQUIVO: {musica[5]}')

    con.close()


def __cadastrar():
    nome = input('Nome: ')
    artista = input('Artista: ')
    album = input('Álbum: ')
    ano = int(input('Ano: '))
    arquivo = input('Arquivo: ')

    con = db.conexao()
    cur = con.cursor()

    sql = 'INSERT INTO musicas(nome, artista, album, ano, arquivo) VALUES (?, ?, ?, ?, ?)'

    cur.execute(sql, (nome, artista, album, ano, arquivo))

    con.commit()
    con.close()

    print('Música cadastrada com sucesso.')


def __alterar():
    id = input('Id: ')
    nome = input('Nome: ')
    artista = input('Artista: ')
    album = input('Álbum: ')
    ano = int(input('Ano: '))
    arquivo = input('Arquivo: ')

    con = db.conexao()
    cur = con.cursor()

    sql = 'UPDATE musicas SET nome = ?, artista = ?, album = ?, ano = ?, arquivo = ? WHERE id = ?'

    cur.execute(sql, (nome, artista, album, ano, arquivo, id))

    con.commit()
    con.close()

    print(f'Id {id} atualizado com sucesso.')


def __excluir():
    id = input('Id: ')

    con = db.conexao()
    cur = con.cursor()

    sql = 'DELETE FROM musicas WHERE id = ?'

    cur.execute(sql, (id,))

    con.commit()
    con.close()

    print(f'Id {id} excluído com sucesso.')


def menu():
    executar = True

    while executar:
        opcoes = ['Listar', 'Cadastrar', 'Alterar', 'Excluir', 'Playlists']

        opcao = montar_menu(opcoes, nome='Músicas', voltar=True)

        if opcao == 1:
            __listar()

        if opcao == 2:
            __cadastrar()

        if opcao == 3:
            __alterar()

        if opcao == 4:
            __excluir()

        if opcao == 5:
            playlists.menu()

        if opcao == len(opcoes):
            executar = False
