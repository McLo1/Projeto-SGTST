def adicionar_pecas():
    id_produtos = input("ID do produto: ")
    descricao = input("Descrição: ")
    tipo = input("Tipo: ")
    quantidade = input("Quantidade: ")
    validade = input("Validade: ")
    observacoes = input("Observações: ")

    with open("peças.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{id_produtos}, {descricao}, {tipo}, {quantidade}, {validade}, {observacoes}\n")
    print("Item adicionado com sucesso!")

def listar_pecas():
    with open("peças.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",")
            print(f"ID: {item[0]}, Descrição: {item[1]}, Tipo: {item[2]}, Quantidade: {item[3]}, Validade: {item[4]}, Observações: {item[5]}")

def alterar_pecas():
    id_produtos = input("ID do produto: ")
    with open("peças.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("peças.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == id_produtos:
                print("Digite os novos dados: ")
                novo_id = input("ID: ")
                nova_descricao = input("Descrição: ")
                novo_tipo = input("Tipo: ")
                nova_quantidade = input("Quantidade: ")
                nova_validade = input("Validade: ")
                novas_observacoes = input("Observações: ")
                arquivo.write(f"{novo_id}, {nova_descricao}, {novo_tipo}, {nova_quantidade}, {nova_validade}, {novas_observacoes}\n")
            else:
                arquivo.write(linha)
    print("Item alterado com sucesso!")

def excluir_pecas():
    id_produtos = input("ID do produto: ")
    with open("peças.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    with open("peças.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != id_produtos:
                arquivo.write(linha)
    print("Item removido com sucesso!")
