import tkinter as tk
from tkinter import ttk, messagebox
from Clientes import clientes

# Cores e estilo
COR_FUNDO = "#f0f4f8"
COR_BOTAO = "#4a90e2"
COR_TEXTO = "#ffffff"

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
    tk.Label(janela_resultado, text=texto.strip(), justify="left", font=("Segoe UI", 11)).pack(padx=20, pady=20)

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
    janela.geometry("800x600")
    janela.configure(bg=COR_FUNDO)

    style = ttk.Style(janela)
    style.theme_use("clam")
    style.configure("Custom.TButton", font=("Segoe UI", 11), foreground=COR_TEXTO,
                    background=COR_BOTAO, padding=8)
    style.map("Custom.TButton", background=[('active', '#357ABD')])

    tk.Label(janela, text="Cadastro de Clientes", font=("Segoe UI", 18, "bold"),
             bg=COR_FUNDO, fg="#333").pack(pady=20)

    frame_form = tk.Frame(janela, bg=COR_FUNDO)
    frame_form.pack()

    labels = ["ID do cliente", "Tipo", "Nome", "CPF", "CNPJ", "Observações", "Endereço", "Contato"]
    entrys = []

    for i, texto in enumerate(labels):
        tk.Label(frame_form, text=texto + ":", bg=COR_FUNDO, anchor="w", font=("Segoe UI", 10)).grid(row=i, column=0, sticky="w", padx=10, pady=5)
        entry = tk.Entry(frame_form, width=50)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entrys.append(entry)

    frame_botoes = tk.Frame(janela, bg=COR_FUNDO)
    frame_botoes.pack(pady=20)

    def botao(texto, comando):
        ttk.Button(frame_botoes, text=texto, style="Custom.TButton", width=25, command=comando).pack(pady=5)

    botao("Adicionar", lambda: adicionar_cliente(entrys))
    botao("Alterar", lambda: alterar_cliente(entrys))
    botao("Excluir", lambda: excluir_cliente(entrys[0]))
    botao("Buscar por ID", lambda: buscar_cliente_por_id(entrys[0]))

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_clientes()
