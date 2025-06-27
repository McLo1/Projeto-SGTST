"""
Nome do arquivo: funcionarios.py
Equipe: Marcelo, Layza, Vanderson, Caique.
Turma: G91166
Semestre: 2025.1
"""

def adicionar_funcionario(dados):
    with open("funcionarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(", ".join(dados) + "\n")
    return "Funcionário adicionado com sucesso!"

def buscar_funcionario(id_funcionario):
    with open("funcionarios.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",")
            if item[0] == id_funcionario:
                return item
    return None

def alterar_funcionario(id_funcionario, novos_dados):
    with open("funcionarios.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("funcionarios.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == id_funcionario:
                arquivo.write(", ".join(novos_dados) + "\n")
            else:
                arquivo.write(linha)
    return "Funcionário alterado com sucesso!"

def excluir_funcionario(id_funcionario):
    with open("funcionarios.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("funcionarios.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != id_funcionario:
                arquivo.write(linha)
    return "Funcionário removido com sucesso!"
