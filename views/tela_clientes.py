import tkinter as tk
from tkinter import messagebox

def adicionar_cliente(entrys):
    dados = [e.get().strip() for e in entrys]
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return

    with open("clientes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{', '.join(dados)}\n")
    messagebox.showinfo("Sucesso", "Cliente adicionado com sucesso!")
    for e in entrys:
        e.delete(0, tk.END)

def mostrar_resultado_cliente(cliente):
    janela_resultado = tk.Toplevel()
    janela_resultado.title("Resultado da Busca - Cliente")
    janela_resultado.geometry("600x250")

    texto = f"""
ID: {cliente[0]}
Tipo: {cliente[1]}
Nome: {cliente[2]}
CPF: {cliente[3]}
CNPJ: {cliente[4]}
Observações: {cliente[5]}
Endereço: {cliente[6]}
Contato: {cliente[7]}
    """
    tk.Label(janela_resultado, text=texto.strip(), justify="left", font=("Arial", 11)).pack(padx=20, pady=20)

def buscar_cliente_por_id(entry_id):
    id_busca = entry_id.get().strip()
    if not id_busca:
        messagebox.showwarning("Aviso", "Informe o ID do cliente para buscar.")
        return

    try:
        with open("clientes.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                item = linha.strip().split(",")
                if item[0] == id_busca:
                    mostrar_resultado_cliente(item)
                    return
        messagebox.showinfo("Resultado", "Cliente não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de clientes não encontrado.")

def alterar_cliente(entrys):
    id_alvo = entrys[0].get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID do cliente a ser alterado.")
        return

    novos_dados = [e.get().strip() for e in entrys]
    atualizado = False

    try:
        with open("clientes.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        with open("clientes.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas:
                item = linha.strip().split(",")
                if item[0] == id_alvo:
                    arquivo.write(", ".join(novos_dados) + "\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
        if atualizado:
            messagebox.showinfo("Sucesso", "Cliente alterado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "ID não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de clientes não encontrado.")

def excluir_cliente(entry_id):
    id_alvo = entry_id.get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID do cliente a ser excluído.")
        return

    excluido = False
    try:
        with open("clientes.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        with open("clientes.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas:
                item = linha.strip().split(",")
                if item[0] != id_alvo:
                    arquivo.write(linha)
                else:
                    excluido = True
        if excluido:
            messagebox.showinfo("Sucesso", "Cliente removido com sucesso!")
        else:
            messagebox.showwarning("Aviso", "ID não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de clientes não encontrado.")

def abrir_tela_clientes():
    janela = tk.Tk()
    janela.title("Cadastro de Clientes")
    janela.geometry("850x500")

    labels = ["ID do cliente", "Tipo", "Nome", "CPF", "CNPJ", "Observações", "Endereço", "Contato"]
    entrys = []

    for i, texto in enumerate(labels):
        tk.Label(janela, text=texto).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(janela, width=60)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entrys.append(entry)

    # Botões principais
    tk.Button(janela, text="Adicionar", command=lambda: adicionar_cliente(entrys)).grid(row=len(labels), column=0, pady=10)
    tk.Button(janela, text="Alterar", command=lambda: alterar_cliente(entrys)).grid(row=len(labels), column=1, pady=10)
    tk.Button(janela, text="Excluir", command=lambda: excluir_cliente(entrys[0])).grid(row=len(labels), column=2, pady=10)
    tk.Button(janela, text="Buscar por ID", command=lambda: buscar_cliente_por_id(entrys[0])).grid(row=len(labels)+1, column=1, pady=10)

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_clientes()
