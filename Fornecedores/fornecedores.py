def adicionar_fornecedor(dados):
    with open("fornecedores.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(", ".join(dados) + "\n")
    return "Fornecedor adicionado com sucesso!"

def buscar_fornecedor(id_fornecedor):
    with open("fornecedores.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",")
            if item[0] == id_fornecedor:
                return item
    return None

def alterar_fornecedor(id_fornecedor, novos_dados):
    with open("fornecedores.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("fornecedores.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == id_fornecedor:
                arquivo.write(", ".join(novos_dados) + "\n")
            else:
                arquivo.write(linha)
    return "Fornecedor alterado com sucesso!"

def excluir_fornecedor(id_fornecedor):
    with open("fornecedores.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("fornecedores.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != id_fornecedor:
                arquivo.write(linha)
    return "Fornecedor removido com sucesso!"
