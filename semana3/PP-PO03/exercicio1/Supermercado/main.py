def inserir_produto(produtos):
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ").capitalize()
    preco = float(input("Digite o preço do produto: "))
    
    produto = {"codigo": codigo, "nome": nome, "preco": preco}
    produtos.append(produto)
    print("Produto inserido com sucesso!\n")

def excluir_produto(produtos):
    codigo = input("Digite o código do produto a ser excluído: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso!\n")
            return
    print("Produto não encontrado!\n")

def main():
     while True:
        print("Menu de Opções:")
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")


if __name__ == "__main__":
    main()


