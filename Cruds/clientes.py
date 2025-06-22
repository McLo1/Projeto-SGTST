def adicionar_cliente():
    id_cliente = input("ID do cliente: ")
    tipo = input("Tipo: ")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cnpj = input("CNPJ: ")
    observacoes = input("Observações: ")
    endereco = input("Endereço: ")
    contato = input("Contato: ")

    with open("clientes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{id_cliente}, {tipo}, {nome}, {cpf}, {cnpj}, {observacoes}, {endereco}, {contato}\n")
    print("Cliente adicionado com sucesso!")

def listar_clientes():
    with open("clientes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",")
            print(f"ID: {item[0]}, Tipo: {item[1]}, Nome: {item[2]}, CPF: {item[3]}, CNPJ: {item[4]}, Observações: {item[5]}, Endereço: {item[6]}, Contato: {item[7]}")

def alterar_cliente():
    id_cliente = input("ID do cliente: ")
    with open("clientes.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("clientes.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == id_cliente:
                print("Digite os novos dados: ")
                novo_id = input("ID: ")
                novo_tipo = input("Tipo: ")
                novo_nome = input("Nome: ")
                novo_cpf = input("CPF: ")
                novo_cnpj = input("CNPJ: ")
                novas_observacoes = input("Observações: ")
                novo_endereco = input("Endereço: ")
                novo_contato = input("Contato: ")
                arquivo.write(f"{novo_id}, {novo_tipo}, {novo_nome}, {novo_cpf}, {novo_cnpj}, {novas_observacoes}, {novo_endereco}, {novo_contato}\n")
            else:
                arquivo.write(linha)
    print("Cliente alterado com sucesso!")

def excluir_cliente():
    id_cliente = input("ID do cliente: ")
    with open("clientes.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    with open("clientes.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != id_cliente:
                arquivo.write(linha)
    print("Cliente removido com sucesso!")
