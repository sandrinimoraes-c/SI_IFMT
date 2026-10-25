# turtle_paint_app.py
# Aplicativo simples de desenho com Turtle
# Controles:
#  🡩: andar para frente
#  🡫: andar para trás
#  🡨/🡪: girar esquerda/direita
#  Espaço: alterna caneta (abaixa/levanta)
#  C: limpar tela
#  + / - : aumentar/diminuir a espessura
#  1..6: cores (preto, vermelho, verde, azul, amarelo, magenta)
#  P: carimbar a tartaruga
#  S: salvar desenho como EPS (drawing.eps)

import turtle as t

# ----- Configuração inicial -----
screen = t.Screen()
screen.title("Turtle Paint - by ChatGPT")
screen.setup(width=900, height=700)
screen.bgcolor("white")

pen = t.Turtle(visible=True)
pen.shape("turtle")
pen.speed(0)
pen.color("black")
pen.pensize(3)

# Estado
step = 20

def go_forward():
    pen.forward(step)

def go_back():
    pen.backward(step)

def turn_left():
    pen.left(15)

def turn_right():
    pen.right(15)

def toggle_pen():
    if pen.isdown():
        pen.penup()
        screen.title("Turtle Paint (PEN UP) - Espaço alterna")
    else:
        pen.pendown()
        screen.title("Turtle Paint (PEN DOWN) - Espaço alterna")

def clear_screen():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

def thicker():
    pen.pensize(min(pen.pensize() + 1, 30))

def thinner():
    pen.pensize(max(pen.pensize() - 1, 1))

def set_color(color):
    pen.color(color)

def stamp_turtle():
    pen.stamp()

def save_eps():
    # Salva a tela em EPS (funciona em ambientes com Tkinter)
    try:
        cv = screen.getcanvas()
        cv.postscript(file="drawing.eps")
        print("Desenho salvo como drawing.eps (formato EPS).")
    except Exception as e:
        print("Não foi possível salvar o arquivo EPS:", e)

# Bindings de teclado
screen.listen()
screen.onkeypress(go_forward, "Up")
screen.onkeypress(go_back, "Down")
screen.onkeypress(turn_left, "Left")
screen.onkeypress(turn_right, "Right")
screen.onkeypress(toggle_pen, "space")
screen.onkeypress(clear_screen, "c")
screen.onkeypress(thicker, "plus")
screen.onkeypress(thinner, "minus")
screen.onkeypress(lambda: set_color("black"), "1")
screen.onkeypress(lambda: set_color("red"), "2")
screen.onkeypress(lambda: set_color("green"), "3")
screen.onkeypress(lambda: set_color("blue"), "4")
screen.onkeypress(lambda: set_color("yellow"), "5")
screen.onkeypress(lambda: set_color("magenta"), "6")
screen.onkeypress(stamp_turtle, "p")
screen.onkeypress(save_eps, "s")

# Mensagem inicial
print("""
Turtle Paint
Controles:
  ↑ / ↓  : mover
  ← / →  : girar
  Espaço : alternar caneta (abaixa/levanta)
  C      : limpar tela
  +  / - : espessura
  1..6   : cores (1=preto, 2=vermelho, 3=verde, 4=azul, 5=amarelo, 6=magenta)
  P      : carimbar
  S      : salvar como drawing.eps
""")

# Mantém a janela aberta
t.done()
