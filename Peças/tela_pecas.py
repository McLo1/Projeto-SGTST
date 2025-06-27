import tkinter as tk
from tkinter import ttk, messagebox
from Peças import pecas

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
    if any(not campo for campo in dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return
    msg = pecas.adicionar_peca(dados)
    messagebox.showinfo("Sucesso", msg)
    limpar(entrys)

def buscar(entrys):
    id_peca = entrys[0].get().strip()
    if not id_peca:
        messagebox.showwarning("Aviso", "Informe o ID da peça para buscar.")
        return
    peca = pecas.buscar_peca(id_peca)
    if peca:
        mostrar_resultado(peca)
    else:
        messagebox.showinfo("Resultado", "Peça não encontrada.")

def mostrar_resultado(peca):
    janela_resultado = tk.Toplevel()
    janela_resultado.title("Peça Encontrada")
    janela_resultado.geometry("500x250")

    texto = f"""
ID: {peca[0]}
Descrição: {peca[1]}
Tipo: {peca[2]}
Quantidade: {peca[3]}
Validade: {peca[4]}
Observações: {peca[5]}
    """
    tk.Label(janela_resultado, text=texto.strip(), justify="left", font=("Segoe UI", 11)).pack(padx=20, pady=20)

def alterar(entrys):
    id_peca = entrys[0].get().strip()
    novos_dados = get_dados(entrys)
    if any(not campo for campo in novos_dados):
        messagebox.showwarning("Aviso", "Preencha todos os campos.")
        return
    msg = pecas.alterar_peca(id_peca, novos_dados)
    messagebox.showinfo("Resultado", msg)

def excluir(entrys):
    id_peca = entrys[0].get().strip()
    if not id_peca:
        messagebox.showwarning("Aviso", "Informe o ID da peça a ser excluída.")
        return
    msg = pecas.excluir_peca(id_peca)
    messagebox.showinfo("Resultado", msg)

def abrir_tela_pecas():
    janela = tk.Tk()
    janela.title("Cadastro de Peças")
    janela.geometry("700x500")
    janela.configure(bg=COR_FUNDO)

    style = ttk.Style(janela)
    style.theme_use("clam")
    style.configure("Custom.TButton", font=("Segoe UI", 11), foreground=COR_TEXTO,
                    background=COR_BOTAO, padding=8)
    style.map("Custom.TButton", background=[('active', '#357ABD')])

    tk.Label(janela, text="Cadastro de Peças", font=("Segoe UI", 18, "bold"),
             bg=COR_FUNDO, fg="#333").pack(pady=20)

    frame_form = tk.Frame(janela, bg=COR_FUNDO)
    frame_form.pack()

    labels = ["ID do produto", "Descrição", "Tipo", "Quantidade", "Validade", "Observações"]
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
    botao("Excluir", lambda: excluir(entrys))
    botao("Buscar por ID", lambda: buscar(entrys))

    janela.mainloop()

if __name__ == "__main__":
    abrir_tela_pecas()
