import tkinter as tk
from tkinter import messagebox
from Peças import pecas

def get_dados(entrys):
    return [e.get().strip() for e in entrys]

def limpar(entrys):
    for e in entrys:
        e.delete(0, tk.END)

def adicionar(entrys):
    dados = get_dados(entrys)
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return
    msg = pecas.adicionar_peca(dados)
    messagebox.showinfo("Sucesso", msg)
    limpar(entrys)

def buscar(entrys):
    id_peca = entrys[0].get().strip()
    if not id_peca:
        messagebox.showwarning("Aviso", "Informe o ID da peça para buscar.")
        return
    peca = pecas.buscar_peca(id_peca)
    if peca:
        mostrar_resultado(peca)
    else:
        messagebox.showinfo("Resultado", "Peça não encontrada.")

def mostrar_resultado(peca):
    janela_resultado = tk.Toplevel()
    janela_resultado.title("Resultado da Busca - Peça")
    janela_resultado.geometry("500x250")

    texto = f"""
ID: {peca[0]}
Descrição: {peca[1]}
Tipo: {peca[2]}
Quantidade: {peca[3]}
Validade: {peca[4]}
Observações: {peca[5]}
    """
    tk.Label(janela_resultado, text=texto.strip(), justify="left", font=("Arial", 11)).pack(padx=20, pady=20)

def alterar(entrys):
    id_peca = entrys[0].get().strip()
    novos_dados = get_dados(entrys)
    if any(not campo for campo in novos_dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return
    msg = pecas.alterar_peca(id_peca, novos_dados)
    messagebox.showinfo("Resultado", msg)

def excluir(entrys):
    id_peca = entrys[0].get().strip()
    if not id_peca:
        messagebox.showwarning("Aviso", "Informe o ID da peça a ser excluída.")
        return
    msg = pecas.excluir_peca(id_peca)
    messagebox.showinfo("Resultado", msg)

def abrir_tela_pecas():
    janela = tk.Toplevel()
    janela.title("Cadastro de Peças")
    janela.geometry("600x450")

    labels = ["ID do produto", "Descrição", "Tipo", "Quantidade", "Validade", "Observações"]
    entrys = []

    for i, texto in enumerate(labels):
        tk.Label(janela, text=texto).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(janela, width=40)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entrys.append(entry)

    # Botões de ação
    tk.Button(janela, text="Adicionar", command=lambda: adicionar(entrys)).grid(row=6, column=0, pady=10)
    tk.Button(janela, text="Alterar", command=lambda: alterar(entrys)).grid(row=6, column=1, pady=10)
    tk.Button(janela, text="Excluir", command=lambda: excluir(entrys)).grid(row=6, column=2, pady=10)
    tk.Button(janela, text="Buscar por ID", command=lambda: buscar(entrys)).grid(row=7, column=1, pady=10)

    janela.mainloop()

# Execução direta
if __name__ == "__main__":
    abrir_tela_pecas()
