import tkinter as tk
from tkinter import ttk
#from tela_fornecedores import abrir_tela_fornecedores  # depois vamos criar essa função
from tela_pecas import abrir_tela_pecas
from tela_caminhoes import abrir_tela_caminhoes
from tela_fornecedores import abrir_tela_fornecedores
from tela_funcionarios import abrir_tela_funcionarios
from tela_clientes import abrir_tela_clientes

# Criação da janela principal
janela = tk.Tk()
janela.title("Sistema de Cadastro")
janela.geometry("300x400")

label = ttk.Label(janela, text="MENU DO SISTEMA", font=("Arial", 16))
label.pack(pady=20)

# Botões para abrir cada tela
ttk.Button(janela, text="Peças", width=25, command=abrir_tela_pecas).pack(pady=5)
ttk.Button(janela, text="Caminhões", width=25, command=abrir_tela_caminhoes).pack(pady=5)
ttk.Button(janela, text="Fornecedores", width=25, command=abrir_tela_fornecedores).pack(pady=5)
ttk.Button(janela, text="Funcionários", width=25, command=abrir_tela_funcionarios).pack(pady=5)
ttk.Button(janela, text="Clientes", width=25, command=abrir_tela_clientes).pack(pady=5)

janela.mainloop()
