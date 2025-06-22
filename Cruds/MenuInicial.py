#SISTEMA DE ESTOQUE
#Menu principal
import pecas as pecas
import fornecedores as fornecedores
import caminhao as caminhao
import funcionarios as funcionarios
import clientes as clientes


def menuInicial():
    while True:
        print("\n ---- MENU INICIAL ---- ")
        print("1 - MENU PEÇAS: ")
        print("2 - MENU FORNECEDORES: ")
        print("3 - MENU CAMINHAO: ")
        print("4 - MENU FUNCIONARIOS: ")
        print("5 - MENU CLIENTES: ")
        print("0 - Sair do Sistema")

        opcao = input ("Digite uma opção: ")
        if opcao == "1":
            menuPecas()
        elif (opcao == "2"):
            menuFornecedor()
        elif (opcao == "3"):
            menuCaminhao()
        elif (opcao == "4"):
            menuFuncionarios()
        elif (opcao == "5"):
            menuClientes()
        elif (opcao == "0"):
            break
        else:
            print ("Opção Inválida. ")




#------------------MENU PEÇAS--------------------------



def menuPecas():
    while True:
        print("\n ---- MENU PEÇAS ---- ")
        print("1 - Adicionar item: ")
        print("2 - Listar estoque: ")
        print("3 - Alterar item: ")
        print("4 - Excluir item: ")
        print("0 - Voltar")

        opcao = input ("Digite uma opção: ")
        if opcao == "1":
            pecas.adicionar_pecas()
        elif (opcao == "2"):
            pecas.listar_pecas()
        elif (opcao == "3"):
            pecas.alterar_pecas()
        elif (opcao == "4"):
            pecas.excluir_pecas()
        elif (opcao == "0"):
            break
        else:
            print ("Opção Inválida. ")



#------------------MENU FORNECEDORES--------------------------



def menuFornecedor():
    while True:
        print("\n ---- MENU FORNECEDORES ---- ")
        print("1 - Adicionar Fornecedor: ")
        print("2 - Listar Fornecedores: ")
        print("3 - Alterar Fornecedor: ")
        print("4 - Excluir Fornecedor: ")
        print("0 - Voltar")

        opcao = input ("Digite uma opção: ")
        if opcao == "1":
            fornecedores.adicionar_fornecedor()
        elif (opcao == "2"):
            fornecedores.listar_fornecedores()
        elif (opcao == "3"):
            fornecedores.alterar_fornecedor()
        elif (opcao == "4"):
            fornecedores.excluir_fornecedor()
        elif (opcao == "0"):
            break
        else:
            print ("Opção Inválida. ")




#------------------MENU CAMINHAO--------------------------


def menuCaminhao():
    while True:
        print("\n ---- MENU CAMINHÕES ---- ")
        print("1 - Adicionar Caminhão: ")
        print("2 - Listar Caminhões: ")
        print("3 - Alterar Caminhão: ")
        print("4 - Excluir Caminhão: ")
        print("0 - Voltar")

        opcao = input ("Digite uma opção: ")
        if opcao == "1":
            caminhao.adicionar_caminhao()
        elif (opcao == "2"):
            caminhao.listar_caminhoes()
        elif (opcao == "3"):
            caminhao.alterar_caminhao()
        elif (opcao == "4"):
            caminhao.excluir_caminhao()
        elif (opcao == "0"):
            break
        else:
            print ("Opção Inválida. ")





#------------------MENU FUNCIONARIO--------------------------




def menuFuncionarios():
    while True:
        print("\n ---- MENU FUNCIONARIO ---- ")
        print("1 - Adicionar Funcionario: ")
        print("2 - Listar Funcionarios: ")
        print("3 - Alterar Funcionario: ")
        print("4 - Excluir Funcionario: ")
        print("0 - Voltar")

        opcao = input ("Digite uma opção: ")
        if opcao == "1":
            funcionarios.adicionar_funcionario()
        elif (opcao == "2"):
            funcionarios.listar_funcionarios()
        elif (opcao == "3"):
            funcionarios.alterar_funcionario()
        elif (opcao == "4"):
            funcionarios.excluir_funcionario()
        elif (opcao == "0"):
            break
        else:
            print ("Opção Inválida. ")




#------------------MENU CLIENTES--------------------------


def menuClientes():
    while True:
        print("\n ---- MENU CLIENTES ---- ")
        print("1 - Adicionar Cliente: ")
        print("2 - Listar Clientes: ")
        print("3 - Alterar Cliente: ")
        print("4 - Excluir Cliente: ")
        print("0 - Voltar")

        opcao = input ("Digite uma opção: ")
        if opcao == "1":
            clientes.adicionar_cliente()
        elif (opcao == "2"):
            clientes.listar_clientes()
        elif (opcao == "3"):
            clientes.alterar_cliente()
        elif (opcao == "4"):
            clientes.excluir_cliente()
        elif (opcao == "0"):
            break
        else:
            print ("Opção Inválida. ")



menuInicial()