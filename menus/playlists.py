import db
from ajudantes import montar_menu


def __listar():
    con = db.conexao()
    cur = con.cursor()

    sql = 'SELECT * FROM playlists'

    cur.execute(sql)

    playlists = cur.fetchall()

    print(f'\nPlaylists [Total:{len(playlists)}]')

    for playlist in playlists:
        print(f'\nID: {playlist[0]}')
        print(f'NOME: {playlist[1]}')
        print(f'DATA: {playlist[2]}')

    con.close()


def __cadastrar():
    nome = input('Nome: ')
    data = input('Data: ')

    con = db.conexao()
    cur = con.cursor()

    sql = 'INSERT INTO playlists(nome, data) VALUES (?, ?)'

    cur.execute(sql, (nome, data))

    con.commit()
    con.close()

    print('Playlist cadastrada com sucesso.')


def __alterar():
    id = input('Id: ')
    nome = input('Nome: ')
    data = input('Data: ')

    con = db.conexao()
    cur = con.cursor()

    sql = 'UPDATE playlists SET nome = ?, data = ? WHERE id = ?'

    cur.execute(sql, (nome, data, id))

    con.commit()
    con.close()

    print(f'Id {id} atualizado com sucesso.')


def __excluir():
    id = input('Id: ')

    con = db.conexao()
    cur = con.cursor()

    sql = 'DELETE FROM playlists WHERE id = ?'

    cur.execute(sql, (id,))

    con.commit()
    con.close()

    print(f'Id {id} excluído com sucesso.')


def __adicionar_musica():
    musica_id = input('Música ID: ')
    playlist_id = input('Playlist ID: ')

    con = db.conexao()
    cur = con.cursor()

    sql = 'INSERT INTO musica_playlist VALUES (?, ?)'

    cur.execute(sql, (musica_id, playlist_id))

    con.commit()
    con.close()

    print(f'Música adicionada a playlist com sucesso.')


def menu():
    executar = True

    while executar:
        opcoes = ['Listar', 'Cadastrar', 'Alterar', 'Excluir', 'Adicionar Música']

        opcao = montar_menu(opcoes, nome='Playlists', voltar=True)

        if opcao == 1:
            __listar()

        if opcao == 2:
            __cadastrar()

        if opcao == 3:
            __alterar()

        if opcao == 4:
            __excluir()

        if opcao == 5:
            __adicionar_musica()

        if opcao == len(opcoes):
            executar = False
