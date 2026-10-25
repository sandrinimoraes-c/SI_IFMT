
import turtle as t

t.bgcolor("black")
t.speed(0)
t.colormode(255)

t.penup()
t.goto(0, -50)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(50)
t.end_fill()


cores = [(255, 140, 0), (255, 200, 0), (255, 255, 255)]  
t.pensize(2)

t.penup()
t.goto(0, 0)
t.pendown()

for i in range(1000):
    cor = cores[i % len(cores)]
    t.pencolor(cor)
    t.forward(i * 2)   
    t.right(45)        

t.hideturtle()
t.done()
