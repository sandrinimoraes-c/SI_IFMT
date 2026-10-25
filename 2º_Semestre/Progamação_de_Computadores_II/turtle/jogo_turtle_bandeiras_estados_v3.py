
#Jogo Educativo: Bandeiras dos Estados 


import turtle  # Importa o módulo gráfico turtle


def retangulo(t, x, y, w, h):
    """Desenha um retângulo (apenas contorno)."""
    t.up(); t.goto(x, y); t.down()
    for _ in range(2):
        t.forward(w); t.left(90); t.forward(h); t.left(90)
    t.up()

def retangulo_preenchido(t, x, y, w, h, cor):
    """Desenha um retângulo preenchido."""
    t.color(cor, cor)
    t.up(); t.goto(x, y); t.setheading(0); t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(w); t.left(90); t.forward(h); t.left(90)
    t.end_fill(); t.up()

def poligono_preenchido(t, pontos, cor):
    """Desenha um polígono preenchido a partir de uma lista de pontos."""
    t.color(cor, cor)
    t.up(); t.goto(pontos[0][0], pontos[0][1]); t.down()
    t.begin_fill()
    for (px, py) in pontos[1:]:
        t.goto(px, py)
    t.goto(pontos[0][0], pontos[0][1])
    t.end_fill(); t.up()

def circulo_preenchido(t, x, y, r, cor):
    """Desenha um círculo preenchido."""
    t.color(cor, cor)
    t.up(); t.goto(x, y - r); t.setheading(0); t.down()
    t.begin_fill(); t.circle(r); t.end_fill(); t.up()

def estrela(t, x, y, r, cor, pontas=5):
    """Desenha uma estrela regular (5 pontas por padrão)."""
    t.color(cor, cor)
    t.up(); t.goto(x, y + r); t.setheading(-90); t.down()
    t.begin_fill()
    for _ in range(pontas):
        t.forward(r * 2)
        t.left(180 - 180 / pontas)
    t.end_fill(); t.up()

def texto_cent(t, msg, x, y, fonte=('Arial', 18, 'bold')):
    """Escreve texto centralizado em (x, y)."""
    t.up(); t.goto(x, y); t.down()
    t.write(msg, align='center', font=fonte); t.up()

# ====================================================
# Configuração padrão da área de desenho da bandeira
# ====================================================
FLAG_W, FLAG_H = 350, 180
FLAG_X, FLAG_Y = -FLAG_W/2, -FLAG_H/2 + 60

# ====================================================
# Funções de desenho de bandeiras (estilizadas)
# ====================================================

def bandeira_para(t):
    """Pará: fundo vermelho, faixa diagonal branca e estrela azul."""
    retangulo_preenchido(t, FLAG_X, FLAG_Y, FLAG_W, FLAG_H, '#d7262d')
    poligono_preenchido(t, [
        (FLAG_X - 10, FLAG_Y + FLAG_H - 10),
        (FLAG_X + 40, FLAG_Y + FLAG_H + 10),
        (FLAG_X + FLAG_W + 10, FLAG_Y - 10),
        (FLAG_X + FLAG_W - 40, FLAG_Y - 30),
    ], 'white')
    estrela(t, FLAG_X + FLAG_W/2, FLAG_Y + FLAG_H/2, 10, '#1f4ed8')

def bandeira_minas(t):
    """Minas Gerais: fundo branco com triângulo vermelho central."""
    retangulo_preenchido(t, FLAG_X, FLAG_Y, FLAG_W, FLAG_H, 'white')
    cx, cy = FLAG_X + FLAG_W/2, FLAG_Y + FLAG_H/2
    tri = [(0, 50), (-80, -40), (80, -40)]
    tri_abs = [(cx + x, cy + y) for (x, y) in tri]
    poligono_preenchido(t, tri_abs, '#d81b1b')

def bandeira_bahia(t):
    """Bahia: listras vermelhas/brancas e cantão azul com triângulo branco."""
    stripes = 9; stripe_h = FLAG_H / stripes
    for i in range(stripes):
        cor = '#d7262d' if i % 2 == 0 else 'white'
        y = FLAG_Y + i * stripe_h
        retangulo_preenchido(t, FLAG_X, y, FLAG_W, stripe_h, cor)
    canton_w = FLAG_W * 0.4; canton_h = stripe_h * 4
    retangulo_preenchido(t, FLAG_X, FLAG_Y + FLAG_H - canton_h, canton_w, canton_h, '#1f4ed8')
    tri = [
        (FLAG_X + canton_w*0.12, FLAG_Y + FLAG_H - canton_h*0.18),
        (FLAG_X + canton_w*0.12, FLAG_Y + FLAG_H - canton_h*0.82),
        (FLAG_X + canton_w*0.58, FLAG_Y + FLAG_H - canton_h*0.50),
    ]
    poligono_preenchido(t, tri, 'white')

def bandeira_goias(t):
    """Goiás: listras verdes/amarelas e cantão azul com círculos brancos."""
    stripes = 9; stripe_h = FLAG_H / stripes
    for i in range(stripes):
        cor = '#1f7a1f' if i % 2 == 0 else '#ffd400'
        y = FLAG_Y + i * stripe_h
        retangulo_preenchido(t, FLAG_X, y, FLAG_W, stripe_h, cor)
    canton_w = FLAG_W * 0.35; canton_h = stripe_h * 4
    retangulo_preenchido(t, FLAG_X, FLAG_Y + FLAG_H - canton_h, canton_w, canton_h, '#1f4ed8')
    for ex, ey in [(0.10,0.80), (0.18,0.70), (0.28,0.82), (0.32,0.66), (0.22,0.60)]:
        cx = FLAG_X + canton_w * ex
        cy = FLAG_Y + FLAG_H - canton_h + canton_h * ey
        circulo_preenchido(t, cx, cy, 5, 'white')

def bandeira_tocantins(t):
    """Tocantins: fundo branco, triângulo azul e sol com raios."""
    retangulo_preenchido(t, FLAG_X, FLAG_Y, FLAG_W, FLAG_H, 'white')
    tri_azul = [
        (FLAG_X + FLAG_W, FLAG_Y),
        (FLAG_X + FLAG_W, FLAG_Y + FLAG_H),
        (FLAG_X + FLAG_W*0.35, FLAG_Y),
    ]
    poligono_preenchido(t, tri_azul, '#1f4ed8')
    cx, cy = FLAG_X + FLAG_W*0.35, FLAG_Y + FLAG_H*0.55
    circulo_preenchido(t, cx, cy, 18, '#ff9f1a')
    t.color('#ff9f1a', '#ff9f1a')
    for ang in range(0, 360, 45):
        t.up(); t.goto(cx, cy); t.setheading(ang)
        t.down(); t.begin_fill()
        t.forward(26); t.left(120); t.forward(10); t.left(120); t.forward(10)
        t.end_fill(); t.up()

def bandeira_acre(t):
    """Acre: fundo amarelo, triângulo verde e estrela vermelha."""
    retangulo_preenchido(t, FLAG_X, FLAG_Y, FLAG_W, FLAG_H, '#ffd400')
    tri_verde = [(FLAG_X, FLAG_Y), (FLAG_X + FLAG_W, FLAG_Y + FLAG_H), (FLAG_X + FLAG_W, FLAG_Y)]
    poligono_preenchido(t, tri_verde, '#1f7a1f')
    estrela(t, FLAG_X + 28, FLAG_Y + FLAG_H - 28, 10, '#d81b1b')

# ====================================================
# Banco de questões
# ====================================================
QUESTOES = [
    ('Pará',       bandeira_para,      ['Pará', 'Minas Gerais', 'Bahia']),
    ('Minas Gerais', bandeira_minas,   ['Bahia', 'Minas Gerais', 'Goiás']),
    ('Bahia',      bandeira_bahia,     ['Bahia', 'Pará', 'Tocantins']),
    ('Goiás',      bandeira_goias,     ['Goiás', 'Acre', 'Minas Gerais']),
    ('Tocantins',  bandeira_tocantins, ['Pará', 'Tocantins', 'Goiás']),
    ('Acre',       bandeira_acre,      ['Acre', 'Bahia', 'Pará']),
]

# ====================================================
# Classe principal do jogo
# ====================================================

class JogoBandeiras:
    def __init__(self):
        self.scr = turtle.Screen()
        self.scr.title('Bandeiras dos Estados - Somente turtle')
        self.scr.setup(900, 650)
        self.scr.bgcolor('#f6f8ff')
        self.scr.tracer(0)

        self.pen_ui  = turtle.Turtle(visible=False); self.pen_ui.speed(0); self.pen_ui.pensize(2)
        self.pen_d   = turtle.Turtle(visible=False); self.pen_d.speed(0)
        self.pen_txt = turtle.Turtle(visible=False); self.pen_txt.speed(0)
        self.pen_msg = turtle.Turtle(visible=False); self.pen_msg.speed(0)

        self.iniciado = False
        self.idx = 0
        self.pontos = 0
        self.botoes = []
        self.resposta = ''

        self.scr.onclick(self.on_click)
        self.scr.onkey(self.iniciar, 'space')
        self.scr.listen()

        self.tela_inicial()
        self.scr.update()

    def tela_inicial(self):
        self.clear_all()
        texto_cent(self.pen_msg, 'Bandeiras dos Estados (somente turtle) 🐢', 0, 220, ('Arial', 26, 'bold'))
        texto_cent(self.pen_msg, 'Pressione ESPAÇO para começar', 0, 180, ('Arial', 14, 'normal'))
        texto_cent(self.pen_msg, 'As opções aparecem ABAIXO do desenho', 0, 150, ('Arial', 12, 'italic'))
        self.scr.update()

    def clear_all(self):
        self.pen_ui.clear(); self.pen_d.clear(); self.pen_txt.clear(); self.pen_msg.clear(); self.botoes.clear()

    def iniciar(self):
        if self.iniciado: return
        self.iniciado = True; self.idx = 0; self.pontos = 0
        self.nova()

    def hud(self):
        self.pen_ui.clear()
        self.pen_ui.color('#c7cbe9')
        retangulo(self.pen_ui, -430, 270, 860, 50)
        self.pen_ui.color('#2a2a2a')
        texto_cent(self.pen_ui, f'Questão {self.idx+1}/{len(QUESTOES)}', -220, 285, ('Arial', 14, 'bold'))
        texto_cent(self.pen_ui, f'Pontos: {self.pontos}', 220, 285, ('Arial', 14, 'bold'))

    def desenhar_botoes(self, labels):
        self.botoes.clear()
        w, h = 400, 40; x = -w/2; spacing = 50; y_start = FLAG_Y - 70
        ys = [y_start - spacing*i for i in range(len(labels))]
        for i, lab in enumerate(labels):
            self.pen_ui.color('#4c6ef5')
            retangulo(self.pen_ui, x, ys[i], w, h)
            texto_cent(self.pen_ui, lab, x + w/2, ys[i] + h/2 - 10, ('Arial', 20, 'bold'))
            self.botoes.append({'x': x, 'y': ys[i], 'w': w, 'h': h, 'rotulo': lab})

    def nova(self):
        self.pen_msg.clear(); self.pen_d.clear(); self.pen_txt.clear()
        if self.idx >= len(QUESTOES): self.fim(); return
        self.hud()
        nome, fn, opcoes = QUESTOES[self.idx]
        self.pen_ui.color('#c7cbe9')
        retangulo(self.pen_ui, FLAG_X-5, FLAG_Y-5, FLAG_W+10, FLAG_H+10)
        fn(self.pen_d)
        texto_cent(self.pen_txt, 'De qual estado é essa bandeira?', 0, FLAG_Y + FLAG_H/2 + 110, ('Arial', 20, 'bold'))
        self.resposta = nome
        self.desenhar_botoes(opcoes)
        self.scr.update()

    def on_click(self, x, y):
        if not self.iniciado: return
        for bt in self.botoes:
            if bt['x'] <= x <= bt['x'] + bt['w'] and bt['y'] <= y <= bt['y'] + bt['h']:
                if bt['rotulo'] == self.resposta:
                    self.pontos += 1; self.feedback('Correto! ✅', '#1f7a1f')
                else:
                    self.feedback(f'Ops! Era {self.resposta}', '#d7262d')
                self.idx += 1; self.nova(); break

    def feedback(self, msg, cor):
        self.pen_msg.clear(); self.pen_msg.color(cor)
        texto_cent(self.pen_msg, msg, 0, FLAG_Y - 10, ('Arial', 14, 'bold'))
        self.scr.update()

    def fim(self):
        self.iniciado = False; self.clear_all()
        texto_cent(self.pen_msg, 'Fim do jogo! 🎉', 0, 80, ('Arial', 28, 'bold'))
        texto_cent(self.pen_msg, f'Pontos: {self.pontos}/{len(QUESTOES)}', 0, 40, ('Arial', 20, 'bold'))
        texto_cent(self.pen_msg, 'Pressione ESPAÇO para jogar novamente', 0, 5, ('Arial', 14, 'normal'))
        self.scr.update()




if __name__ == '__main__':
    JogoBandeiras()
    turtle.done()
