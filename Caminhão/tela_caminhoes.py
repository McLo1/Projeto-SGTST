import tkinter as tk
from tkinter import messagebox
from Caminhão import caminhao as cam

def get_dados(entrys):
    return [e.get().strip() for e in entrys]

def limpar(entrys):
    for e in entrys:
        e.delete(0, tk.END)

def adicionar(entrys):
    dados = get_dados(entrys)
    if any(not d for d in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return
    msg = cam.adicionar_caminhao(dados)
    messagebox.showinfo("OK", msg)
    limpar(entrys)

def buscar(entrys):
    id_cam = entrys[0].get().strip()
    if not id_cam:
        messagebox.showwarning("Aviso", "Digite o ID.")
        return
    caminhao = cam.buscar_caminhao(id_cam)
    if caminhao:
        messagebox.showinfo("Encontrado", "\n".join(caminhao))
    else:
        messagebox.showinfo("Não encontrado", "ID não localizado.")

def alterar(entrys):
    id_cam = entrys[0].get().strip()
    dados = get_dados(entrys)
    if any(not d for d in dados):
        messagebox.showwarning("Aviso", "Preencha tudo.")
        return
    msg = cam.alterar_caminhao(id_cam, dados)
    messagebox.showinfo("Resultado", msg)

def excluir(entrys):
    id_cam = entrys[0].get().strip()
    if not id_cam:
        messagebox.showwarning("Aviso", "Informe o ID.")
        return
    msg = cam.excluir_caminhao(id_cam)
    messagebox.showinfo("Resultado", msg)

def abrir_tela():
    janela = tk.Tk()
    janela.title("Caminhões")
    janela.geometry("700x500")

    campos = ["ID", "Renavan", "Modelo", "Marca", "Cor", "Placa", "Chassi", "Status", "Tipo", "Peso"]
    entrys = []

    for i, nome in enumerate(campos):
        tk.Label(janela, text=nome).grid(row=i, column=0, sticky="w", padx=10, pady=5)
        ent = tk.Entry(janela, width=40)
        ent.grid(row=i, column=1, padx=10, pady=5)
        entrys.append(ent)

    tk.Button(janela, text="Adicionar", command=lambda: adicionar(entrys)).grid(row=11, column=0, pady=10)
    tk.Button(janela, text="Buscar por ID", command=lambda: buscar(entrys)).grid(row=11, column=1, pady=10)
    tk.Button(janela, text="Alterar", command=lambda: alterar(entrys)).grid(row=12, column=0, pady=10)
    tk.Button(janela, text="Excluir", command=lambda: excluir(entrys)).grid(row=12, column=1, pady=10)

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela()
