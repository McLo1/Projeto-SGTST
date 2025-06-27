"""
Nome do arquivo: Menu Principal.py
Equipe: Marcelo, Layza, Vanderson, Caique.
Turma: G91166
Semestre: 2025.1
"""

import tkinter as tk
from tkinter import scrolledtext
import threading
import random
import time

def gerar_dados_fake(texto_area):
    while True:
        temperatura = random.randint(20, 50)
        gas = random.randint(100, 800)
        presenca = random.choice([0, 1])
        linha = f" Temperatura: {temperatura} Gás: {gas} Presenca: {presenca}"

        texto_area.insert(tk.END, linha + "\n")
        texto_area.yview(tk.END)
        time.sleep(1)

def abrir_tela_arduino_fake():
    janela = tk.Toplevel()
    janela.title("🔌 Simulação Arduino (Fake)")
    janela.geometry("500x400")
    janela.configure(bg="#f0f4f8")

    titulo = tk.Label(janela, text="🧪 Simulador de Dados Arduino", font=("Segoe UI", 16, "bold"), bg="#f0f4f8", fg="#333")
    titulo.pack(pady=10)

    texto_area = scrolledtext.ScrolledText(janela, wrap=tk.WORD, font=("Consolas", 10))
    texto_area.pack(expand=True, fill='both', padx=10, pady=10)

    thread = threading.Thread(target=gerar_dados_fake, args=(texto_area,), daemon=True)
    thread.start()
