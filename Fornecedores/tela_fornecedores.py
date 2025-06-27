"""
Nome do arquivo: tela_fornecedores.py
Equipe: Marcelo, Layza, Vanderson, Caique.
Turma: G91166
Semestre: 2025.1
"""

import tkinter as tk
from tkinter import ttk, messagebox
from Fornecedores import fornecedores as crud

# Cores e estilos
COR_FUNDO = "#f0f4f8"
COR_BOTAO = "#4a90e2"
COR_TEXTO = "#ffffff"

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
    tk.Label(janela, text=texto.strip(), justify="left", font=("Segoe UI", 11)).pack(padx=20, pady=20)

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
    janela.geometry("800x600")
    janela.configure(bg=COR_FUNDO)

    style = ttk.Style(janela)
    style.theme_use("clam")
    style.configure("Custom.TButton", font=("Segoe UI", 11), foreground=COR_TEXTO,
                    background=COR_BOTAO, padding=8)
    style.map("Custom.TButton", background=[('active', '#357ABD')])

    tk.Label(janela, text="Cadastro de Fornecedores", font=("Segoe UI", 18, "bold"),
             bg=COR_FUNDO, fg="#333").pack(pady=20)

    frame_form = tk.Frame(janela, bg=COR_FUNDO)
    frame_form.pack()

    labels = [
        "ID do fornecedor", "CNPJ", "Razão Social", "Nome Fantasia",
        "Área de Atuação", "Endereço", "Contato", "Produtos"
    ]
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

    botao("Adicionar", lambda: adicionar(entrys))
    botao("Alterar", lambda: alterar(entrys))
    botao("Excluir", lambda: excluir(entrys[0]))
    botao("Buscar por ID", lambda: buscar(entrys[0]))

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_fornecedores()
