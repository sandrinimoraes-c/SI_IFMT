
import turtle as t

t.title("Exercício 9 - Quatro círculos coloridos")
t.speed(10)

raio = 80
cores = ["blue", "red", "green", "yellow"]
for cor in cores:
    t.fillcolor(cor)
    t.begin_fill()
    t.circle(raio)
    t.end_fill()
    t.penup()
    t.forward(2 * raio)
    t.pendown()

t.done()
