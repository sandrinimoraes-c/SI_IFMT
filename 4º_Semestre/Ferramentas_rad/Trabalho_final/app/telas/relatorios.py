import customtkinter as ctk

from database import consultar
from telas.base import TelaBase

SQL_RESUMO = """
SELECT
    (SELECT COUNT(*) FROM animais)                                         AS total,
    (SELECT COUNT(*) FROM animais WHERE status = 'disponivel_adocao')      AS disponiveis,
    (SELECT COUNT(*) FROM animais WHERE status = 'adotado')                AS adotados,
    (SELECT COUNT(*) FROM resgates WHERE situacao IN ('aberta','em_andamento')) AS resgates_abertos
"""


class TelaPainel(TelaBase):
    titulo = "Painel"
    descricao = "Resumo geral do abrigo"

    def construir(self):
        self.valores = {}
        grade = ctk.CTkFrame(self.corpo, fg_color="transparent")
        grade.pack(fill="x", padx=20, pady=30)

        cartoes = [
            ("total", "Animais cadastrados"),
            ("disponiveis", "Disponíveis para adoção"),
            ("adotados", "Adotados"),
            ("resgates_abertos", "Resgates em aberto"),
        ]
        for coluna, (chave, rotulo) in enumerate(cartoes):
            grade.grid_columnconfigure(coluna, weight=1)
            cartao = ctk.CTkFrame(grade, corner_radius=10, fg_color="#F1F5F9")
            cartao.grid(row=0, column=coluna, padx=8, sticky="nsew")
            valor = ctk.CTkLabel(cartao, text="-", font=ctk.CTkFont(size=34, weight="bold"))
            valor.pack(pady=(18, 0))
            ctk.CTkLabel(cartao, text=rotulo, text_color="#64748B").pack(pady=(0, 18))
            self.valores[chave] = valor

    def atualizar(self):
        dados = consultar(SQL_RESUMO)[0]
        for chave, rotulo in self.valores.items():
            rotulo.configure(text=str(dados[chave]))
