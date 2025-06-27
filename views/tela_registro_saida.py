import tkinter as tk
from tkinter import messagebox

def registrar_saida(entrys):
    dados = [e.get().strip() for e in entrys]
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return
    with open("registros_saida.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{', '.join(dados)}\n")
    messagebox.showinfo("Sucesso", "Saída registrada com sucesso!")
    for e in entrys:
        e.delete(0, tk.END)

def mostrar_resultado_saida(saida):
    janela_resultado = tk.Toplevel()
    janela_resultado.title("Resultado da Busca - Saída de Caminhão")
    janela_resultado.geometry("600x300")

    texto = f"""
ID Caminhão: {saida[0]}
ID Cliente: {saida[1]}
Tipo de Carga: {saida[2]}
Destino: {saida[3]}
Horário de Entrada: {saida[4]}
Horário de Saída: {saida[5]}
KM Inicial: {saida[6]}
KM Final: {saida[7]}
    """
    tk.Label(janela_resultado, text=texto.strip(), justify="left", font=("Arial", 11)).pack(padx=20, pady=20)

def buscar_saida_por_id(entry_id):
    id_busca = entry_id.get().strip()
    if not id_busca:
        messagebox.showwarning("Aviso", "Informe o ID do caminhão para buscar.")
        return

    try:
        with open("registros_saida.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                item = linha.strip().split(",")
                if item[0] == id_busca:
                    mostrar_resultado_saida(item)
                    return
        messagebox.showinfo("Resultado", "Registro de saída não encontrado.")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de registros de saída não encontrado.")

def abrir_tela_saida_caminhao():
    janela = tk.Tk()
    janela.title("Registro de Saída de Caminhão")
    janela.geometry("700x450")

    labels = [
        "ID do Caminhão", "ID do Cliente", "Tipo de Carga", "Destino",
        "Horário de Entrada", "Horário de Saída",
        "KM Inicial", "KM Final"
    ]
    entrys = []

    for i, texto in enumerate(labels):
        tk.Label(janela, text=texto).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(janela, width=50)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entrys.append(entry)

    tk.Button(janela, text="Registrar Saída", command=lambda: registrar_saida(entrys)).grid(row=len(labels), column=0, pady=15)
    tk.Button(janela, text="Buscar por ID do Caminhão", command=lambda: buscar_saida_por_id(entrys[0])).grid(row=len(labels), column=1, pady=15)

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_saida_caminhao()
