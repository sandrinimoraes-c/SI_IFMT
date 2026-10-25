
import turtle as t

t.title("Exercício 8 - Quatro círculos")
t.speed(5)

raio = 80
for i in range(4):
    t.circle(raio)
    t.penup()
    t.forward(2 * raio)
    t.pendown()

t.done()
