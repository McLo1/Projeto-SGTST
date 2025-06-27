"""
Nome do arquivo: Registro_saida.py
Equipe: Marcelo, Layza, Vanderson, Caique.
Turma: G91166
Semestre: 2025.1
"""

def adicionar_saida(dados):
    with open("registros_saida.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(", ".join(dados) + "\n")
    return "Saída registrada com sucesso!"

def buscar_saida(id_caminhao):
    with open("registros_saida.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",")
            if item[0] == id_caminhao:
                return item
    return None

def alterar_saida(id_caminhao, novos_dados):
    with open("registros_saida.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("registros_saida.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == id_caminhao:
                arquivo.write(", ".join(novos_dados) + "\n")
            else:
                arquivo.write(linha)
    return "Saída alterada com sucesso!"

def excluir_saida(id_caminhao):
    with open("registros_saida.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("registros_saida.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != id_caminhao:
                arquivo.write(linha)
    return "Saída removida com sucesso!"
