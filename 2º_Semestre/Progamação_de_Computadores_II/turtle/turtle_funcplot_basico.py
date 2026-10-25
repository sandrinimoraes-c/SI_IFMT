# turtle_funcplot_basico.py
# Plotador MUITO simples com Turtle (ideal para começar)
# Teclas: 1=sin(x), 2=x**2/5, 3=0.7*x - 2, C=limpar/replotar
# Escala Y pode ser ajustada em SCALE para "caber" na tela.
import turtle as t
import math

WIDTH, HEIGHT = 900, 600
SCALE_Y = 40  # quanto 1 unidade em y "vale" em pixels
STEP = 1      # passo em pixels para o traço do gráfico

screen = t.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("FuncPlot Básico - Turtle")
screen.tracer(0, 0)

pen = t.Turtle(visible=False)
pen.speed(0)

# ----- utilidades -----
def draw_axes():
    pen.clear()
    pen.pensize(2)
    pen.pencolor("black")
    # eixo X
    pen.penup(); pen.goto(-WIDTH//2, 0); pen.pendown(); pen.goto(WIDTH//2, 0)
    # eixo Y
    pen.penup(); pen.goto(0, -HEIGHT//2); pen.pendown(); pen.goto(0, HEIGHT//2)
    # grade simples a cada 100 px
    pen.pensize(1); pen.pencolor("#dddddd")
    for x in range(-WIDTH//2, WIDTH//2+1, 100):
        pen.penup(); pen.goto(x, -HEIGHT//2); pen.pendown(); pen.goto(x, HEIGHT//2)
    for y in range(-HEIGHT//2, HEIGHT//2+1, 100):
        pen.penup(); pen.goto(-WIDTH//2, y); pen.pendown(); pen.goto(WIDTH//2, y)

def plot(func, color="blue"):
    draw_axes()
    pen.pensize(2); pen.pencolor(color)
    first = True
    for sx in range(-WIDTH//2, WIDTH//2+1, STEP):
        x = sx / 50.0  # 50 px ~ 1 unidade em x
        try:
            y = func(x)
            sy = y * SCALE_Y
            if -HEIGHT//2 <= sy <= HEIGHT//2:
                pen.goto(sx, sy)
                if first:
                    pen.pendown(); first = False
            else:
                pen.penup(); first = True
        except Exception:
            pen.penup(); first = True
    screen.update()

# ----- funções simples -----
def f1(x): return math.sin(x)
def f2(x): return (x**2)/5.0
def f3(x): return 0.7*x - 2.0

def plot1(): plot(f1, "blue")
def plot2(): plot(f2, "green")
def plot3(): plot(f3, "red")

def clear_and_info():
    draw_axes()
    pen.penup(); pen.goto(-WIDTH//2+10, HEIGHT//2-30); pen.pencolor("black")
    pen.write("1=sin(x) | 2=x**2/5 | 3=0.7*x-2 | C=limpar", font=("Arial", 12, "normal"))
    screen.update()

# ----- binds -----
screen.listen()
screen.onkey(plot1, "1")
screen.onkey(plot2, "2")
screen.onkey(plot3, "3")
screen.onkey(clear_and_info, "c")

# inicial
clear_and_info()
t.mainloop()
