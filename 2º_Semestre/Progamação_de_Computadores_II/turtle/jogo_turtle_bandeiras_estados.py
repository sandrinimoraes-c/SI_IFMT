# Jogo Educativo: Bandeiras dos Estados (somente turtle)
# Como jogar:
# - Pressione ESPAÇO para começar.
# - Observe a bandeira desenhada ao centro.
# - Clique na opção correta (os botões ficam ABAIXO do desenho).
# Observação: desenho estilizado com formas e cores aproximadas usando apenas turtle.

import turtle
import math

def retangulo(t, x, y, w, h):
    t.up(); t.goto(x, y); t.down()
    for _ in range(2):
        t.forward(w); t.left(90); t.forward(h); t.left(90)
    t.up()

def retangulo_preenchido(t, x, y, w, h, cor):
    t.color(cor, cor)
    t.up(); t.goto(x, y); t.setheading(0); t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(w); t.left(90); t.forward(h); t.left(90)
    t.end_fill()
    t.up()

def triangulo_preenchido(t, pontos, cor):
    # pontos: [(x1,y1), (x2,y2), (x3,y3)]
    t.color(cor, cor)
    t.up(); t.goto(pontos[0][0], pontos[0][y:=1]); t.down()
    t.begin_fill()
    t.goto(pontos[1][0], pontos[1][1])
    t.goto(pontos[2][0], pontos[2][1])
    t.goto(pontos[0][0], pontos[0][1])
    t.end_fill()
    t.up()

def poligono_preenchido(t, pontos, cor):
    t.color(cor, cor)
    t.up(); t.goto(pontos[0][0], pontos[0][1]); t.down()
    t.begin_fill()
    for (px, py) in pontos[1:]:
        t.goto(px, py)
    t.goto(pontos[0][0], pontos[0][1])
    t.end_fill()
    t.up()

def circulo_preenchido(t, x, y, r, cor):
    t.color(cor, cor)
    t.up(); t.goto(x, y - r); t.setheading(0); t.down()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.up()

def estrela(t, x, y, r, cor, pontos=5):
    t.color(cor, cor)
    t.up(); t.goto(x, y - r); t.setheading(90); t.down()
    t.begin_fill()
    # desenhar uma estrela regular de 5 pontas
    t.setheading(90)
    for _ in range(pontos):
        t.forward(r*2)
        t.right(144)
        t.forward(r*2)
        t.left(72)
    t.end_fill()
    t.up()

def texto_cent(t, msg, x, y, fonte=('Arial', 18, 'bold')):
    t.up(); t.goto(x, y); t.down()
    t.write(msg, align='center', font=fonte); t.up()


# Área do desenho da bandeira

FLAG_W, FLAG_H = 350, 180   # tamanho padrão da bandeira
FLAG_X, FLAG_Y = -FLAG_W/2, -FLAG_H/2 + 60  # centralizar um pouco acima do meio


# Funções para desenhar bandeiras 

def bandeira_para(t):
    # Pará: campo vermelho, faixa diagonal branca (de cima-esquerda para baixo-direita) e estrela azul
    retangulo_preenchido(t, FLAG_X, FLAG_Y, FLAG_W, FLAG_H, '#d7262d')  # vermelho
    # faixa diagonal branca
    t.color('white', 'white')
    poligono_preenchido(t, [
        (FLAG_X - 10, FLAG_Y + FLAG_H - 10),
        (FLAG_X + 40, FLAG_Y + FLAG_H + 10),
        (FLAG_X + FLAG_W + 10, FLAG_Y - 10),
        (FLAG_X + FLAG_W - 40, FLAG_Y - 30),
    ], 'white')
    # estrela azul no centro
    estrela(t, FLAG_X + FLAG_W/2, FLAG_Y + FLAG_H/2, 10, '#1f4ed8')

def bandeira_minas(t):
    # Minas Gerais: campo branco, triângulo vermelho central
    retangulo_preenchido(t, FLAG_X, FLAG_Y, FLAG_W, FLAG_H, 'white')
    # triângulo vermelho
    h = 120
    tri = [
        (0, 40 + 10),
        (-90, -40 + 10),
        (90, -40 + 10),
    ]
    # ajustar para o centro da bandeira
    tri = [(x, y) for (x, y) in tri]
    # converter coord relativas para absolutas
    tri_abs = [(x, y) for (x, y) in tri]
    # deslocar baseado no centro da bandeira
    cx, cy = FLAG_X + FLAG_W/2, FLAG_Y + FLAG_H/2
    tri_abs = [(cx + x, cy + y) for (x, y) in tri_abs]
    poligono_preenchido(t, tri_abs, '#d81b1b')

def bandeira_bahia(t):
    # Bahia: 9 listras horizontais (vermelho e branco alternadas) + cantão azul com triângulo branco
    # Listras
    stripes = 9
    stripe_h = FLAG_H / stripes
    colors = []
    # Alternar começando com vermelho no topo
    for i in range(stripes):
        colors.append('#d7262d' if i % 2 == 0 else 'white')
    for i, c in enumerate(colors):
        y = FLAG_Y + i*stripe_h
        retangulo_preenchido(t, FLAG_X, y, FLAG_W, stripe_h, c)
    # Cantão (canto superior esquerdo)
    canton_w = FLAG_W * 0.4
    canton_h = stripe_h * 4
    retangulo_preenchido(t, FLAG_X, FLAG_Y + FLAG_H - canton_h, canton_w, canton_h, '#1f4ed8')
    # Triângulo branco dentro do cantão
    tri = [
        (FLAG_X + canton_w*0.1, FLAG_Y + FLAG_H - canton_h*0.2),
        (FLAG_X + canton_w*0.1, FLAG_Y + FLAG_H - canton_h*0.8),
        (FLAG_X + canton_w*0.55, FLAG_Y + FLAG_H - canton_h*0.5),
    ]
    poligono_preenchido(t, tri, 'white')

def bandeira_goias(t):
    # Goiás: listras verdes e amarelas + cantão azul com estrelas
    stripes = 9
    stripe_h = FLAG_H / stripes
    for i in range(stripes):
        cor = '#1f7a1f' if i % 2 == 0 else '#ffd400'  # verde, amarelo
        y = FLAG_Y + i*stripe_h
        retangulo_preenchido(t, FLAG_X, y, FLAG_W, stripe_h, cor)
    # Cantão azul
    canton_w = FLAG_W * 0.35
    canton_h = stripe_h * 4
    retangulo_preenchido(t, FLAG_X, FLAG_Y + FLAG_H - canton_h, canton_w, canton_h, '#1f4ed8')
    # algumas "estrelas" brancas simples (círculos pequenos)
    for ex, ey in [ (0.08,0.85), (0.15,0.75), (0.25,0.82), (0.30,0.70), (0.20,0.62) ]:
        circulo_preenchido(t, FLAG_X + canton_w*ex, FLAG_Y + FLAG_H - canton_h + canton_h*ey, 5, 'white')

def bandeira_tocantins(t):
    # Tocantins: diagonal separando branco (superior esquerdo) e azul (inferior direito) + sol alaranjado
    # base branca
    retangulo_preenchido(t, FLAG_X, FLAG_Y, FLAG_W, FLAG_H, 'white')
    # triângulo azul (inferior direito)
    tri_azul = [
        (FLAG_X + FLAG_W, FLAG_Y),
        (FLAG_X + FLAG_W, FLAG_Y + FLAG_H),
        (FLAG_X + FLAG_W*0.35, FLAG_Y),
    ]
    poligono_preenchido(t, tri_azul, '#1f4ed8')
    # sol (círculo + "raios" simples) em laranja, no centro-esquerda
    cx, cy = FLAG_X + FLAG_W*0.35, FLAG_Y + FLAG_H*0.55
    circulo_preenchido(t, cx, cy, 18, '#ff9f1a')
    # raios (pequenos triângulos)
    for ang in [0, 45, 90, 135, 180, 225, 270, 315]:
        t.setheading(ang)
        r = 28
        p1 = (cx, cy)
        p2 = (cx + 26 * math.cos(math.radians(ang)), cy + 26 * math.sin(math.radians(ang)))
        p3 = (cx + 18 * math.cos(math.radians(ang+15)), cy + 18 * math.sin(math.radians(ang+15)))
        poligono_preenchido(t, [p1, p2, p3], '#ff9f1a')

def bandeira_acre(t):
    # Acre: campo dividido na diagonal (amarelo e verde) + estrela vermelha no canto superior esquerdo
    # amarelo (base)
    retangulo_preenchido(t, FLAG_X, FLAG_Y, FLAG_W, FLAG_H, '#ffd400')
    # triângulo verde (inferior direito)
    tri_verde = [
        (FLAG_X + FLAG_W, FLAG_Y),
        (FLAG_X + FLAG_W, FLAG_Y + FLAG_H),
        (FLAG_X, FLAG_Y),
    ]
    poligono_preenchido(t, tri_verde, '#1f7a1f')
    # estrela vermelha no canto superior esquerdo
    estrela(t, FLAG_X + 30, FLAG_Y + FLAG_H - 30, 12, '#d81b1b')


# Banco de questões (ordem fixa)
# Cada item: (nome, funcao_desenho, [op1, op2, op3])

QUESTOES = [
    ('Pará', bandeira_para, ['Pará', 'Minas Gerais', 'Bahia']),
    ('Minas Gerais', bandeira_minas, ['Bahia', 'Minas Gerais', 'Goiás']),
    ('Bahia', bandeira_bahia, ['Bahia', 'Pará', 'Tocantins']),
    ('Goiás', bandeira_goias, ['Goiás', 'Acre', 'Minas Gerais']),
    ('Tocantins', bandeira_tocantins, ['Pará', 'Tocantins', 'Goiás']),
    ('Acre', bandeira_acre, ['Acre', 'Bahia', 'Pará']),
]


# Jogo

class JogoBandeiras:
    def __init__(self):
        self.scr = turtle.Screen()
        self.scr.title('Bandeiras dos Estados')
        self.scr.setup(900, 650)
        self.scr.bgcolor('#f6f8ff')
        self.scr.tracer(0)

        self.pen_ui  = turtle.Turtle(visible=False); self.pen_ui.speed(0); self.pen_ui.pensize(2)
        self.pen_d   = turtle.Turtle(visible=False); self.pen_d.speed(0)  # desenha a bandeira
        self.pen_txt = turtle.Turtle(visible=False); self.pen_txt.speed(0)
        self.pen_msg = turtle.Turtle(visible=False); self.pen_msg.speed(0)

        self.iniciado = False
        self.idx = 0
        self.pontos = 0
        self.botoes = []  # dict(x,y,w,h,rotulo)

        self.scr.onclick(self.on_click)
        self.scr.onkey(self.iniciar, 'space')
        self.scr.listen()

        self.tela_inicial()
        self.scr.update()

    def tela_inicial(self):
        self.clear_all()
        texto_cent(self.pen_msg, 'Bandeiras dos Estados 🐢', 0, 220, ('Arial', 26, 'bold'))
        texto_cent(self.pen_msg, 'Pressione ESPAÇO para começar', 0, 180, ('Arial', 14, 'normal'))
        texto_cent(self.pen_msg, 'As opções aparecem ABAIXO do desenho', 0, 150, ('Arial', 12, 'italic'))
        self.scr.update()

    def clear_all(self):
        self.pen_ui.clear(); self.pen_d.clear(); self.pen_txt.clear(); self.pen_msg.clear(); self.botoes.clear()

    def iniciar(self):
        if self.iniciado: return
        self.iniciado = True
        self.idx = 0
        self.pontos = 0
        self.nova()

    def hud(self):
        self.pen_ui.clear()
        # moldura superior
        self.pen_ui.color('#c7cbe9')
        retangulo(self.pen_ui, -430, 270, 860, 50)
        self.pen_ui.color('#2a2a2a')
        texto_cent(self.pen_ui, f'Questão {self.idx+1}/{len(QUESTOES)}', -220, 285, ('Arial', 14, 'bold'))
        texto_cent(self.pen_ui, f'Pontos: {self.pontos}', 220, 285, ('Arial', 14, 'bold'))

    def desenhar_botoes(self, labels):
        # três botões alinhados abaixo da bandeira
        self.botoes.clear()
        w, h = 400, 40
        x = -w/2
        spacing = 50
        y_start = FLAG_Y - 70  # abaixo do retângulo da bandeira
        ys = [y_start - spacing*i for i in range(len(labels))]
        for i, lab in enumerate(labels):
            self.pen_ui.color('#4c6ef5')
            retangulo(self.pen_ui, x, ys[i], w, h)
            texto_cent(self.pen_ui, lab, x + w/2, ys[i] + h/2 - 10, ('Arial', 20, 'bold'))
            self.botoes.append({'x': x, 'y': ys[i], 'w': w, 'h': h, 'rotulo': lab})

    def nova(self):
        self.pen_msg.clear(); self.pen_d.clear(); self.pen_txt.clear()
        if self.idx >= len(QUESTOES):
            self.fim()
            return

        self.hud()

        nome, fn, opcoes = QUESTOES[self.idx]
        # moldura da bandeira
        self.pen_ui.color('#c7cbe9')
        retangulo(self.pen_ui, FLAG_X-5, FLAG_Y-5, FLAG_W+10, FLAG_H+10)
        # desenhar bandeira
        fn(self.pen_d)

        # Pergunta
        texto_cent(self.pen_txt, 'De qual estado é essa bandeira?', 0, FLAG_Y + FLAG_H/2 + 110, ('Arial', 20, 'bold'))

        # Opções ABAIXO do desenho
        self.resposta = nome
        self.desenhar_botoes(opcoes)

        self.scr.update()

    def on_click(self, x, y):
        if not self.iniciado: return
        for bt in self.botoes:
            if bt['x'] <= x <= bt['x'] + bt['w'] and bt['y'] <= y <= bt['y'] + bt['h']:
                if bt['rotulo'] == self.resposta:
                    self.pontos += 1
                    self.feedback('Correto! ✅', '#1f7a1f')
                else:
                    self.feedback(f'Ops! Era {self.resposta}', '#d7262d')
                self.idx += 1
                self.nova()
                break

    def feedback(self, msg, cor):
        self.pen_msg.clear(); self.pen_msg.color(cor)
        texto_cent(self.pen_msg, msg, 0, FLAG_Y - 10, ('Arial', 14, 'bold'))
        self.scr.update()

    def fim(self):
        self.iniciado = False
        self.clear_all()
        texto_cent(self.pen_msg, 'Fim do jogo! 🎉', 0, 80, ('Arial', 28, 'bold'))
        texto_cent(self.pen_msg, f'Pontos: {self.pontos}/{len(QUESTOES)}', 0, 40, ('Arial', 20, 'bold'))
        texto_cent(self.pen_msg, 'Pressione ESPAÇO para jogar novamente', 0, 5, ('Arial', 14, 'normal'))
        self.scr.update()

if __name__ == '__main__':
    JogoBandeiras()
    turtle.done()
