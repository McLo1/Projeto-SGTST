"""
Nome do arquivo: Menu Principal.py
Equipe: Marcelo, Layza, Vanderson, Caique.
Turma: G91166
Semestre: 2025.1
"""

import tkinter as tk
from tkinter import scrolledtext
import serial
import threading

def ler_dados(serial_port, texto_area):
    try:
        with serial.Serial(serial_port, 9600, timeout=1) as arduino:
            while True:
                try:
                    linha = arduino.readline().decode('utf-8').strip()
                    if linha:
                        texto_area.insert(tk.END, linha + "\n")
                        texto_area.yview(tk.END)
                except Exception as e:
                    texto_area.insert(tk.END, f"[ERRO NA LEITURA] {e}\n")
    except Exception as e:
        texto_area.insert(tk.END, f"[ERRO NA CONEXÃO] {e}\n")

def abrir_tela_arduino():
    janela = tk.Toplevel()
    janela.title("📟 Monitoramento Arduino")
    janela.geometry("500x400")
    janela.configure(bg="#f0f4f8")

    titulo = tk.Label(janela, text="🔍 Leitura em Tempo Real", font=("Segoe UI", 14, "bold"), bg="#f0f4f8", fg="#333")
    titulo.pack(pady=10)

    texto_area = scrolledtext.ScrolledText(janela, wrap=tk.WORD, font=("Consolas", 10))
    texto_area.pack(expand=True, fill='both', padx=10, pady=10)

    thread = threading.Thread(target=ler_dados, args=('COM3', texto_area), daemon=True)
    thread.start()
