import tkinter as tk
from tkinter import messagebox

# === Funções do CRUD originais adaptadas para GUI ===
def adicionar_pecas(entrys):
    dados = [e.get().strip() for e in entrys]
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return

    with open("peças.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{dados[0]}, {dados[1]}, {dados[2]}, {dados[3]}, {dados[4]}, {dados[5]}\n")
    messagebox.showinfo("Sucesso", "Peça adicionada com sucesso!")
    for e in entrys:
        e.delete(0, tk.END)

def listar_pecas(caixa_texto):
    caixa_texto.delete("1.0", tk.END)
    try:
        with open("peças.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                item = linha.strip().split(",")
                caixa_texto.insert(tk.END, f"ID: {item[0]} | Descrição: {item[1]} | Tipo: {item[2]} | Quantidade: {item[3]} | Validade: {item[4]} | Obs: {item[5]}\n")
    except FileNotFoundError:
        messagebox.showinfo("Info", "Nenhuma peça cadastrada ainda.")

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
    janela.geometry("600x550")

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

    caixa_texto = tk.Text(janela, width=70, height=15)
    caixa_texto.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

    tk.Button(janela, text="Listar Peças", command=lambda: listar_pecas(caixa_texto)).grid(row=8, column=1, pady=10)

    janela.mainloop()