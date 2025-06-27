import tkinter as tk
from tkinter import ttk, messagebox
from Caminhão import caminhao as cam

# Cores e estilo
COR_FUNDO = "#f0f4f8"
COR_BOTAO = "#4a90e2"
COR_TEXTO = "#ffffff"

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
        janela_resultado = tk.Toplevel()
        janela_resultado.title("Caminhão Encontrado")
        janela_resultado.geometry("600x300")

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
        tk.Label(janela_resultado, text=texto.strip(), justify="left", font=("Segoe UI", 11)).pack(padx=20, pady=20)
    else:
        messagebox.showinfo("Não encontrado", "ID não localizado.")


def alterar(entrys):
    id_cam = entrys[0].get().strip()
    dados = get_dados(entrys)
    if any(not d for d in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
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
    janela.title("Cadastro de Caminhões")
    janela.geometry("700x600")
    janela.configure(bg=COR_FUNDO)

    # Estilo dos botões
    style = ttk.Style(janela)
    style.theme_use("clam")
    style.configure("Custom.TButton", font=("Segoe UI", 11), foreground=COR_TEXTO,
                    background=COR_BOTAO, padding=8)
    style.map("Custom.TButton", background=[('active', '#357ABD')])

    # Título
    tk.Label(janela, text="Cadastro de Caminhões", font=("Segoe UI", 18, "bold"),
             bg=COR_FUNDO, fg="#333").pack(pady=20)

    # Container para formulário
    frame_form = tk.Frame(janela, bg=COR_FUNDO)
    frame_form.pack(pady=10)

    campos = ["ID", "Renavan", "Modelo", "Marca", "Cor", "Placa", "Chassi", "Status", "Tipo", "Peso"]
    entrys = []

    for i, nome in enumerate(campos):
        tk.Label(frame_form, text=nome + ":", bg=COR_FUNDO, anchor="w", font=("Segoe UI", 10)).grid(row=i, column=0, sticky="w", padx=10, pady=5)
        ent = tk.Entry(frame_form, width=45)
        ent.grid(row=i, column=1, padx=10, pady=5)
        entrys.append(ent)

    # Container para botões
    frame_botoes = tk.Frame(janela, bg=COR_FUNDO)
    frame_botoes.pack(pady=20)

    def criar_botao(texto, comando):
        ttk.Button(frame_botoes, text=texto, style="Custom.TButton", width=25, command=comando).pack(pady=5)

    criar_botao("Adicionar", lambda: adicionar(entrys))
    criar_botao("Buscar por ID", lambda: buscar(entrys))
    criar_botao("Alterar", lambda: alterar(entrys))
    criar_botao("Excluir", lambda: excluir(entrys))

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela()
