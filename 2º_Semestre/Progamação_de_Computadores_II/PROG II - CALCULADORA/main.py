# Projeto calculadora com Flet - Programação II
# pip install flet

import flet as ft

def main(tela: ft.Page):

    # Parte 1 – Configuração inicial da tela
    
    tela.title = "Calculadora - Programação II"
    tela.bgcolor = "#AF187D"           # cor de fundo da janela
    tela.window_width = 380            # largura da janela
    tela.window_height = 520           # altura da janela
    tela.window_resizable = False

        # Parte 2 – Variáveis e Visor
    
    expressao = ""  # guarda a expressão atual ao longo do uso da calc

    visor = ft.Text(
        value="0",
        color=ft.Colors.WHITE,
        size=32,
        text_align="right",
        no_wrap=True,
        selectable=False,
    )

        # Parte 3 – Função de clique dos botões
    
    def clicar(botao: ft.ControlEvent):
        nonlocal expressao
        valor = botao.control.text

        if valor == "AC":
            expressao = ""
            visor.value = "0"
        
        elif valor == "⌫":   
            expressao = expressao[:-1]  # remove último caractere
            visor.value = expressao if expressao else "0"

        elif valor == "=":
            try:
                # eval() executa código dentro de uma string.
                # Aqui calculamos a expressão matemática digitada.
                # resultado = eval(expressao) e
                # expressao = str(resultado) ou
                expressao=str(eval(expressao))
                visor.value = expressao
            
            # except Exception: ou   
            except:
            
                visor.value = "Erro"
                expressao = ""
                    
        else:
            # acrescente o valor pressionado
            expressao += valor
            visor.value = expressao

        tela.update()

        # Parte 4 – Função para criar botões
    
    def botao(texto, cor_fundo, cor_texto, expand=1):
        return ft.ElevatedButton(
            text=texto,
            expand=expand,
            style=ft.ButtonStyle(
                bgcolor=cor_fundo,
                color=cor_texto,
                shape=ft.RoundedRectangleBorder(radius=12),
            ),
            on_click=clicar,
        )
    
    # Parte 5 – Organizar layout e rodar o app
    # Container > Column > Rows (visor + linhas de botões)
    
    tela.add(
        ft.Container(
            width=350,
            bgcolor=ft.Colors.BLACK,
            border_radius=ft.border_radius.all(20),
            padding=20,
            content=ft.Column(
                spacing=12,
                controls=[
                    ft.Row(controls=[visor], alignment="end"),
                    # padrão para formar o teclado da calculadora.
                    ft.Row(
                        controls=[
                            botao("AC", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK),
                            botao("⌫", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK),
                            botao("%", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK),
                            botao("/", ft.Colors.ORANGE, ft.Colors.WHITE),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            botao("7", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK),
                            botao("8", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK),
                            botao("9", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK),
                            botao("*", ft.Colors.ORANGE, ft.Colors.WHITE),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            botao("4", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK),
                            botao("5", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK),
                            botao("6", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK),
                            botao("-", ft.Colors.ORANGE, ft.Colors.WHITE),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            botao("1", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK),
                            botao("2", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK),
                            botao("3", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK),
                            botao("+", ft.Colors.ORANGE, ft.Colors.WHITE),
                        ]
                    ),
                    ft.Row(
                        controls=[
                            botao("0", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK, expand=2),
                            botao(".", ft.Colors.BLUE_GREY_100, ft.Colors.BLACK),
                            botao("=", ft.Colors.ORANGE, ft.Colors.WHITE),
                        ]
                    ),
                ],
            ),
        )
    )


if __name__ == "__main__":
    # Executar
    ft.app(target=main)
