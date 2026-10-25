import flet as ft
import random

# ---------------------------------------------------------
# PERGUNTAS DO QUIZ
# ---------------------------------------------------------

QUESTOES = [
    ("Qual é a capital do Brasil?",
     ["São Paulo","Rio de Janeiro","Brasília","Salvador"], 2),
    ("Em que data é comemorada a Independência do Brasil?",
     ["21 de abril de 1822","7 de setembro de 1822","15 de novembro de 1889","1 de maio de 1888"], 1),
    ("Quem proclamou a independência do Brasil?",
     ["Getúlio Vargas","Dom Pedro I","Juscelino Kubitschek","Tiradentes"], 1),
    ("Qual é a maior cidade do Brasil em população?",
     ["Rio de Janeiro","Brasília","Salvador","São Paulo"], 3),
]

# ---------------------------------------------------------
#   APLICAÇÃO FLET (sem UserControl!)
# ---------------------------------------------------------

def main(page: ft.Page):
    page.title = "Quiz Brasil - Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 450
    page.window_height = 700
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # --- Estado do jogo ---
    perguntas = QUESTOES[:]
    random.shuffle(perguntas)
    indice = ft.Ref[int]()
    indice.current = 0
    acertos = ft.Ref[int]()
    acertos.current = 0

    # --- Elementos de texto ---
    titulo = ft.Text("🇧🇷 Quiz: Conhecimentos Gerais sobre o Brasil",
                     size=22, weight="bold", color="#005500", text_align="center")

    progresso = ft.Text(size=16, weight="bold")
    pergunta = ft.Text(size=18, weight="bold", text_align="center")
    resultado = ft.Text(size=22, weight="bold", text_align="center")

    # --- Botões ---
    botoes = []

    def responder(i):
        """Trata a escolha do usuário."""
        correta = perguntas[indice.current][2]

        if i == correta:
            acertos.current += 1

        indice.current += 1
        mostrar_pergunta()

    # Criar botões
    for i in range(4):
        btn = ft.ElevatedButton(
            text="Opção",
            width=300,
            height=50,
            on_click=lambda e, x=i: responder(x),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
                padding=20
            )
        )
        botoes.append(btn)

    # ---------------------------------------------------------
    #   Exibe pergunta atual
    # ---------------------------------------------------------
    def mostrar_pergunta():
        if indice.current >= len(perguntas):
            return mostrar_resultado()

        pergunta_atual, alternativas, _ = perguntas[indice.current]

        progresso.value = f"Pergunta {indice.current + 1} de {len(perguntas)}"
        pergunta.value = pergunta_atual

        letras = ["A", "B", "C", "D"]
        for i in range(4):
            botoes[i].text = f"{letras[i]} - {alternativas[i]}"

        page.update()

    # ---------------------------------------------------------
    #   Resultado final
    # ---------------------------------------------------------
    def mostrar_resultado():
        page.controls.clear()
        resultado.value = (
            f"Você acertou {acertos.current} de {len(perguntas)} perguntas!"
        )

        page.add(
            ft.Column([
                ft.Text("🎉 Quiz Finalizado!", size=26, weight="bold"),
                resultado,
                ft.ElevatedButton(
                    "Jogar novamente",
                    width=250,
                    height=50,
                    on_click=lambda e: reiniciar()
                )
            ],
            alignment="center",
            spacing=20)
        )
        page.update()

    # ---------------------------------------------------------
    #   Reiniciar jogo
    # ---------------------------------------------------------
    def reiniciar():
        perguntas[:] = QUESTOES[:]
        random.shuffle(perguntas)
        indice.current = 0
        acertos.current = 0

        page.controls.clear()
        page.add(layout_quiz)
        mostrar_pergunta()

    # ---------------------------------------------------------
    # Layout principal
    # ---------------------------------------------------------
    layout_quiz = ft.Column(
        [
            titulo,
            progresso,
            pergunta,
            ft.Column(botoes, spacing=10, horizontal_alignment="center")
        ],
        alignment="center",
        spacing=20
    )

    page.add(layout_quiz)
    mostrar_pergunta()


ft.app(target=main)