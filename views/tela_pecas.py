import tkinter as tk
from tkinter import messagebox

def adicionar_pecas(entrys):
    dados = [e.get().strip() for e in entrys]
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return

    with open("peças.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(", ".join(dados) + "\n")
    messagebox.showinfo("Sucesso", "Peça adicionada com sucesso!")
    for e in entrys:
        e.delete(0, tk.END)

def mostrar_resultado_peca(peca):
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

def buscar_peca_por_id(entry_id):
    id_busca = entry_id.get().strip()
    if not id_busca:
        messagebox.showwarning("Aviso", "Informe o ID da peça para buscar.")
        return

    try:
        with open("peças.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                item = linha.strip().split(",")
                if item[0] == id_busca:
                    mostrar_resultado_peca(item)
                    return
        messagebox.showinfo("Resultado", "Peça não encontrada.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de peças não encontrado.")

def alterar_pecas(entrys):
    id_alvo = entrys[0].get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID da peça a ser alterada.")
        return

    novos_dados = [e.get().strip() for e in entrys]
    atualizado = False

    try:
        with open("peças.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        with open("peças.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas:
                item = linha.strip().split(",")
                if item[0] == id_alvo:
                    arquivo.write(", ".join(novos_dados) + "\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
        if atualizado:
            messagebox.showinfo("Sucesso", "Peça alterada com sucesso!")
        else:
            messagebox.showwarning("Aviso", "ID não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de peças não encontrado.")

def excluir_pecas(entry_id):
    id_alvo = entry_id.get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID da peça a ser excluída.")
        return

    excluido = False
    try:
        with open("peças.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        with open("peças.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas:
                item = linha.strip().split(",")
                if item[0] != id_alvo:
                    arquivo.write(linha)
                else:
                    excluido = True
        if excluido:
            messagebox.showinfo("Sucesso", "Peça removida com sucesso!")
        else:
            messagebox.showwarning("Aviso", "ID não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de peças não encontrado.")

# === Interface ===
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
    tk.Button(janela, text="Adicionar", command=lambda: adicionar_pecas(entrys)).grid(row=6, column=0, pady=10)
    tk.Button(janela, text="Alterar", command=lambda: alterar_pecas(entrys)).grid(row=6, column=1, pady=10)
    tk.Button(janela, text="Excluir", command=lambda: excluir_pecas(entrys[0])).grid(row=6, column=2, pady=10)
    tk.Button(janela, text="Buscar por ID", command=lambda: buscar_peca_por_id(entrys[0])).grid(row=7, column=1, pady=10)

    janela.mainloop()
