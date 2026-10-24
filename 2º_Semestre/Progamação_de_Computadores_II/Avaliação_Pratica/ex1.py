#Corrija os erros do código abaixo
#São 5 erros 

import flet as ft


def main(page: ft.Page):
    page.title = "Contador de Cliques"

    contador = ft.Text(value="0", size=100)
        
    def incrementar(e): 
        int(contador.value) 
        contador.value = str(int(contador.value))

    def resetar(e):
        contador.value = "0"
        page.update()

    page.add(
        contador,
        ft.Row
            
            [
                ft.ElevatedButton("+1", on_click=incrementar),
                ft.ElevatedButton("Reset", on_click=resetar)
                
            ]
        )
    
ft.app(target=main)