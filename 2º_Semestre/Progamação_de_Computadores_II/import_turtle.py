import turtle as t


def quadrado():
    for _ in range(4):
        t.forward(100)
        t.left(90)

def retangulo():
    for _ in range(2):
        t.forward(150)
        t.left(90)
        t.forward(80)
        t.left(90)

def triangulo():
    for _ in range(3):
        t.forward(120)
        t.left(120)

def circulo():
    t.circle(60)

def pentagono():
    for _ in range(5):
        t.forward(100)
        t.left(72)

def hexagono():
    for _ in range(6):
        t.forward(80)
        t.left(60)

def losango():
    for _ in range(2):
        t.forward(100)
        t.left(60)
        t.forward(100)
        t.left(120)

def trapezio():
    t.forward(120)
    t.left(60)
    t.forward(60)
    t.left(120)
    t.forward(100)
    t.left(60)
    t.forward(60)
    t.left(120)

def estrela():
    for _ in range(5):
        t.forward(150)
        t.right(144)

def oval():
    for _ in range(2):
        t.circle(60, 90)   # raio 60, arco 90°
        t.circle(30, 90)   # raio 30, arco 90°


# Perguntas e respostas

perguntas = [
    ("Qual forma geométrica tem 4 lados iguais?", "quadrado", quadrado),
    ("Qual forma geométrica tem lados opostos iguais?", "retangulo", retangulo),
    ("Qual forma geométrica tem 3 lados?", "triangulo", triangulo),
    ("Qual forma geométrica não tem lados?", "circulo", circulo),
    ("Qual forma geométrica tem 5 lados iguais?", "pentagono", pentagono),
    ("Qual forma geométrica tem 6 lados iguais?", "hexagono", hexagono),
    ("Qual forma geométrica parece um quadrado inclinado?", "losango", losango),
    ("Qual forma geométrica tem apenas um par de lados paralelos?", "trapezio", trapezio),
    ("Qual forma geométrica tem 5 pontas?", "estrela", estrela),
    ("Qual forma geométrica parece um círculo alongado?", "oval", oval)
]


# Jogo

tela = t.Screen()
tela.title("Jogo Educativo de Formas Geométricas")
tela.setup(width=900, height=700)

pontos = 0
for pergunta, resposta_correta, desenho in perguntas:
    t.clear()
    t.penup()
    t.goto(-250, 250)
    t.write(pergunta, font=("Arial", 16, "bold"))
    t.hideturtle()
    t.goto(0, 0)
    t.pendown()
    desenho()

    resposta = tela.textinput("Pergunta", "Digite sua resposta:").lower()

    if resposta == resposta_correta:
        pontos += 1
        t.penup()
        t.goto(0, -200)
        t.write("✔ Acertou!", align="center", font=("Arial", 18, "bold"))
    else:
        t.penup()
        t.goto(0, -200)
        t.write(f"✘ Errou! Era {resposta_correta}.", align="center", font=("Arial", 18, "bold"))


# Resultado
t.clear()
t.penup()
t.goto(0, 0)
t.write(f"Fim de jogo! Você acertou {pontos}/{len(perguntas)}.", align="center", font=("Arial", 22, "bold"))

t.done()