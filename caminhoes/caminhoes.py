import os  # Usado para verificar se o arquivo existe

# Nome do arquivo onde os caminhões serão salvos
ARQUIVO = "caminhoes.txt"

# =========================
# Função para carregar caminhões do arquivo
# =========================
def carregar_caminhoes():
    caminhoes = []  # Lista para armazenar os caminhões
    if os.path.exists(ARQUIVO):  # Verifica se o arquivo já existe
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                try:
                    dados = linha.strip().split(", ")  # Divide a linha nos campos
                    caminhao = {}
                    for campo in dados:
                        chave, valor = campo.split(": ", 1)
                        caminhao[chave.lower()] = valor
                    caminhoes.append(caminhao)
                except:
                    continue  # Pula linha se tiver erro
    return caminhoes

# =========================
# Função para salvar os caminhões no arquivo
# =========================
def salvar_caminhoes(caminhoes):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for c in caminhoes:
            linha = (
                f"renavan: {c['renavan']}, modelo: {c['modelo']}, marca: {c['marca']}, cor: {c['cor']}, "
                f"placa: {c['placa']}, chassi: {c['chassi']}, status: {c['status']}, tipo: {c['tipo']}, peso: {c['peso']}"
            )
            f.write(linha + "\n")

# =========================
# Inserir novo caminhão
# =========================
def inserir(caminhoes):
    print("\n-- Inserir novo caminhão --")
    renavan = input("Renavan (identificador): ")

    # Verifica se o Renavan já existe
    if any(c['renavan'] == renavan for c in caminhoes):
        print("Já existe um caminhão com esse Renavan.")
        return

    modelo = input("Modelo: ")
    marca = input("Marca: ")
    cor = input("Cor: ")
    placa = input("Placa: ")
    chassi = input("Chassi: ")
    status = input("Status (ativo/inativo/manutenção): ")
    tipo = input("Tipo (baú, prancha, etc.): ")
    peso = input("Peso (em kg): ")

    novo_caminhao = {
        'renavan': renavan,
        'modelo': modelo,
        'marca': marca,
        'cor': cor,
        'placa': placa,
        'chassi': chassi,
        'status': status,
        'tipo': tipo,
        'peso': peso
    }

    caminhoes.append(novo_caminhao)
    print("Caminhão inserido com sucesso!")

# =========================
# Pesquisar caminhão
# =========================
def pesquisar(caminhoes):
    print("\n-- Pesquisar caminhão --")
    renavan = input("Informe o Renavan do caminhão: ")
    for caminhao in caminhoes:
        if caminhao['renavan'] == renavan:
            print("\nCaminhão encontrado:")
            for chave, valor in caminhao.items():
                print(f"{chave.capitalize()}: {valor}")
            return
    print("Caminhão não encontrado.")

# =========================
# Alterar caminhão
# =========================
def alterar(caminhoes):
    print("\n-- Alterar caminhão --")
    renavan = input("Informe o Renavan do caminhão: ")
    for caminhao in caminhoes:
        if caminhao['renavan'] == renavan:
            print("Deixe em branco para manter o valor atual.")

            modelo = input(f"Novo modelo ({caminhao['modelo']}): ") or caminhao['modelo']
            marca = input(f"Nova marca ({caminhao['marca']}): ") or caminhao['marca']
            cor = input(f"Nova cor ({caminhao['cor']}): ") or caminhao['cor']
            placa = input(f"Nova placa ({caminhao['placa']}): ") or caminhao['placa']
            chassi = input(f"Novo chassi ({caminhao['chassi']}): ") or caminhao['chassi']
            status = input(f"Novo status ({caminhao['status']}): ") or caminhao['status']
            tipo = input(f"Novo tipo ({caminhao['tipo']}): ") or caminhao['tipo']
            peso = input(f"Novo peso ({caminhao['peso']}): ") or caminhao['peso']

            caminhao.update({
                'modelo': modelo,
                'marca': marca,
                'cor': cor,
                'placa': placa,
                'chassi': chassi,
                'status': status,
                'tipo': tipo,
                'peso': peso
            })

            print("Caminhão atualizado com sucesso!")
            return
    print("Caminhão não encontrado.")

# =========================
# Excluir caminhão
# =========================
def excluir(caminhoes):
    print("\n-- Excluir caminhão --")
    renavan = input("Informe o Renavan do caminhão a excluir: ")
    for i, caminhao in enumerate(caminhoes):
        if caminhao['renavan'] == renavan:
            confirmar = input("Tem certeza que deseja excluir? (s/n): ").lower()
            if confirmar == 's':
                del caminhoes[i]
                print("Caminhão excluído com sucesso!")
            else:
                print("Exclusão cancelada.")
            return
    print("Caminhão não encontrado.")

# =========================
# Listar todos os caminhões
# =========================
def listar(caminhoes):
    print("\n-- Lista de Caminhões --")
    if not caminhoes:
        print("Nenhum caminhão cadastrado.")
        return

    for caminhao in caminhoes:
        print(", ".join([f"{k}: {v}" for k, v in caminhao.items()]))
        print("-" * 30)

# =========================
# Menu principal
# =========================
def menu():
    caminhoes = carregar_caminhoes()  # Carrega os caminhões do arquivo

    while True:
        print("\n=== Menu CRUD de Caminhões ===")
        print("1. Inserir caminhão")
        print("2. Pesquisar caminhão")
        print("3. Alterar caminhão")
        print("4. Excluir caminhão")
        print("5. Listar todos os caminhões")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir(caminhoes)
            salvar_caminhoes(caminhoes)
        elif opcao == '2':
            pesquisar(caminhoes)
        elif opcao == '3':
            alterar(caminhoes)
            salvar_caminhoes(caminhoes)
        elif opcao == '4':
            excluir(caminhoes)
            salvar_caminhoes(caminhoes)
        elif opcao == '5':
            listar(caminhoes)
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
