"""Janela principal: alterna entre a tela de login e o sistema (menu lateral + telas)."""
import customtkinter as ctk

from telas.adocoes import TelaAdocoes
from telas.adotantes import TelaAdotantes
from telas.animais import TelaAnimais
from telas.login import TelaLogin
from telas.painel import TelaPainel
from telas.relatorios import TelaRelatorios
from telas.resgates import TelaResgates
from telas.saude import TelaSaude

# (chave, texto do botão, classe da tela) — a ordem define a ordem do menu
MENU = [
    ("painel", "Painel", TelaPainel),
    ("animais", "Animais", TelaAnimais),
    ("saude", "Saúde", TelaSaude),
    ("resgates", "Resgates", TelaResgates),
    ("adotantes", "Adotantes", TelaAdotantes),
    ("adocoes", "Adoções", TelaAdocoes),
    ("relatorios", "Relatórios", TelaRelatorios),
]

COR_ATIVA = "#2563EB"
COR_INATIVA = "transparent"


class Sistema(ctk.CTkFrame):
    """Tela principal depois do login: menu lateral à esquerda e conteúdo à direita."""

    def __init__(self, master, app):
        super().__init__(master, fg_color="transparent")
        self.app = app
        self.telas = {}      # telas já criadas (criadas só na primeira visita)
        self.botoes = {}
        self.atual = None

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        barra = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color="#F1F5F9")
        barra.grid(row=0, column=0, sticky="nsew")
        barra.grid_propagate(False)

        ctk.CTkLabel(
            barra, text="Animais de Rua", font=ctk.CTkFont(size=18, weight="bold")
        ).pack(padx=20, pady=(25, 0), anchor="w")
        ctk.CTkLabel(barra, text="Pontes e Lacerda", text_color="#64748B").pack(
            padx=20, pady=(0, 20), anchor="w"
        )

        for chave, texto, _ in MENU:
            botao = ctk.CTkButton(
                barra, text=texto, anchor="w", height=38, corner_radius=8,
                fg_color=COR_INATIVA, text_color="#1E293B", hover_color="#E2E8F0",
                command=lambda c=chave: self.navegar(c),
            )
            botao.pack(fill="x", padx=12, pady=2)
            self.botoes[chave] = botao

        rodape = ctk.CTkFrame(barra, fg_color="transparent")
        rodape.pack(side="bottom", fill="x", padx=12, pady=20)
        ctk.CTkLabel(
            rodape, text=f"{app.usuario['nome']}\n({app.usuario['perfil']})",
            text_color="#64748B", justify="left",
        ).pack(anchor="w", padx=8, pady=(0, 10))
        ctk.CTkButton(
            rodape, text="Sair da conta", height=36, fg_color="#E2E8F0",
            text_color="#1E293B", hover_color="#CBD5E1", command=app.mostrar_login,
        ).pack(fill="x")

        self.area = ctk.CTkFrame(self, fg_color="transparent")
        self.area.grid(row=0, column=1, sticky="nsew")
        self.navegar("painel")

    def navegar(self, chave: str):
        if self.atual:
            self.telas[self.atual].pack_forget()
            self.botoes[self.atual].configure(fg_color=COR_INATIVA, text_color="#1E293B")

        if chave not in self.telas:
            classe = next(c for k, _, c in MENU if k == chave)
            self.telas[chave] = classe(self.area, self.app)

        tela = self.telas[chave]
        tela.pack(fill="both", expand=True)
        tela.atualizar()
        self.botoes[chave].configure(fg_color=COR_ATIVA, text_color="#FFFFFF")
        self.atual = chave


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Animais de Rua e Adoção - Pontes e Lacerda")
        self.geometry("1100x680")
        self.minsize(900, 560)
        self.usuario = None
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)
        self.mostrar_login()

    def _trocar(self, frame_classe, *args):
        for widget in self.container.winfo_children():
            widget.destroy()
        frame_classe(self.container, self, *args).pack(fill="both", expand=True)

    def mostrar_login(self):
        self.usuario = None
        self._trocar(TelaLogin)

    def mostrar_sistema(self, usuario: dict):
        self.usuario = usuario
        self._trocar(Sistema)
