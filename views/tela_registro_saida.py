import tkinter as tk
from tkinter import messagebox

def registrar_saida(entrys, text_area):
    dados = [e.get().strip() for e in entrys]
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return
    with open("registros_saida.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{', '.join(dados)}\n")
    messagebox.showinfo("Sucesso", "Saída registrada com sucesso!")
    for e in entrys:
        e.delete(0, tk.END)

def listar_saidas(text_area):
    text_area.delete("1.0", tk.END)
    try:
        with open("registros_saida.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                text_area.insert(tk.END, linha)
    except FileNotFoundError:
        messagebox.showinfo("Info", "Nenhum registro encontrado.")

def abrir_tela_saida_caminhao():
    janela = tk.Tk()
    janela.title("Registro de Saída de Caminhão")
    janela.geometry("900x600")

    labels = [
        "ID do Caminhão", "ID do Cliente", "Tipo de Carga", "Destino",
        "Horário de Entrada", "Horário de Saída",
        "KM Inicial", "KM Final"
    ]
    entrys = []

    for i, texto in enumerate(labels):
        tk.Label(janela, text=texto).grid(row=i, column=0, padx=10, pady=5, sticky="w")
        entry = tk.Entry(janela, width=60)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entrys.append(entry)

    caixa_texto = tk.Text(janela, width=100, height=10)
    caixa_texto.grid(row=len(labels)+2, column=0, columnspan=3, padx=10, pady=10)

    tk.Button(janela, text="Registrar Saída", command=lambda: registrar_saida(entrys, caixa_texto)).grid(row=len(labels), column=0, pady=10)
    tk.Button(janela, text="Listar Saídas", command=lambda: listar_saidas(caixa_texto)).grid(row=len(labels), column=1, pady=10)

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_saida_caminhao()
