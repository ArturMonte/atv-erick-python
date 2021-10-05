import sqlite3


def conexao():
    return sqlite3.connect('database.sqlite')


def __criar_banco_contatos():
    con = conexao()
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS contatos
        (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nome        TEXT NOT NULL,
            celular     TEXT NOT NULL,
            telefone    TEXT NOT NULL,
            email       TEXT NOT NULL,
            aniversario TEXT NOT NULL
        )
    ''')

    con.commit()
    con.close()


def __criar_tabela_musicas():
    con = conexao()
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS musicas
        (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            nome    TEXT    NOT NULL,
            artista TEXT    NOT NULL,
            album   TEXT    NOT NULL,
            ano     INTEGER NOT NULL,
            arquivo TEXT    NOT NULL
        )
    ''')

    con.commit()
    con.close()


def __criar_tabela_playlists():
    con = conexao()
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS playlists
        (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data TEXT NOT NULL
        )
    ''')

    con.commit()
    con.close()


def __criar_tabela_musica_playlist():
    con = conexao()
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS musica_playlist
        (
            musica_id   INTEGER NOT NULL REFERENCES musicas (id),
            playlist_id INTEGER NOT NULL REFERENCES playlists (id),
            PRIMARY KEY (musica_id, playlist_id)
        )
    ''')

    con.commit()
    con.close()


def __criar_tabela_vendas():
    con = conexao()
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS vendas
        (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo       TEXT NOT NULL,
            quantidade   TEXT NOT NULL,
            preco_compra REAL NOT NULL,
            preco_venda  REAL NOT NULL
        )
    ''')

    con.commit()
    con.close()


def iniciar():
    __criar_banco_contatos()
    __criar_tabela_musicas()
    __criar_tabela_playlists()
    __criar_tabela_musica_playlist()
    __criar_tabela_vendas()
