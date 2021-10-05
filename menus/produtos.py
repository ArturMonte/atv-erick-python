import db
import csv
from ajudantes import montar_menu


def __importar():
    produtos_importados = []
    with open('produtos.csv', 'r', newline='\n') as csv_produtos:
        produtos = csv.reader(csv_produtos, delimiter=';')
        next(produtos)
        for produto in produtos:
            produtos_importados.append(produto)

    con = db.conexao()
    cur = con.cursor()

    sql = 'INSERT INTO vendas (codigo, quantidade, preco_compra, preco_venda) VALUES (?, ?, ?, ?)'

    for produto in produtos_importados:
        cur.execute(sql, (produto[0], produto[1], produto[2], produto[3]))

    con.commit()
    con.close()

    print(f'Um total de {len(produtos_importados)} foram importados')


def menu():
    executar = True

    while executar:
        opcoes = ['Importar', 'Listar Produtos']

        opcao = montar_menu(opcoes, nome='Produtos', voltar=True)

        if opcao == 1:
            __importar()

        if opcao == len(opcoes):
            executar = False
