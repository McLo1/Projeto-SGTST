"""
Nome do arquivo: clientes.py
Equipe: Marcelo, Layza, Vanderson, Caique.
Turma: G91166
Semestre: 2025.1
"""

def adicionar_cliente(dados):
    with open("clientes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(", ".join(dados) + "\n")
    return "Cliente adicionado com sucesso!"

def buscar_cliente(id_cliente):
    with open("clientes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",")
            if item[0] == id_cliente:
                return item
    return None

def alterar_cliente(id_cliente, novos_dados):
    with open("clientes.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("clientes.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == id_cliente:
                arquivo.write(", ".join(novos_dados) + "\n")
            else:
                arquivo.write(linha)
    return "Cliente alterado com sucesso!"

def excluir_cliente(id_cliente):
    with open("clientes.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
    with open("clientes.txt", "w", encoding="utf-8") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != id_cliente:
                arquivo.write(linha)
    return "Cliente removido com sucesso!"
