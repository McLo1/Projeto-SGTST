def adicionar_funcionario():
    id_funcionario = input("ID do funcionário: ")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cargo = input("Cargo: ")
    dta_nascimento = input("Data de nascimento: ")
    endereco = input("Endereço: ")
    contato = input("Contato: ")

    with open("funcionarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{id_funcionario}, {nome}, {cpf}, {cargo}, {dta_nascimento}, {endereco}, {contato}\n")
    print("Funcionário adicionado com sucesso!")

def listar_funcionarios():
    with open("funcionarios.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",")
            print(f"ID: {item[0]}, Nome: {item[1]}, CPF: {item[2]}, Cargo: {item[3]}, Data de Nascimento: {item[4]}, Endereço: {item[5]}, Contato: {item[6]}")

def alterar_funcionario():
    id_funcionario = input("ID do funcionário: ")
    with open("funcionarios.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("funcionarios.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == id_funcionario:
                print("Digite os novos dados: ")
                novo_id = input("ID: ")
                novo_nome = input("Nome: ")
                novo_cpf = input("CPF: ")
                novo_cargo = input("Cargo: ")
                nova_data = input("Data de nascimento: ")
                novo_endereco = input("Endereço: ")
                novo_contato = input("Contato: ")
                arquivo.write(f"{novo_id}, {novo_nome}, {novo_cpf}, {novo_cargo}, {nova_data}, {novo_endereco}, {novo_contato}\n")
            else:
                arquivo.write(linha)
    print("Funcionário alterado com sucesso!")

def excluir_funcionario():
    id_funcionario = input("ID do funcionário: ")
    with open("funcionarios.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    with open("funcionarios.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != id_funcionario:
                arquivo.write(linha)
    print("Funcionário removido com sucesso!")
