# py -m pip install flet

import flet as ft #importando a biblioteca com apelido 

def main (page: ft.Page): #define a função principal 
    page.title = "Contador de Mortos" #atribuindo titulo 
    
    contador = ft.Text(value = 0, size = 40) #cria contador e atribui 

    def adicionar (e): #criando uma função
        contador.value = str(int(contador.value) + 1) #Adicionando e convertendo 
        page.update() #atualizando pg
    
    def resetar(e): #função de resetar 
        contador.value = "0" #valor ao chegar a função
        page.update() #atualizando a pg
    
    page.add(
        contador,
        ft.Row(
            [
                ft.ElevatedButton("+1", on_click=adicionar),
                ft.ElevatedButton("0", on_click =resetar),

            ]
        )
    )

ft.app(target=main)