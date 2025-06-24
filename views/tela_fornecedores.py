import tkinter as tk
from tkinter import messagebox

def adicionar_fornecedor(entrys):
    dados = [e.get().strip() for e in entrys]
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return

    with open("fornecedores.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{', '.join(dados)}\n")
    messagebox.showinfo("Sucesso", "Fornecedor adicionado com sucesso!")
    for e in entrys:
        e.delete(0, tk.END)

def listar_fornecedores(caixa_texto):
    caixa_texto.delete("1.0", tk.END)
    try:
        with open("fornecedores.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                item = linha.strip().split(",")
                caixa_texto.insert(tk.END, f"ID: {item[0]} | CNPJ: {item[1]} | Razão Social: {item[2]} | Nome Fantasia: {item[3]} | Área de Atuação: {item[4]} | Endereço: {item[5]} | Contato: {item[6]} | Produtos: {item[7]}\n")
    except FileNotFoundError:
        messagebox.showinfo("Info", "Nenhum fornecedor cadastrado ainda.")

def alterar_fornecedor(entrys):
    id_alvo = entrys[0].get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID do fornecedor a ser alterado.")
        return

    novos_dados = [e.get().strip() for e in entrys]
    atualizado = False

    try:
        with open("fornecedores.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        with open("fornecedores.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas:
                item = linha.strip().split(",")
                if item[0] == id_alvo:
                    arquivo.write(", ".join(novos_dados) + "\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
        if atualizado:
            messagebox.showinfo("Sucesso", "Fornecedor alterado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "ID não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de fornecedores não encontrado.")

def excluir_fornecedor(entry_id):
    id_alvo = entry_id.get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID do fornecedor a ser excluído.")
        return

    excluido = False
    try:
        with open("fornecedores.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        with open("fornecedores.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas:
                item = linha.strip().split(",")
                if item[0] != id_alvo:
                    arquivo.write(linha)
                else:
                    excluido = True
        if excluido:
            messagebox.showinfo("Sucesso", "Fornecedor removido com sucesso!")
        else:
            messagebox.showwarning("Aviso", "ID não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de fornecedores não encontrado.")

def abrir_tela_fornecedores():
    janela = tk.Tk()
    janela.title("Cadastro de Fornecedores")
    janela.geometry("800x600")

    labels = ["ID do fornecedor", "CNPJ", "Razão Social", "Nome Fantasia", "Área de Atuação", "Endereço", "Contato", "Produtos"]
    entrys = []

    for i, texto in enumerate(labels):
        tk.Label(janela, text=texto).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(janela, width=50)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entrys.append(entry)

    caixa_texto = tk.Text(janela, width=95, height=15)
    caixa_texto.grid(row=len(labels)+1, column=0, columnspan=3, padx=10, pady=10)

    tk.Button(janela, text="Adicionar", command=lambda: adicionar_fornecedor(entrys)).grid(row=len(labels), column=0, pady=10)
    tk.Button(janela, text="Alterar", command=lambda: alterar_fornecedor(entrys)).grid(row=len(labels), column=1, pady=10)
    tk.Button(janela, text="Excluir", command=lambda: excluir_fornecedor(entrys[0])).grid(row=len(labels), column=2, pady=10)
    tk.Button(janela, text="Listar Fornecedores", command=lambda: listar_fornecedores(caixa_texto)).grid(row=len(labels)+2, column=1, pady=10)

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_fornecedores()
