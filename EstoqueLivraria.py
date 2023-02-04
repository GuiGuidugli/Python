estoque = []
choice = 0
codigo = 1
while choice != 4:
    choice = int(input("Selecione sua opção:\n1 - Adicionar Livro\n2 - Consultar livro\n3 - Inventário\n4 - Sair\n=> "))
    if choice == 1:
        autor = input("Insira o nome do autor: ")
        titulo = input("Insira o nome do livro: ")
        editora = input("Insira a editora: ")
        ano = int(input("Insira o ano de lançamento: "))
        quantidade = int(input("Quantidade de livros: "))
        valor = float(input("Insira o valor do livro: "))
        estoque.append({
            "registro": codigo,
            "autor": autor,
            "titulo": titulo,
            "editora": editora,
            "ano": ano,
            "quantidade": quantidade,
            "valor": valor
            })
        codigo = codigo + 1
    elif choice == 2:
        codigoDoItem = int(input("Digite o código do livro: "))
        encontrado = False
        for item in estoque:
            if item["registro"] == codigoDoItem:
                encontrado = True
                break
        if encontrado == True:
            print(item)
        else:
            print("Livro não encontrado")
    elif choice == 3:
        print(estoque)