# Jogo Educativo Minimalista (somente turtle)
import turtle

Q = [('3+4=?',7,[5,7,9]), ('10-6=?',4,[4,3,8]), ('5x2=?',10,[8,10,12])]  # (pergunta, certa, opcoes)
i=p=0; bs=[]  # índice, pontos, botões

s=turtle.Screen(); s.setup(800,500); s.title('Jogo Educativo Minimalista'); s.bgcolor('#f7f7fb'); s.tracer(0)
ui=turtle.Turtle(visible=False); ui.speed(0); ui.pensize(2)
tx=turtle.Turtle(visible=False); tx.speed(0)
msg=turtle.Turtle(visible=False); msg.speed(0)

def rect(x,y,w,h,c=None,fill=False):
    ui.up(); ui.goto(x,y); ui.setheading(0)
    if fill and c: ui.color(c,c); ui.down(); ui.begin_fill()
    else: ui.color(c or '#4c6ef5'); ui.down()
    for _ in range(2): ui.forward(w); ui.left(90); ui.forward(h); ui.left(90)
    if fill and c: ui.end_fill()
    ui.up()

def text(t, s, x, y, f=('Arial',18,'bold')):
    t.up(); t.goto(x,y); t.down(); t.write(s,align='center',font=f); t.up()

def draw():
    ui.clear(); tx.clear(); msg.clear(); bs.clear()
    text(tx, f'Questão {i+1}/{len(Q)}  |  Pontos: {p}', 0, 200, ('Arial',14,'bold'))
    q,c,ops = Q[i]
    text(tx, q, 0, 120, ('Arial',32,'bold'))
    # botões abaixo
    w,h,x,y = 500,60,-250,20
    for k,val in enumerate(ops):
        rect(x, y-90*k, w, h)
        text(ui, str(val), x+w/2, y-90*k+h/2-10, ('Arial',22,'bold'))
        bs.append((x,y-90*k,w,h,val))
    s.update()

def click(x,y):
    global i,p
    if i>=len(Q): start(); return
    for bx,by,bw,bh,val in bs:
        if bx<=x<=bx+bw and by<=y<=by+bh:
            if val==Q[i][1]: p+=1; msg.color('#2f9e44'); text(msg,'Correto! ✅',0,-160,('Arial',14,'bold'))
            else: msg.color('#e03131'); text(msg,f'Ops! Era {Q[i][1]}',0,-160,('Arial',14,'bold'))
            i+=1
            if i<len(Q): draw()
            else: end()
            break

def start():
    global i,p; i=p=0; ui.clear(); tx.clear(); msg.clear()
    text(tx,'Jogo Educativo Minimalista',0,80,('Arial',26,'bold'))
    text(tx,'Pressione ESPAÇO para começar',0,40,('Arial',14,'normal')); s.update()

def end():
    ui.clear(); tx.clear()
    text(msg,'Fim do jogo! 🎉',0,40,('Arial',26,'bold'))
    text(msg,f'Pontos: {p}/{len(Q)}',0,5,('Arial',18,'bold'))
    text(msg,'Clique para recomeçar',0,-30,('Arial',12,'normal')); s.update()

def on_space(): 
    if i==0 and p==0: draw()
    elif i>=len(Q): start()

s.onclick(click); s.onkey(on_space,'space'); s.listen()
start()
turtle.done()
