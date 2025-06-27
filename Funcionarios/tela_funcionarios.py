"""
Nome do arquivo: tela_funcionarios.py
Equipe: Marcelo, Layza, Vanderson, Caique.
Turma: G91166
Semestre: 2025.1
"""

import tkinter as tk
from tkinter import ttk, messagebox
from Funcionarios import funcionarios

# Cores e estilos
COR_FUNDO = "#f0f4f8"
COR_BOTAO = "#4a90e2"
COR_TEXTO = "#ffffff"

def adicionar_funcionario(entrys):
    dados = [e.get().strip() for e in entrys]
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return
    msg = funcionarios.adicionar_funcionario(dados)
    messagebox.showinfo("Sucesso", msg)
    for e in entrys:
        e.delete(0, tk.END)

def mostrar_resultado_funcionario(funcionario):
    janela_resultado = tk.Toplevel()
    janela_resultado.title("Funcionário Encontrado")
    janela_resultado.geometry("500x250")

    texto = f"""
ID: {funcionario[0]}
Nome: {funcionario[1]}
CPF: {funcionario[2]}
Cargo: {funcionario[3]}
Nascimento: {funcionario[4]}
Endereço: {funcionario[5]}
Contato: {funcionario[6]}
    """
    tk.Label(janela_resultado, text=texto.strip(), justify="left", font=("Segoe UI", 11)).pack(padx=20, pady=20)

def buscar_funcionario_por_id(entry_id):
    id_busca = entry_id.get().strip()
    if not id_busca:
        messagebox.showwarning("Aviso", "Informe o ID do funcionário para buscar.")
        return
    funcionario = funcionarios.buscar_funcionario(id_busca)
    if funcionario:
        mostrar_resultado_funcionario(funcionario)
    else:
        messagebox.showinfo("Resultado", "Funcionário não encontrado.")

def alterar_funcionario(entrys):
    id_funcionario = entrys[0].get().strip()
    if not id_funcionario:
        messagebox.showwarning("Aviso", "Informe o ID do funcionário a ser alterado.")
        return
    novos_dados = [e.get().strip() for e in entrys]
    msg = funcionarios.alterar_funcionario(id_funcionario, novos_dados)
    messagebox.showinfo("Resultado", msg)

def excluir_funcionario(entry_id):
    id_funcionario = entry_id.get().strip()
    if not id_funcionario:
        messagebox.showwarning("Aviso", "Informe o ID do funcionário a ser excluído.")
        return
    msg = funcionarios.excluir_funcionario(id_funcionario)
    messagebox.showinfo("Resultado", msg)

def abrir_tela_funcionarios():
    janela = tk.Tk()
    janela.title("Cadastro de Funcionários")
    janela.geometry("900x700")
    janela.configure(bg=COR_FUNDO)

    style = ttk.Style(janela)
    style.theme_use("clam")
    style.configure("Custom.TButton", font=("Segoe UI", 11), foreground=COR_TEXTO,
                    background=COR_BOTAO, padding=8)
    style.map("Custom.TButton", background=[('active', '#357ABD')])

    tk.Label(janela, text="Cadastro de Funcionários", font=("Segoe UI", 18, "bold"),
             bg=COR_FUNDO, fg="#333").pack(pady=20)

    frame_form = tk.Frame(janela, bg=COR_FUNDO)
    frame_form.pack()

    labels = ["ID do funcionário", "Nome", "CPF", "Cargo", "Data de nascimento", "Endereço", "Contato"]
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

    botao("Adicionar", lambda: adicionar_funcionario(entrys))
    botao("Buscar por ID", lambda: buscar_funcionario_por_id(entrys[0]))
    botao("Alterar", lambda: alterar_funcionario(entrys))
    botao("Excluir", lambda: excluir_funcionario(entrys[0]))

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_funcionarios()
