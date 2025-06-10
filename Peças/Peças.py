import os  # Usado para verificar se o arquivo existe

# Nome do arquivo onde as peças serão salvas
ARQUIVO = "pecas.txt"

# =========================
# Função para carregar peças do arquivo
# =========================
def carregar_pecas():
    pecas = []  # Lista vazia que vai armazenar os dados
    if os.path.exists(ARQUIVO):  # Verifica se o arquivo já existe
        with open(ARQUIVO, "r", encoding="utf-8") as f:  # Abre o arquivo em modo leitura
            for linha in f:
                try:
                    dados = linha.strip().split(", ")  # Divide cada campo
                    peca = {}
                    for campo in dados:
                        chave, valor = campo.split(": ", 1)
                        peca[chave.lower()] = valor
                    peca["quantidade"] = int(peca["quantidade"])  # Converte quantidade para número
                    pecas.append(peca)
                except:
                    continue  # Se der erro, ignora a linha
    return pecas

# =========================
# Função para salvar as peças no arquivo
# =========================
def salvar_pecas(pecas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:  # Abre o arquivo para escrita
        for p in pecas:
            linha = (
                f"id: {p['id']}, descricao: {p['descricao']}, tipo: {p['tipo']}, "
                f"quantidade: {p['quantidade']}, validade: {p['validade']}, observacoes: {p['observacoes']}"
            )
            f.write(linha + "\n")

# =========================
# Função para gerar o próximo ID automaticamente
# =========================
def gerar_proximo_id(pecas):
    if not pecas:
        return "1"  # Começa do 1 se não houver peças
    ids = [int(p["id"]) for p in pecas if p["id"].isdigit()]
    return str(max(ids) + 1)  # Pega o maior ID e soma 1

# =========================
# Inserir nova peça (com ID automático)
# =========================
def inserir(pecas):
    print("\n-- Inserir nova peça --")
    
    id = gerar_proximo_id(pecas)  # Gera o ID automaticamente

    descricao = input("Descrição: ")
    tipo = input("Tipo: ")

    try:
        quantidade = int(input("Quantidade: "))
    except ValueError:
        print("Quantidade inválida.")
        return

    validade = input("Validade (AAAA-MM-DD): ")
    observacoes = input("Observações: ")

    nova_peca = {
        'id': id,
        'descricao': descricao,
        'tipo': tipo,
        'quantidade': quantidade,
        'validade': validade,
        'observacoes': observacoes
    }

    pecas.append(nova_peca)
    print(f"Peça inserida com sucesso! ID atribuído: {id}")

# =========================
# Pesquisar uma peça
# =========================
def pesquisar(pecas):
    print("\n-- Pesquisar peça --")
    id = input("Informe o ID da peça: ")
    for peca in pecas:
        if peca['id'] == id:
            print("\nPeça encontrada:")
            for chave, valor in peca.items():
                print(f"{chave.capitalize()}: {valor}")
            return
    print("Peça não encontrada.")

# =========================
# Alterar uma peça
# =========================
def alterar(pecas):
    print("\n-- Alterar peça --")
    id = input("Informe o ID da peça a alterar: ")
    for peca in pecas:
        if peca['id'] == id:
            print("Deixe em branco para manter o valor atual.")

            descricao = input(f"Nova descrição ({peca['descricao']}): ") or peca['descricao']
            tipo = input(f"Novo tipo ({peca['tipo']}): ") or peca['tipo']

            try:
                quantidade_str = input(f"Nova quantidade ({peca['quantidade']}): ")
                quantidade = int(quantidade_str) if quantidade_str else peca['quantidade']
            except ValueError:
                print("Valor inválido. Mantendo a quantidade atual.")
                quantidade = peca['quantidade']

            validade = input(f"Nova validade ({peca['validade']}): ") or peca['validade']
            observacoes = input(f"Novas observações ({peca['observacoes']}): ") or peca['observacoes']

            peca.update({
                'descricao': descricao,
                'tipo': tipo,
                'quantidade': quantidade,
                'validade': validade,
                'observacoes': observacoes
            })
            print("Peça atualizada com sucesso!")
            return
    print("Peça não encontrada.")

# =========================
# Excluir uma peça
# =========================
def excluir(pecas):
    print("\n-- Excluir peça --")
    id = input("Informe o ID da peça a excluir: ")
    for i, peca in enumerate(pecas):
        if peca['id'] == id:
            confirmar = input("Tem certeza que deseja excluir? (s/n): ").lower()
            if confirmar == 's':
                del pecas[i]
                print("Peça excluída com sucesso!")
            else:
                print("Exclusão cancelada.")
            return
    print("Peça não encontrada.")

# =========================
# Listar todas as peças
# =========================
def listar(pecas):
    print("\n-- Lista de Peças --")
    if not pecas:
        print("Nenhuma peça cadastrada.")
        return

    for peca in pecas:
        print(", ".join([f"{k}: {v}" for k, v in peca.items()]))
        print("-" * 30)

# =========================
# Menu principal
# =========================
def menu():
    pecas = carregar_pecas()

    while True:
        print("\n=== Menu CRUD de Peças ===")
        print("1. Inserir peça")
        print("2. Pesquisar peça")
        print("3. Alterar peça")
        print("4. Excluir peça")
        print("5. Listar todas as peças")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir(pecas)
            salvar_pecas(pecas)
        elif opcao == '2':
            pesquisar(pecas)
        elif opcao == '3':
            alterar(pecas)
            salvar_pecas(pecas)
        elif opcao == '4':
            excluir(pecas)
            salvar_pecas(pecas)
        elif opcao == '5':
            listar(pecas)
        elif opcao == '0':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# =========================
# Início do programa
# =========================
if __name__ == "__main__":
    menu()
