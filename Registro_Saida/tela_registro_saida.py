"""
Nome do arquivo: tela_registro_saida.py
Equipe: Marcelo, Layza, Vanderson, Caique.
Turma: G91166
Semestre: 2025.1
"""

import tkinter as tk
from tkinter import ttk, messagebox
from Registro_Saida import Registro_saida as saida_caminhao

# Cores padrão do sistema
COR_FUNDO = "#f0f4f8"
COR_BOTAO = "#4a90e2"
COR_TEXTO = "#ffffff"

def limpar_campos(entrys):
    for e in entrys:
        e.delete(0, tk.END)

def get_dados(entrys):
    return [e.get().strip() for e in entrys]

def registrar_saida(entrys):
    dados = get_dados(entrys)
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
    novos_dados = get_dados(entrys)
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

def mostrar_resultado_saida(saida):
    janela_resultado = tk.Toplevel()
    janela_resultado.title("Saída Encontrada")
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
    tk.Label(janela_resultado, text=texto.strip(), justify="left", font=("Segoe UI", 11)).pack(padx=20, pady=20)

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

def abrir_tela_saida_caminhao():
    janela = tk.Tk()
    janela.title("Registro de Saída de Caminhão")
    janela.geometry("750x550")
    janela.configure(bg=COR_FUNDO)

    style = ttk.Style(janela)
    style.theme_use("clam")
    style.configure("Custom.TButton", font=("Segoe UI", 11), foreground=COR_TEXTO,
                    background=COR_BOTAO, padding=8)
    style.map("Custom.TButton", background=[('active', '#357ABD')])

    tk.Label(janela, text="Registro de Saída de Caminhão", font=("Segoe UI", 18, "bold"),
             bg=COR_FUNDO, fg="#333").pack(pady=20)

    frame_form = tk.Frame(janela, bg=COR_FUNDO)
    frame_form.pack()

    labels = [
        "ID do Caminhão", "ID do Cliente", "Tipo de Carga", "Destino",
        "Horário de Entrada", "Horário de Saída", "KM Inicial", "KM Final"
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
        ttk.Button(frame_botoes, text=texto, style="Custom.TButton", width=30, command=comando).pack(pady=5)

    botao("Registrar Saída", lambda: registrar_saida(entrys))
    botao("Buscar por ID do Caminhão", lambda: buscar_saida_por_id(entrys[0]))
    botao("Alterar Saída", lambda: alterar_saida(entrys))
    botao("Excluir Saída", lambda: excluir_saida(entrys[0]))

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_saida_caminhao()
