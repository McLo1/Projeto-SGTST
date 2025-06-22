def adicionar_caminhao():
    id_caminhao = input("ID do caminhão: ")
    renavan = input("Renavan: ")
    modelo = input("Modelo: ")
    marca = input("Marca: ")
    cor = input("Cor: ")
    placa = input("Placa: ")
    chassi = input("Chassi: ")
    status = input("Status: ")
    tipo = input("Tipo: ")
    peso = input("Peso: ")

    with open("caminhoes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{id_caminhao}, {renavan}, {modelo}, {marca}, {cor}, {placa}, {chassi}, {status}, {tipo}, {peso}\n")
    print("Caminhão adicionado com sucesso!")

def listar_caminhoes():
    with open("caminhoes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",")
            print(f"ID: {item[0]}, Renavan: {item[1]}, Modelo: {item[2]}, Marca: {item[3]}, Cor: {item[4]}, Placa: {item[5]}, Chassi: {item[6]}, Status: {item[7]}, Tipo: {item[8]}, Peso: {item[9]}")

def alterar_caminhao():
    id_caminhao = input("ID do caminhão: ")
    with open("caminhoes.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("caminhoes.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == id_caminhao:
                print("Digite os novos dados: ")
                novo_id = input("ID: ")
                novo_renavan = input("Renavan: ")
                novo_modelo = input("Modelo: ")
                nova_marca = input("Marca: ")
                nova_cor = input("Cor: ")
                nova_placa = input("Placa: ")
                novo_chassi = input("Chassi: ")
                novo_status = input("Status: ")
                novo_tipo = input("Tipo: ")
                novo_peso = input("Peso: ")
                arquivo.write(f"{novo_id}, {novo_renavan}, {novo_modelo}, {nova_marca}, {nova_cor}, {nova_placa}, {novo_chassi}, {novo_status}, {novo_tipo}, {novo_peso}\n")
            else:
                arquivo.write(linha)
    print("Caminhão alterado com sucesso!")

def excluir_caminhao():
    id_caminhao = input("ID do caminhão: ")
    with open("caminhoes.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    with open("caminhoes.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != id_caminhao:
                arquivo.write(linha)
    print("Caminhão removido com sucesso!")
