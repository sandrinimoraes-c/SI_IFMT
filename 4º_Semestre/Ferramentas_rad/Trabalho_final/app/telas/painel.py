import customtkinter as ctk
from mysql.connector import Error

from database import autenticar


class TelaLogin(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master, fg_color="transparent")
        self.app = app

        cartao = ctk.CTkFrame(self, corner_radius=12, border_width=1, border_color="#E2E8F0")
        cartao.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(
            cartao, text="Animais de Rua e Adoção", font=ctk.CTkFont(size=22, weight="bold")
        ).pack(padx=50, pady=(35, 2))
        ctk.CTkLabel(
            cartao, text="Pontes e Lacerda - MT", text_color="#64748B"
        ).pack(pady=(0, 25))

        self.ent_login = ctk.CTkEntry(cartao, width=280, height=40, placeholder_text="Usuário")
        self.ent_login.pack(padx=40, pady=(0, 12))
        self.ent_senha = ctk.CTkEntry(
            cartao, width=280, height=40, placeholder_text="Senha", show="*"
        )
        self.ent_senha.pack(padx=40, pady=(0, 8))

        self.lbl_erro = ctk.CTkLabel(cartao, text="", text_color="#DC2626")
        self.lbl_erro.pack(pady=(0, 8))

        botoes = ctk.CTkFrame(cartao, fg_color="transparent")
        botoes.pack(padx=40, pady=(0, 35))
        ctk.CTkButton(botoes, text="Entrar", width=135, height=40, command=self.entrar).pack(
            side="left", padx=(0, 10)
        )
        ctk.CTkButton(
            botoes, text="Sair", width=135, height=40,
            fg_color="#E2E8F0", text_color="#1E293B", hover_color="#CBD5E1",
            command=app.destroy,
        ).pack(side="left")

        for campo in (self.ent_login, self.ent_senha):
            campo.bind("<Return>", lambda e: self.entrar())
        self.after(150, self.ent_login.focus)

    def entrar(self):
        login = self.ent_login.get().strip()
        senha = self.ent_senha.get()

        if not login or not senha:
            self.lbl_erro.configure(text="Preencha usuário e senha.")
            return
        try:
            usuario = autenticar(login, senha)
        except Error:
            self.lbl_erro.configure(text="Não foi possível acessar o banco de dados.")
            return

        if not usuario:
            self.lbl_erro.configure(text="Usuário ou senha incorretos.")
            self.ent_senha.delete(0, "end")
            return
        self.app.mostrar_sistema(usuario)
