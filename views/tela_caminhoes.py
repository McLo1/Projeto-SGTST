import tkinter as tk
from tkinter import messagebox

def adicionar_caminhao(entrys):
    dados = [e.get().strip() for e in entrys]
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return

    with open("caminhoes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{', '.join(dados)}\n")
    messagebox.showinfo("Sucesso", "Caminhão adicionado com sucesso!")
    for e in entrys:
        e.delete(0, tk.END)

def mostrar_resultado_em_janela(caminhao):
    janela_resultado = tk.Toplevel()
    janela_resultado.title("Resultado da Busca")
    janela_resultado.geometry("200x300")

    texto = f"""
ID: {caminhao[0]}
Renavan: {caminhao[1]}
Modelo: {caminhao[2]}
Marca: {caminhao[3]}
Cor: {caminhao[4]}
Placa: {caminhao[5]}
Chassi: {caminhao[6]}
Status: {caminhao[7]}
Tipo: {caminhao[8]}
Peso: {caminhao[9]}
    """
    tk.Label(janela_resultado, text=texto.strip(), justify="left", font=("Arial", 11)).pack(padx=20, pady=20)

def buscar_caminhao_por_id(entry_id):
    id_busca = entry_id.get().strip()
    if not id_busca:
        messagebox.showwarning("Aviso", "Informe o ID do caminhão para buscar.")
        return

    try:
        with open("caminhoes.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                item = linha.strip().split(",")
                if item[0] == id_busca:
                    mostrar_resultado_em_janela(item)
                    return
        messagebox.showinfo("Resultado", "Caminhão não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de caminhões não encontrado.")

def alterar_caminhao(entrys):
    id_alvo = entrys[0].get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID do caminhão a ser alterado.")
        return

    novos_dados = [e.get().strip() for e in entrys]
    atualizado = False

    try:
        with open("caminhoes.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        with open("caminhoes.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas:
                item = linha.strip().split(",")
                if item[0] == id_alvo:
                    arquivo.write(", ".join(novos_dados) + "\n")
                    atualizado = True
                else:
                    arquivo.write(linha)
        if atualizado:
            messagebox.showinfo("Sucesso", "Caminhão alterado com sucesso!")
        else:
            messagebox.showwarning("Aviso", "ID não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de caminhões não encontrado.")

def excluir_caminhao(entry_id):
    id_alvo = entry_id.get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID do caminhão a ser excluído.")
        return

    excluido = False
    try:
        with open("caminhoes.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        with open("caminhoes.txt", "w", encoding="utf-8") as arquivo:
            for linha in linhas:
                item = linha.strip().split(",")
                if item[0] != id_alvo:
                    arquivo.write(linha)
                else:
                    excluido = True
        if excluido:
            messagebox.showinfo("Sucesso", "Caminhão removido com sucesso!")
        else:
            messagebox.showwarning("Aviso", "ID não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de caminhões não encontrado.")

def abrir_tela_caminhoes():
    janela = tk.Tk()
    janela.title("Cadastro de Caminhões")
    janela.geometry("750x600")

    labels = ["ID do caminhão", "Renavan", "Modelo", "Marca", "Cor", "Placa", "Chassi", "Status", "Tipo", "Peso"]
    entrys = []

    for i, texto in enumerate(labels):
        tk.Label(janela, text=texto).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(janela, width=50)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entrys.append(entry)

    # Botões principais
    tk.Button(janela, text="Adicionar", command=lambda: adicionar_caminhao(entrys)).grid(row=11, column=0, pady=10)
    tk.Button(janela, text="Alterar", command=lambda: alterar_caminhao(entrys)).grid(row=11, column=1, pady=10)
    tk.Button(janela, text="Excluir", command=lambda: excluir_caminhao(entrys[0])).grid(row=11, column=2, pady=10)

    # Botão de busca por ID (substituindo a listagem)
    tk.Button(janela, text="Buscar por ID", command=lambda: buscar_caminhao_por_id(entrys[0])).grid(row=12, column=1, pady=10)

    janela.mainloop()
