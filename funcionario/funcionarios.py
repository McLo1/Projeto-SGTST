import os

ARQUIVO = "fornecedores.txt"

# =========================
# Função para carregar os fornecedores do arquivo
# =========================
def carregar_fornecedores():
    fornecedores = []
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                try:
                    dados = linha.strip().split(", ")
                    fornecedor = {}
                    for campo in dados:
                        chave, valor = campo.split(": ", 1)
                        fornecedor[chave.lower()] = valor
                    fornecedores.append(fornecedor)
                except:
                    continue
    return fornecedores

# =========================
# Função para salvar fornecedores no arquivo
# =========================
def salvar_fornecedores(fornecedores):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for fnd in fornecedores:
            linha = (
                f"id: {fnd['id']}, nome: {fnd['nome']}, cpf: {fnd['cpf']}, cargo: {fnd['cargo']}, "
                f"dta_nascimento: {fnd['dta_nascimento']}, endereco: {fnd['endereco']}, contato: {fnd['contato']}"
            )
            f.write(linha + "\n")

# =========================
# Função para gerar o próximo ID automaticamente
# =========================
def gerar_proximo_id(fornecedores):
    if not fornecedores:
        return "1"  # Se a lista estiver vazia, começa do 1
    # Pega todos os IDs já usados e converte para inteiro
    ids = [int(f["id"]) for f in fornecedores if f["id"].isdigit()]
    return str(max(ids) + 1)

# =========================
# Inserir novo fornecedor (com ID automático)
# =========================
def inserir(fornecedores):
    print("\n-- Inserir novo fornecedor --")
    
    novo_id = gerar_proximo_id(fornecedores)  # Gera o ID automaticamente

    nome = input("Nome: ")
    cpf = input("CPF: ")
    cargo = input("Cargo: ")
    dta_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
    endereco = input("Endereço: ")
    contato = input("Contato (telefone/email): ")

    novo_fornecedor = {
        'id': novo_id,
        'nome': nome,
        'cpf': cpf,
        'cargo': cargo,
        'dta_nascimento': dta_nascimento,
        'endereco': endereco,
        'contato': contato
    }

    fornecedores.append(novo_fornecedor)
    print(f"Fornecedor inserido com sucesso! ID atribuído: {novo_id}")

# =========================
# Pesquisar fornecedor por ID
# =========================
def pesquisar(fornecedores):
    print("\n-- Pesquisar fornecedor --")
    id = input("Informe o ID do fornecedor: ")
    for fornecedor in fornecedores:
        if fornecedor['id'] == id:
            print("\nFornecedor encontrado:")
            for chave, valor in fornecedor.items():
                print(f"{chave.capitalize()}: {valor}")
            return
    print("Fornecedor não encontrado.")

# =========================
# Alterar fornecedor
# =========================
def alterar(fornecedores):
    print("\n-- Alterar fornecedor --")
    id = input("Informe o ID do fornecedor a alterar: ")
    for fornecedor in fornecedores:
        if fornecedor['id'] == id:
            print("Deixe em branco para manter o valor atual.")

            nome = input(f"Novo nome ({fornecedor['nome']}): ") or fornecedor['nome']
            cpf = input(f"Novo CPF ({fornecedor['cpf']}): ") or fornecedor['cpf']
            cargo = input(f"Novo cargo ({fornecedor['cargo']}): ") or fornecedor['cargo']
            dta_nascimento = input(f"Nova data de nascimento ({fornecedor['dta_nascimento']}): ") or fornecedor['dta_nascimento']
            endereco = input(f"Novo endereço ({fornecedor['endereco']}): ") or fornecedor['endereco']
            contato = input(f"Novo contato ({fornecedor['contato']}): ") or fornecedor['contato']

            fornecedor.update({
                'nome': nome,
                'cpf': cpf,
                'cargo': cargo,
                'dta_nascimento': dta_nascimento,
                'endereco': endereco,
                'contato': contato
            })

            print("Fornecedor atualizado com sucesso!")
            return
    print("Fornecedor não encontrado.")

# =========================
# Excluir fornecedor
# =========================
def excluir(fornecedores):
    print("\n-- Excluir fornecedor --")
    id = input("Informe o ID do fornecedor a excluir: ")
    for i, fornecedor in enumerate(fornecedores):
        if fornecedor['id'] == id:
            confirmar = input("Tem certeza que deseja excluir? (s/n): ").lower()
            if confirmar == 's':
                del fornecedores[i]
                print("Fornecedor excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
            return
    print("Fornecedor não encontrado.")

# =========================
# Listar fornecedores
# =========================
def listar(fornecedores):
    print("\n-- Lista de Fornecedores --")
    if not fornecedores:
        print("Nenhum fornecedor cadastrado.")
        return

    for f in fornecedores:
        print(", ".join([f"{k}: {v}" for k, v in f.items()]))
        print("-" * 30)

# =========================
# Menu principal
# =========================
def menu():
    fornecedores = carregar_fornecedores()

    while True:
        print("\n=== Menu CRUD de Fornecedores ===")
        print("1. Inserir fornecedor")
        print("2. Pesquisar fornecedor")
        print("3. Alterar fornecedor")
        print("4. Excluir fornecedor")
        print("5. Listar todos os fornecedores")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir(fornecedores)
            salvar_fornecedores(fornecedores)
        elif opcao == '2':
            pesquisar(fornecedores)
        elif opcao == '3':
            alterar(fornecedores)
            salvar_fornecedores(fornecedores)
        elif opcao == '4':
            excluir(fornecedores)
            salvar_fornecedores(fornecedores)
        elif opcao == '5':
            listar(fornecedores)
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
