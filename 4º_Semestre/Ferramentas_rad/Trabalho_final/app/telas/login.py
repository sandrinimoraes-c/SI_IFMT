"""Classe-base das telas internas: título, descrição e área de conteúdo.

Para criar uma tela: herde de TelaBase, defina `titulo` e `descricao`
e sobrescreva `construir()` (monta os widgets) e `atualizar()`
(recarrega os dados — é chamado toda vez que a tela é aberta).
"""
import customtkinter as ctk


class TelaBase(ctk.CTkFrame):
    titulo = "Tela"
    descricao = ""
    a_fazer = ""

    def __init__(self, master, app):
        super().__init__(master, fg_color="transparent")
        self.app = app

        ctk.CTkLabel(
            self, text=self.titulo, font=ctk.CTkFont(size=24, weight="bold")
        ).pack(anchor="w", padx=30, pady=(25, 0))
        if self.descricao:
            ctk.CTkLabel(
                self, text=self.descricao, text_color="#64748B"
            ).pack(anchor="w", padx=30, pady=(2, 0))

        self.corpo = ctk.CTkFrame(self, corner_radius=12, border_width=1, border_color="#E2E8F0")
        self.corpo.pack(fill="both", expand=True, padx=30, pady=20)
        self.construir()

    def construir(self):
        """Padrão: aviso de tela em construção."""
        ctk.CTkLabel(
            self.corpo,
            text="Em construção",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#94A3B8",
        ).pack(pady=(80, 8))
        if self.a_fazer:
            ctk.CTkLabel(
                self.corpo, text=self.a_fazer, text_color="#94A3B8", justify="center"
            ).pack()

    def atualizar(self):
        """Recarrega os dados da tela (sobrescreva quando precisar)."""
