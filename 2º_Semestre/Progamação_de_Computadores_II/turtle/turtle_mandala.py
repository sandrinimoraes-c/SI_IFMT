# turtle_mandala.py
# Mandala geométrica simples usando apenas 'for'
import turtle as t

t.bgcolor("black")
t.colormode(255)

pen = t.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

colors = [(255, 99, 71), (255, 215, 0), (50, 205, 50), (64, 224, 208), (65, 105, 225), (186, 85, 211)]

# Roseta: desenha um pequeno polígono e gira um pouco; repete
for i in range(72):              # 72 * 5° = 360°
    pen.pencolor(colors[i % len(colors)])
    for _ in range(6):           # hexágono
        pen.forward(120)
        pen.right(60)
    pen.right(5)
    pen.forward(5)

# Pontos ao redor para dar "textura"
pen.penup()
for r in range(40, 181, 10):
    pen.home()
    pen.sety(-r)
    pen.pendown()
    pen.pencolor(255, 255, 255)
    for _ in range(36):
        pen.dot(3)
        pen.circle(r, 10)

t.done()
