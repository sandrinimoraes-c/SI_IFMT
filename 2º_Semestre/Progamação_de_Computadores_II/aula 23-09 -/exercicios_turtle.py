
# Lista de exercícios Turtle — Programação II
# Docente: Letícia Ferreira
# Solução em Python (turtle)

import turtle as t

# ---------- utilidades ----------
def setup():
    t.reset()
    t.title("Lista de exercícios Turtle")
    t.speed(0)          # mais rápido
    t.hideturtle()
    t.penup()

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def desenha_circulo(raio):
    t.circle(raio)

# ---------- 1. linha horizontal ----------
def ex1_linha_horizontal():
    move_to(-330, 260)
    t.setheading(0)     # aponta para Leste
    t.pendown()
    t.forward(200)

# ---------- 2. linha vertical ----------
def ex2_linha_vertical():
    move_to(-70, 260)
    t.setheading(90)    # aponta para Norte
    t.pendown()
    t.forward(200)

# ---------- 3. quadrado (sem for) ----------
def ex3_quadrado_sem_for(lado=100):
    move_to(210, 260)
    t.setheading(0)
    t.pendown()
    t.forward(lado); t.right(90)
    t.forward(lado); t.right(90)
    t.forward(lado); t.right(90)
    t.forward(lado); t.right(90)

# ---------- 4. triângulo semelhante ao ilustrado ----------
# Dica: triângulo equilátero -> ângulos internos = 60°, externos = 120°.
def ex4_triangulo(lado=120):
    move_to(-330, 120)
    t.setheading(0)
    t.pendown()
    t.forward(lado); t.right(120)
    t.forward(lado); t.right(120)
    t.forward(lado); t.right(120)

# ---------- 5. triângulo com ciclo for ----------
def ex5_triangulo_for(lado=120):
    move_to(-60, 120)
    t.setheading(0)
    t.pendown()
    for _ in range(3):
        t.forward(lado)
        t.right(120)  # ângulo externo de 120°

# ---------- 6. quadrado com ciclo for ----------
def ex6_quadrado_for(lado=100):
    move_to(210, 120)
    t.setheading(0)
    t.pendown()
    for _ in range(4):
        t.forward(lado)
        t.right(90)

# ---------- 7. círculo com raio 200 ----------
def ex7_circulo_raio_200():
    move_to(-340, -60)
    t.setheading(0)
    t.pendown()
    t.circle(200)

# ---------- 8. quatro círculos tangentes ----------
def ex8_quatro_circulos(raio=80, quantidade=4):
    move_to(-60, -60 - raio)  # desce para o ponto onde a turtle começa a traçar circles
    t.setheading(0)
    for i in range(quantidade):
        t.pendown()
        t.circle(raio)
        t.penup()
        t.forward(2 * raio)   # avança exatamente o diâmetro para ficarem tangentes

# ---------- 9. quatro círculos coloridos (fillcolor, begin_fill, end_fill) ----------
def ex9_circulos_pintados(raio=80):
    cores = ["black", "lightgray", "silver", "dimgray"]
    move_to(-60, -280 - raio)
    t.setheading(0)
    for cor in cores:
        t.fillcolor(cor)
        t.begin_fill()
        t.pendown()
        t.circle(raio)
        t.end_fill()
        t.penup()
        t.forward(2 * raio)

# ---------- 10. pentágono regular ----------
# Em um polígono regular de n lados, o ângulo externo = 360/n.
# Para pentágono: externo = 72°, interno = 108°.
def ex10_pentagono(lado=100):
    move_to(260, -40)
    t.setheading(0)
    t.pendown()
    for _ in range(5):
        t.forward(lado)
        t.right(72)

# ---------- execução ----------
setup()
ex1_linha_horizontal()
ex2_linha_vertical()
ex3_quadrado_sem_for()
ex4_triangulo()
ex5_triangulo_for()
ex6_quadrado_for()
ex7_circulo_raio_200()
ex8_quatro_circulos()
ex9_circulos_pintados()
ex10_pentagono()

t.done()

t.done()