import tkinter as tk
from tkinter import messagebox
from Clientes import clientes

def adicionar_cliente(entrys):
    dados = [e.get().strip() for e in entrys]
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return

    msg = clientes.adicionar_cliente(dados)
    messagebox.showinfo("Resultado", msg)
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

    resultado = clientes.buscar_cliente(id_busca)
    if resultado:
        mostrar_resultado_cliente(resultado)
    else:
        messagebox.showinfo("Resultado", "Cliente não encontrado.")

def alterar_cliente(entrys):
    id_cliente = entrys[0].get().strip()
    if not id_cliente:
        messagebox.showwarning("Aviso", "Informe o ID do cliente a ser alterado.")
        return

    novos_dados = [e.get().strip() for e in entrys]
    msg = clientes.alterar_cliente(id_cliente, novos_dados)
    messagebox.showinfo("Resultado", msg)

def excluir_cliente(entry_id):
    id_cliente = entry_id.get().strip()
    if not id_cliente:
        messagebox.showwarning("Aviso", "Informe o ID do cliente a ser excluído.")
        return

    msg = clientes.excluir_cliente(id_cliente)
    messagebox.showinfo("Resultado", msg)

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
