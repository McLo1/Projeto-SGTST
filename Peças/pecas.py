"""
Nome do arquivo: pecas.py
Equipe: Marcelo, Layza, Vanderson, Caique.
Turma: G91166
Semestre: 2025.1
"""

def adicionar_peca(dados):
    with open("peças.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(", ".join(dados) + "\n")
    return "Peça adicionada com sucesso!"

def buscar_peca(id_peca):
    with open("peças.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",")
            if item[0] == id_peca:
                return item
    return None

def alterar_peca(id_peca, novos_dados):
    with open("peças.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("peças.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == id_peca:
                arquivo.write(", ".join(novos_dados) + "\n")
            else:
                arquivo.write(linha)
    return "Peça alterada com sucesso!"

def excluir_peca(id_peca):
    with open("peças.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("peças.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != id_peca:
                arquivo.write(linha)
    return "Peça removida com sucesso!"
