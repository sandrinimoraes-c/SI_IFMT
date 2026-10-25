# turtle_blackhole.py
# Espiral que lembra um "buraco negro" usando apenas 'for'
import turtle as t

t.bgcolor("black")
t.colormode(255)

pen = t.Turtle()
pen.hideturtle()
pen.speed(0)

# Passo inicial grande que diminui a cada volta -> espiral "puxando" para o centro
step = 18.0
pen.pensize(2)

# Paleta azul-roxa luminosa
def color_grad(k):
    # k vai de 0..239
    r = int(80 * (1 - k/239))    # diminui
    g = int(30 * (1 - k/239))
    b = 180
    return (r, g, b)

for k in range(240):
    pen.pencolor(color_grad(k))
    pen.forward(step)
    pen.right(18)        # ângulo fixo dá um turbilhão
    step *= 0.985        # contrai aos poucos
    if k % 12 == 0:
        # espessura cresce levemente, simulando densidade
        pen.pensize(min(2 + k//24, 8))

# "disco de acreção" com pequenos arcos pontilhados
pen.penup()
pen.sety(-40)
pen.pendown()
pen.pencolor(200, 200, 200)
for _ in range(36):
    pen.circle(40, 8)
    pen.penup(); pen.forward(3); pen.pendown()

t.done()
