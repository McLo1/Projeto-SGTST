def adicionar_fornecedor():
    id_fornecedor = input("ID do fornecedor: ")
    cnpj = input("CNPJ: ")
    razao_social = input("Razão Social: ")
    nome_fantasia = input("Nome Fantasia: ")
    area_atuacao = input("Área de Atuação: ")
    endereco = input("Endereço: ")
    contato = input("Contato: ")
    produtos = input("Produtos: ")

    with open("fornecedores.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{id_fornecedor}, {cnpj}, {razao_social}, {nome_fantasia}, {area_atuacao}, {endereco}, {contato}, {produtos}\n")
    print("Fornecedor adicionado com sucesso!")

def listar_fornecedores():
    with open("fornecedores.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",")
            print(f"ID: {item[0]}, CNPJ: {item[1]}, Razão Social: {item[2]}, Nome Fantasia: {item[3]}, Área de Atuação: {item[4]}, Endereço: {item[5]}, Contato: {item[6]}, Produtos: {item[7]}")

def alterar_fornecedor():
    id_fornecedor = input("ID do fornecedor: ")
    with open("fornecedores.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("fornecedores.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == id_fornecedor:
                print("Digite os novos dados: ")
                novo_id = input("ID: ")
                novo_cnpj = input("CNPJ: ")
                nova_razao = input("Razão Social: ")
                novo_nome = input("Nome Fantasia: ")
                nova_area = input("Área de Atuação: ")
                novo_endereco = input("Endereço: ")
                novo_contato = input("Contato: ")
                novos_produtos = input("Produtos: ")
                arquivo.write(f"{novo_id}, {novo_cnpj}, {nova_razao}, {novo_nome}, {nova_area}, {novo_endereco}, {novo_contato}, {novos_produtos}\n")
            else:
                arquivo.write(linha)
    print("Fornecedor alterado com sucesso!")

def excluir_fornecedor():
    id_fornecedor = input("ID do fornecedor: ")
    with open("fornecedores.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    with open("fornecedores.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != id_fornecedor:
                arquivo.write(linha)
    print("Fornecedor removido com sucesso!")
