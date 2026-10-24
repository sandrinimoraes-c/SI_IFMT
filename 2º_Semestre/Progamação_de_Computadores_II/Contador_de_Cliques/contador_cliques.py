# Faça as alterações abaixo no contador de cliques:
# * Crie uma função que incremente 2 cliques no contador.
# * Crie uma função de decremento que subtraia 2 do contador.
# * Coloque o contador para começar em 5, em vez de voltar para zero, 
# o botão Reset pode voltar para 1, 10 ou outro valor escolhido.

import flet as ft #importando a biblioteca com apelido 
import random as r

def main (page: ft.Page): #define a função principal 
    page.title = "Contador de cliques" #atribuindo titulo 
    
    contador = ft.Text(value = 5, size = 100, color=ft.Colors.PINK) #cria contador e atribui 
    # contador = ft.Text(value = 0, size = 40)

    def adicionar (e): #criando uma função
        contador.value = str(int(contador.value) + 1) #Adicionando e convertendo 
        page.update() #atualizando pg
    
    def encrementar (e):
        contador.value = str(int(contador.value) + 2)
        page.update()
    
    def decrementar (e):
        contador.value = str(int(contador.value) - 2)
        page.update()
              
    def resetar(e): #função de resetar 
        contador.value = "0" #valor ao chegar a função
        page.update() #atualizando a pg

    def resetarpara10(e): 
        contador.value = "10" 
        page.update()
    
    def sortear (e):    
        
        page.update

    page.add(
        contador,
        ft.Row(
            [
                ft.ElevatedButton("+1", on_click=adicionar),
                ft.ElevatedButton("+2", on_click=encrementar),
                ft.ElevatedButton("-2", on_click=decrementar),
                ft.ElevatedButton("0", on_click =resetar),
                ft.ElevatedButton("Resetar para 10", on_click =resetarpara10),

            ]
        )
    )

ft.app(target=main)