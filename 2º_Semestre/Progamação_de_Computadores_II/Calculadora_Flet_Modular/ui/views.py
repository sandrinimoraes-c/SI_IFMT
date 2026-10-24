
import flet as ft
from .buttons import BUTTON_LAYOUT
from ..calc.state import CalcState
from .controller import Controller

def build_app(page: ft.Page):
    page.title = "Calculadora (Flet Modular)"
    page.window_width = 330
    page.window_height = 480
    page.window_resizable = False

    display = ft.TextField(
        value="",
        text_align=ft.TextAlign.RIGHT,
        read_only=True,
        border=ft.InputBorder.OUTLINE,
        border_radius=8,
        height=70,
        text_size=28,
    )

    def set_display(txt: str):
        display.value = txt
        display.update()

    state = CalcState()
    ctrl = Controller(state, set_display)

    rows = []
    for row in BUTTON_LAYOUT:
        r = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text=label,
                    data=label,
                    on_click=lambda e: ctrl.press(e.control.data),
                    expand=1,
                    height=60,
                )
                for label in row
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            spacing=8,
        )
        rows.append(r)

    page.add(
        ft.Container(padding=10, content=display),
        ft.Column(rows, spacing=8, expand=True, scroll=ft.ScrollMode.AUTO),
    )