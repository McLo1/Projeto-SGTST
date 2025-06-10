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
                    # Cada linha é dividida usando vírgula e espaço
                    dados = linha.strip().split(", ")
                    peca = {}  # Dicionário para armazenar os campos de uma peça
                    for campo in dados:
                        chave, valor = campo.split(": ", 1)  # Separa campo e valor
                        peca[chave.lower()] = valor  # Armazena no dicionário
                    peca["quantidade"] = int(peca["quantidade"])  # Converte quantidade para número
                    pecas.append(peca)  # Adiciona a peça à lista
                except:
                    continue  # Se der erro, pula a linha
    return pecas  # Retorna a lista de peças

# =========================
# Função para salvar as peças no arquivo
# =========================
def salvar_pecas(pecas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:  # Abre o arquivo para escrita
        for p in pecas:
            # Cria uma linha formatada com os campos
            linha = (
                f"id: {p['id']}, descricao: {p['descricao']}, tipo: {p['tipo']}, "
                f"quantidade: {p['quantidade']}, validade: {p['validade']}, observacoes: {p['observacoes']}"
            )
            f.write(linha + "\n")  # Escreve a linha no arquivo

# =========================
# Função para inserir nova peça
# =========================
def inserir(pecas):
    print("\n-- Inserir nova peça --")
    id = input("ID: ")
    
    # Verifica se o ID já existe
    if any(p['id'] == id for p in pecas):
        print("Já existe uma peça com esse ID.")
        return

    descricao = input("Descrição: ")
    tipo = input("Tipo: ")

    try:
        quantidade = int(input("Quantidade: "))  # Converte para número inteiro
    except ValueError:
        print("Quantidade inválida.")
        return

    validade = input("Validade (AAAA-MM-DD): ")
    observacoes = input("Observações: ")

    # Cria o dicionário da nova peça
    nova_peca = {
        'id': id,
        'descricao': descricao,
        'tipo': tipo,
        'quantidade': quantidade,
        'validade': validade,
        'observacoes': observacoes
    }

    pecas.append(nova_peca)  # Adiciona na lista
    print("Peça inserida com sucesso!")

# =========================
# Função para pesquisar uma peça pelo ID
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
# Função para alterar uma peça
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

            # Atualiza os valores
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
# Função para excluir uma peça
# =========================
def excluir(pecas):
    print("\n-- Excluir peça --")
    id = input("Informe o ID da peça a excluir: ")
    for i, peca in enumerate(pecas):
        if peca['id'] == id:
            confirmar = input("Tem certeza que deseja excluir? (s/n): ").lower()
            if confirmar == 's':
                del pecas[i]  # Remove a peça da lista
                print("Peça excluída com sucesso!")
            else:
                print("Exclusão cancelada.")
            return
    print("Peça não encontrada.")

# =========================
# Função para listar todas as peças
# =========================
def listar(pecas):
    print("\n-- Lista de Peças --")
    if not pecas:
        print("Nenhuma peça cadastrada.")
        return

    for peca in pecas:
        # Imprime os dados da peça de forma legível
        print(", ".join([f"{k}: {v}" for k, v in peca.items()]))
        print("-" * 30)

# =========================
# Função principal (menu)
# =========================
def menu():
    pecas = carregar_pecas()  # Carrega as peças do arquivo no início

    while True:
        # Exibe o menu principal
        print("\n=== Menu CRUD de Peças ===")
        print("1. Inserir peça")
        print("2. Pesquisar peça")
        print("3. Alterar peça")
        print("4. Excluir peça")
        print("5. Listar todas as peças")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        # Executa a função correspondente
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
# Inicia o programa
# =========================
if __name__ == "__main__":
    menu()
