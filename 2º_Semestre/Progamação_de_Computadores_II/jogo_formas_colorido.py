
import turtle as t


t.title("Jogo de Formas Geométricas")
t.speed(0) # mais rápido
t.pensize(3) # contorno mais vísivel
t.hideturtle() # ocultar tartaruga

# Paleta de cores por forma (contorno, preenchimento)
CORES = {
    "quadrado":  ("#1e293b", "#93c5fd"),
    "retangulo": ("#0f766e", "#99f6e4"),
    "triangulo": ("#7c2d12", "#fed7aa"),
    "circulo":   ("#1d4ed8", "#bfdbfe"),
    "pentagono": ("#7c3aed", "#ddd6fe"),
    "hexagono":  ("#065f46", "#a7f3d0"),
    "losango":   ("#a16207", "#fde68a"),
    "trapezio":  ("#9333ea", "#e9d5ff"),
    "estrela":   ("#b91c1c", "#fecaca"),
    "oval":      ("#2563eb", "#bfdbfe"),
}

# Funções de desenho 
def quadrado():
    for i in range(4):
        t.forward(120); 
        t.left(90)

def retangulo():
    for i in range(2):
        t.forward(170); 
        t.left(90); 
        t.forward(100); 
        t.left(90)

def triangulo():
    for i in range(3):
        t.forward(140); 
        t.left(120)

def circulo():
    t.circle(70)

def pentagono():
    for i in range(5):
        t.forward(110); 
        t.left(72)

def hexagono():
    for i_ in range(6):
        t.forward(95); 
        t.left(60)

def losango():
    t.left(30)
    for i in range(2):
        t.forward(120); 
        t.left(120); 
        t.forward(120); 
        t.left(60)
    t.right(30)

def trapezio():
    t.forward(230); 
    t.left(120); 
    t.forward(90); 
    t.left(60)
    t.forward(140); 
    t.left(60); 
    t.forward(90); 
    t.left(120)

def estrela():
    for i in range(5):
        t.forward(180); 
        t.right(144)


def oval():
    for i in range(2):
        t.circle(80, 90); 
        t.circle(40, 90)

# Mapa nome->função
FORMAS = {
    "quadrado": quadrado, 
    "retangulo": retangulo, 
    "triangulo": triangulo, 
    "circulo": circulo,
    "pentagono": pentagono, 
    "hexagono": hexagono, 
    "losango": losango, 
    "trapezio": trapezio,
    "estrela": estrela, 
    "oval": oval,
}

# Perguntas
PERGUNTAS = [
    ("Qual forma geométrica tem 4 lados iguais?", "quadrado", "quadrado"),
    ("Qual forma geométrica tem lados opostos iguais?", "retangulo", "retangulo"),
    ("Qual forma geométrica tem 3 lados?", "triangulo", "triangulo"),
    ("Qual forma geométrica não tem lados?", "circulo", "circulo"),
    ("Qual forma geométrica tem 5 lados iguais?", "pentagono", "pentagono"),
    ("Qual forma geométrica tem 6 lados iguais?", "hexagono", "hexagono"),
    ("Qual forma geométrica possui quatro lados iguais e ângulos opostos iguais?", "losango", "losango"),
    ("Qual forma geométrica tem apenas um par de lados paralelos?", "trapezio", "trapezio"),
    ("Qual forma geométrica tem 5 pontas?", "estrela", "estrela"),
    ("Qual forma geométrica parece um círculo alongado?", "oval", "oval"),
]

# Tela
tela = t.Screen()
tela.setup(900, 700)
tela.bgcolor("#fcfeff")

pontos = 0

# percorre todas as perguntas do jogo
for pergunta, resposta, nome in PERGUNTAS:
    t.clear()

    # pergunta no topo
    t.penup(); 
    t.goto(-400, 270); 
    t.color("#0f172a")
    t.write(pergunta, font=("Arial", 16, "bold"))

    # desenha forma no centro
    t.color(*CORES.get(nome, ("black", "lightgray")))
    t.penup(); 
    t.goto(0, 100); 
    t.setheading(0); 
    t.pendown()
    t.begin_fill(); 
    FORMAS[nome](); t.end_fill()

    # resposta (comparação)
    r = tela.textinput("Pergunta", "Digite sua resposta:")

    acertou = (r or "").strip().lower() == resposta
    t.penup(); #reposicionar 
    t.goto(0, -260)

    if acertou:
        pontos += 1; t.color("#065f46")
        t.write("✔ Acertou!", align="center", font=("Arial", 20, "bold"))
    else:
        t.color("#9f1239")
        t.write(f"✘ Errou! Era {resposta}.", align="center", font=("Arial", 20, "bold"))


t.clear(); 
t.penup(); 
t.color("#0f172a"); 
t.goto(0, 20)
t.write(f"Fim de jogo! Você acertou {pontos}/{len(PERGUNTAS)}.", align="center", font=("Arial", 24, "bold"))
t.goto(0, -30)
t.write("Feche a janela para encerrar.", align="center", font=("Arial", 14))

t.done()