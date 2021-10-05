import db
from ajudantes import montar_menu


def __listar_contatos():
    con = db.conexao()
    cur = con.cursor()

    sql = 'SELECT * FROM contatos'

    cur.execute(sql)

    contatos = cur.fetchall()

    print(f'\nContatos [Total:{len(contatos)}]')

    for contato in contatos:
        print(f'\nID: {contato[0]}')
        print(f'NOME: {contato[1]}')
        print(f'CELULAR: {contato[2]}')
        print(f'TELEFONE: {contato[3]}')
        print(f'EMAIL: {contato[4]}')
        print(f'ANIVERSÁRIO: {contato[5]}')

    con.close()


def __cadastrar_contato():
    nome = input('Nome: ')
    celular = input('Celular: ')
    telefone = input('Telefone: ')
    email = input('Email: ')
    aniversario = input('Aniversário: ')

    con = db.conexao()
    cur = con.cursor()

    sql = 'INSERT INTO contatos(nome, celular, telefone, email, aniversario) VALUES (?, ?, ?, ?, ?)'

    cur.execute(sql, (nome, celular, telefone, email, aniversario))

    con.commit()
    con.close()

    print(f'{nome} cadastrado com sucesso.')


def __alterar_contato():
    id = input('Id: ')
    celular = input('Celular: ')
    telefone = input('Telefone: ')
    email = input('Email: ')

    con = db.conexao()
    cur = con.cursor()

    sql = 'UPDATE contatos SET celular = ?, telefone = ?, email = ? WHERE id = ?'

    cur.execute(sql, (celular, telefone, email, id))

    con.commit()
    con.close()

    print(f'Id {id} atualizado com sucesso.')


def __excluir_contato():
    id = input('Id: ')

    con = db.conexao()
    cur = con.cursor()

    sql = 'DELETE FROM contatos WHERE id = ?'

    cur.execute(sql, (id,))

    con.commit()
    con.close()

    print(f'Id {id} excluído com sucesso.')


def menu():
    executar = True

    while executar:
        opcoes = ['Listar', 'Cadastrar', 'Alterar', 'Excluir']

        opcao = montar_menu(opcoes, nome='Contatos', voltar=True)

        if opcao == 1:
            __listar_contatos()

        if opcao == 2:
            __cadastrar_contato()

        if opcao == 3:
            __alterar_contato()

        if opcao == 4:
            __excluir_contato()

        if opcao == len(opcoes):
            executar = False
