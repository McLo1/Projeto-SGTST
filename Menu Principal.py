"""
Nome do arquivo: Menu Principal.py
Equipe: Marcelo, Layza, Vanderson, Caique.
Turma: G91166
Semestre: 2025.1
"""

import tkinter as tk
from tkinter import ttk
from Caminhão.tela_caminhoes import abrir_tela
from Peças.tela_pecas import abrir_tela_pecas
from Clientes.tela_clientes import abrir_tela_clientes
from Funcionarios.tela_funcionarios import abrir_tela_funcionarios
from Fornecedores.tela_fornecedores import abrir_tela_fornecedores
from Registro_Saida.tela_registro_saida import abrir_tela_saida_caminhao
from Arduino.tela_arduino import abrir_tela_arduino

# Cores e estilo
COR_FUNDO = "#f0f4f8"
COR_BOTAO = "#4a90e2"
COR_TEXTO = "#ffffff"

# Criação da janela principal
janela = tk.Tk()
janela.title("MTV")
janela.geometry("350x500")
janela.configure(bg=COR_FUNDO)

# Estilo dos botões
style = ttk.Style(janela)
style.theme_use("clam")  # pode usar também 'default', 'alt', 'vista'
style.configure("Custom.TButton",
                font=("Segoe UI", 11),
                foreground=COR_TEXTO,
                background=COR_BOTAO,
                padding=10)
style.map("Custom.TButton",
          background=[('active', '#357ABD')])

# Título
label = tk.Label(janela, text="📋 MENU DO SISTEMA", font=("Segoe UI", 18, "bold"), bg=COR_FUNDO, fg="#333")
label.pack(pady=30)

# Container para botões
frame_botoes = tk.Frame(janela, bg=COR_FUNDO)
frame_botoes.pack()

# Função auxiliar para criar botões
def criar_botao(texto, comando):
    ttk.Button(frame_botoes, text=texto, style="Custom.TButton", width=30, command=comando).pack(pady=8)

# Botões
criar_botao("🚛  Caminhões", abrir_tela)
criar_botao("🔧  Peças", abrir_tela_pecas)
criar_botao("👥  Clientes", abrir_tela_clientes)
criar_botao("🧑‍🔧  Funcionários", abrir_tela_funcionarios)
criar_botao("🏢  Fornecedores", abrir_tela_fornecedores)
criar_botao("📤  Registro de Saída", abrir_tela_saida_caminhao)

# Inicia a interface
janela.mainloop()
