def adicionar_caminhao(dados):
    with open("caminhoes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(", ".join(dados) + "\n")
    return "Caminhão adicionado!"

def buscar_caminhao(id_caminhao):
    with open("caminhoes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(", ")
            if item[0] == id_caminhao:
                return item
    return None

def alterar_caminhao(id_caminhao, novos_dados):
    with open("caminhoes.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("caminhoes.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(", ")
            if item[0] == id_caminhao:
                arquivo.write(", ".join(novos_dados) + "\n")
            else:
                arquivo.write(linha)
    return "Caminhão alterado!"

def excluir_caminhao(id_caminhao):
    with open("caminhoes.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("caminhoes.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(", ")
            if item[0] != id_caminhao:
                arquivo.write(linha)
    return "Caminhão removido!"
