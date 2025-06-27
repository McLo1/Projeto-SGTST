import tkinter as tk
from tkinter import messagebox

def adicionar_funcionario(entrys):
    dados = [e.get().strip() for e in entrys]
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return

    with open("funcionarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{', '.join(dados)}\n")
    messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso!")
    for e in entrys:
        e.delete(0, tk.END)

def mostrar_resultado_funcionario(funcionario):
    janela_resultado = tk.Toplevel()
    janela_resultado.title("Resultado da Busca - Funcionário")
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
    tk.Label(janela_resultado, text=texto.strip(), justify="left", font=("Arial", 11)).pack(padx=20, pady=20)

def buscar_funcionario_por_id(entry_id):
    id_busca = entry_id.get().strip()
    if not id_busca:
        messagebox.showwarning("Aviso", "Informe o ID do funcionário para buscar.")
        return

    try:
        with open("funcionarios.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                item = linha.strip().split(",")
                if item[0] == id_busca:
                    mostrar_resultado_funcionario(item)
                    return
        messagebox.showinfo("Resultado", "Funcionário não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de funcionários não encontrado.")

def alterar_funcionario(entrys):
    id_alvo = entrys[0].get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID do funcionário a ser alterado.")
        return

    novos_dados = [e.get().strip() for e in entrys]
    atualizado = False

    try:
        with open("funcionarios.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        with open("funcionarios.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas:
                item = linha.strip().split(",")
                if item[0] == id_alvo:
                    arquivo.write(", ".join(novos_dados) + "\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
        if atualizado:
            messagebox.showinfo("Sucesso", "Funcionário alterado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "ID não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de funcionários não encontrado.")

def excluir_funcionario(entry_id):
    id_alvo = entry_id.get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID do funcionário a ser excluído.")
        return

    excluido = False
    try:
        with open("funcionarios.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        with open("funcionarios.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas:
                item = linha.strip().split(",")
                if item[0] != id_alvo:
                    arquivo.write(linha)
                else:
                    excluido = True
        if excluido:
            messagebox.showinfo("Sucesso", "Funcionário removido com sucesso!")
        else:
            messagebox.showwarning("Aviso", "ID não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de funcionários não encontrado.")

def abrir_tela_funcionarios():
    janela = tk.Tk()
    janela.title("Cadastro de Funcionários")
    janela.geometry("800x500")

    labels = ["ID do funcionário", "Nome", "CPF", "Cargo", "Data de nascimento", "Endereço", "Contato"]
    entrys = []

    for i, texto in enumerate(labels):
        tk.Label(janela, text=texto).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(janela, width=50)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entrys.append(entry)

    tk.Button(janela, text="Adicionar", command=lambda: adicionar_funcionario(entrys)).grid(row=len(labels), column=0, pady=10)
    tk.Button(janela, text="Alterar", command=lambda: alterar_funcionario(entrys)).grid(row=len(labels), column=1, pady=10)
    tk.Button(janela, text="Excluir", command=lambda: excluir_funcionario(entrys[0])).grid(row=len(labels), column=2, pady=10)
    tk.Button(janela, text="Buscar por ID", command=lambda: buscar_funcionario_por_id(entrys[0])).grid(row=len(labels)+1, column=1, pady=10)

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_funcionarios()
