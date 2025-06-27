import tkinter as tk
from tkinter import messagebox
from Registro_Saida import Registro_saida as saida_caminhao

def registrar_saida(entrys):
    dados = [e.get().strip() for e in entrys]
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return
    msg = saida_caminhao.adicionar_saida(dados)
    messagebox.showinfo("Sucesso", msg)
    limpar_campos(entrys)

def alterar_saida(entrys):
    id_alvo = entrys[0].get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID do caminhão para alterar.")
        return

    novos_dados = [e.get().strip() for e in entrys]
    msg = saida_caminhao.alterar_saida(id_alvo, novos_dados)
    messagebox.showinfo("Resultado", msg)
    limpar_campos(entrys)

def excluir_saida(entry_id):
    id_alvo = entry_id.get().strip()
    if not id_alvo:
        messagebox.showwarning("Aviso", "Informe o ID do caminhão para excluir.")
        return

    msg = saida_caminhao.excluir_saida(id_alvo)
    messagebox.showinfo("Resultado", msg)
    entry_id.delete(0, tk.END)

def limpar_campos(entrys):
    for e in entrys:
        e.delete(0, tk.END)

def mostrar_resultado_saida(saida):
    janela_resultado = tk.Toplevel()
    janela_resultado.title("Resultado da Busca - Saída de Caminhão")
    janela_resultado.geometry("600x300")

    texto = (
        f"ID Caminhão: {saida[0]}\n"
        f"ID Cliente: {saida[1]}\n"
        f"Tipo de Carga: {saida[2]}\n"
        f"Destino: {saida[3]}\n"
        f"Horário de Entrada: {saida[4]}\n"
        f"Horário de Saída: {saida[5]}\n"
        f"KM Inicial: {saida[6]}\n"
        f"KM Final: {saida[7]}"
    )
    tk.Label(janela_resultado, text=texto, justify="left", font=("Arial", 11)).pack(padx=20, pady=20)

def buscar_saida_por_id(entry_id):
    id_busca = entry_id.get().strip()
    if not id_busca:
        messagebox.showwarning("Aviso", "Informe o ID do caminhão para buscar.")
        return

    saida = saida_caminhao.buscar_saida(id_busca)
    if saida:
        mostrar_resultado_saida(saida)
    else:
        messagebox.showinfo("Resultado", "Registro de saída não encontrado.")

def criar_label_entry(janela, texto, linha, largura=50):
    tk.Label(janela, text=texto).grid(row=linha, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(janela, width=largura)
    entry.grid(row=linha, column=1, padx=10, pady=5)
    return entry

def abrir_tela_saida_caminhao():
    janela = tk.Tk()
    janela.title("Registro de Saída de Caminhão")
    janela.geometry("700x500")

    labels = [
        "ID do Caminhão", "ID do Cliente", "Tipo de Carga", "Destino",
        "Horário de Entrada", "Horário de Saída",
        "KM Inicial", "KM Final"
    ]

    entrys = [criar_label_entry(janela, texto, i) for i, texto in enumerate(labels)]

    tk.Button(janela, text="Registrar Saída", command=lambda: registrar_saida(entrys)).grid(row=len(labels), column=0, pady=10)
    tk.Button(janela, text="Buscar por ID do Caminhão", command=lambda: buscar_saida_por_id(entrys[0])).grid(row=len(labels), column=1, pady=10)
    tk.Button(janela, text="Alterar Saída", command=lambda: alterar_saida(entrys)).grid(row=len(labels)+1, column=0, pady=10)
    tk.Button(janela, text="Excluir Saída", command=lambda: excluir_saida(entrys[0])).grid(row=len(labels)+1, column=1, pady=10)

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_saida_caminhao()
