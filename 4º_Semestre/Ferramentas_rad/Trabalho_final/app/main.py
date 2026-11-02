"""Ponto de entrada. Execute dentro da pasta app:  python3 main.py"""
import tkinter as tk
from tkinter import messagebox

import customtkinter as ctk
from mysql.connector import Error

from app import App
from database import inicializar_banco


def main():
    try:
        inicializar_banco()
    except Error as erro:
        raiz = tk.Tk()
        raiz.withdraw()
        messagebox.showerror(
            "Erro de conexão",
            f"Não foi possível acessar o MySQL:\n{erro}\n\n"
            "Confira se o servidor está ligado e se a variável DB_PASSWORD está definida.",
        )
        raiz.destroy()
        return

    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("blue")
    App().mainloop()


if __name__ == "__main__":
    main()
