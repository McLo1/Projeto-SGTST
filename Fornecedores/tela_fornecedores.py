import tkinter as tk
from tkinter import messagebox
from Fornecedores import fornecedores as crud

def adicionar(entrys):
    dados = [e.get().strip() for e in entrys]
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return
    mensagem = crud.adicionar_fornecedor(dados)
    messagebox.showinfo("Sucesso", mensagem)
    for e in entrys:
        e.delete(0, tk.END)

def mostrar_resultado(fornecedor):
    janela = tk.Toplevel()
    janela.title("Fornecedor Encontrado")
    janela.geometry("600x300")

    texto = f"""
ID: {fornecedor[0]}
CNPJ: {fornecedor[1]}
Razão Social: {fornecedor[2]}
Nome Fantasia: {fornecedor[3]}
Área de Atuação: {fornecedor[4]}
Endereço: {fornecedor[5]}
Contato: {fornecedor[6]}
Produtos: {fornecedor[7]}
    """
    tk.Label(janela, text=texto.strip(), justify="left", font=("Arial", 11)).pack(padx=20, pady=20)

def buscar(entry_id):
    id_busca = entry_id.get().strip()
    if not id_busca:
        messagebox.showwarning("Aviso", "Informe o ID do fornecedor para buscar.")
        return
    resultado = crud.buscar_fornecedor(id_busca)
    if resultado:
        mostrar_resultado(resultado)
    else:
        messagebox.showinfo("Resultado", "Fornecedor não encontrado.")

def alterar(entrys):
    id_alvo = entrys[0].get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID do fornecedor.")
        return
    novos_dados = [e.get().strip() for e in entrys]
    mensagem = crud.alterar_fornecedor(id_alvo, novos_dados)
    messagebox.showinfo("Sucesso", mensagem)

def excluir(entry_id):
    id_alvo = entry_id.get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID do fornecedor.")
        return
    mensagem = crud.excluir_fornecedor(id_alvo)
    messagebox.showinfo("Sucesso", mensagem)

def abrir_tela_fornecedores():
    janela = tk.Tk()
    janela.title("Cadastro de Fornecedores")
    janela.geometry("850x500")

    labels = [
        "ID do fornecedor", "CNPJ", "Razão Social", "Nome Fantasia",
        "Área de Atuação", "Endereço", "Contato", "Produtos"
    ]
    entrys = []

    for i, texto in enumerate(labels):
        tk.Label(janela, text=texto).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(janela, width=50)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entrys.append(entry)

    tk.Button(janela, text="Adicionar", command=lambda: adicionar(entrys)).grid(row=len(labels), column=0, pady=10)
    tk.Button(janela, text="Alterar", command=lambda: alterar(entrys)).grid(row=len(labels), column=1, pady=10)
    tk.Button(janela, text="Excluir", command=lambda: excluir(entrys[0])).grid(row=len(labels), column=2, pady=10)
    tk.Button(janela, text="Buscar por ID", command=lambda: buscar(entrys[0])).grid(row=len(labels)+1, column=1, pady=10)

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_fornecedores()
