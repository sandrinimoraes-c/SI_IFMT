# Jogo Educativo: Formas Geométricas (somente turtle)
# Como jogar:
# - Pressione ESPAÇO para começar.
# - Observe a forma desenhada no centro.
# - Clique no botão com o nome correto da forma.
# - Use apenas o módulo turtle (sem random, sem time).

import turtle

# -----------------------------
# Utilidades de UI (somente turtle)
# -----------------------------
def retangulo(t, x, y, w, h):
    t.up(); t.goto(x, y); t.down()
    for _ in range(2):
        t.forward(w); t.left(90); t.forward(h); t.left(90)
    t.up()

def texto_c(t, msg, x, y, fonte=('Arial', 18, 'bold')):
    t.up(); t.goto(x, y); t.down()
    t.write(msg, align='center', font=fonte); t.up()

# -----------------------------
# Desenho das formas (somente turtle)
# -----------------------------
def desenhar_circulo(t):
    t.up(); t.goto(0, -80); t.setheading(0); t.down()
    t.circle(80); t.up()

def desenhar_quadrado(t):
    t.up(); t.goto(-80, -80); t.setheading(0); t.down()
    for _ in range(4):
        t.forward(160); t.left(90)
    t.up()

def desenhar_triangulo(t):
    t.up(); t.goto(-90, -70); t.setheading(0); t.down()
    for _ in range(3):
        t.forward(180); t.left(120)
    t.up()

def desenhar_retang(t):
    t.up(); t.goto(-110, -60); t.setheading(0); t.down()
    for _ in range(2):
        t.forward(220); t.left(90); t.forward(120); t.left(90)
    t.up()

def desenhar_pentagono(t):
    t.up(); t.goto(0, 0); t.setheading(-90); t.forward(70); t.left(90); t.backward(80); t.setheading(0); t.down()
    t.up(); t.goto(-70, -30); t.setheading(0); t.down()
    for _ in range(5):
        t.forward(140); t.left(72)
    t.up()

# -----------------------------
# Questões fixas (sem aleatoriedade)
# Cada item: (nome_da_forma, funcao_de_desenho, [op1, op2, op3])
# -----------------------------
QUESTOES = [
    ('Círculo', desenhar_circulo, ['Círculo', 'Quadrado', 'Triângulo']),
    ('Quadrado', desenhar_quadrado, ['Triângulo', 'Quadrado', 'Retângulo']),
    ('Triângulo', desenhar_triangulo, ['Retângulo', 'Pentágono', 'Triângulo']),
    ('Retângulo', desenhar_retang, ['Retângulo', 'Círculo', 'Quadrado']),
    ('Pentágono', desenhar_pentagono, ['Triângulo', 'Pentágono', 'Círculo']),
]

# -----------------------------
# Classe do jogo
# -----------------------------
class JogoFormas:
    def __init__(self):
        self.scr = turtle.Screen()
        self.scr.title('Jogo de Formas Geométricas - Somente Turtle')
        self.scr.setup(900, 600)
        self.scr.bgcolor("#ffffff")
        self.scr.tracer(0)

        self.pen_ui = turtle.Turtle(visible=False); self.pen_ui.speed(0); self.pen_ui.pensize(2)
        self.pen_q  = turtle.Turtle(visible=False); self.pen_q.speed(0)
        self.pen_d  = turtle.Turtle(visible=False); self.pen_d.speed(0)  # desenho da forma
        self.pen_msg= turtle.Turtle(visible=False); self.pen_msg.speed(0)

        self.iniciado = False
        self.idx = 0
        self.pontos = 0
        self.botoes = []  # dict(x,y,w,h,texto)

        self.scr.onclick(self.on_click)
        self.scr.onkey(self.iniciar, 'space')
        self.scr.listen()

        self.tela_inicial()
        self.scr.update()

    def tela_inicial(self):
        self.limpa()
        texto_c(self.pen_msg, 'Formas Geométricas (Somente Turtle) 🐢', 0, 120, ('Arial', 28, 'bold'))
        texto_c(self.pen_msg, 'Pressione ESPAÇO para começar', 0, 70, ('Arial', 16, 'normal'))
        texto_c(self.pen_msg, 'Clique no nome correto da forma desenhada no centro', 0, 35, ('Arial', 14, 'normal'))
        texto_c(self.pen_msg, 'Feito apenas com turtle', 0, -260, ('Arial', 12, 'italic'))
        self.scr.update()

    def limpa(self):
        self.pen_ui.clear(); self.pen_q.clear(); self.pen_msg.clear(); self.pen_d.clear(); self.botoes.clear()

    def iniciar(self):
        if self.iniciado: return
        self.iniciado = True
        self.idx = 0
        self.pontos = 0
        self.nova_questao()

    def hud(self):
        self.pen_ui.clear()
        self.pen_ui.color('#cccccc')
        retangulo(self.pen_ui, -430, 230, 860, 60)
        self.pen_ui.color('#333333')
        texto_c(self.pen_ui, f'Questão: {self.idx+1}/{len(QUESTOES)}', -220, 245, ('Arial', 16, 'bold'))
        texto_c(self.pen_ui, f'Pontos: {self.pontos}', 220, 245, ('Arial', 16, 'bold'))

    def desenhar_botao(self, x, y, w, h, texto):
        self.pen_ui.color('#4c6ef5')
        retangulo(self.pen_ui, x, y, w, h)
        texto_c(self.pen_ui, texto, x + w/2, y + h/2 - 10, ('Arial', 22, 'bold'))

    def nova_questao(self):
        self.pen_msg.clear(); self.pen_q.clear(); self.pen_d.clear(); self.botoes.clear()
        if self.idx >= len(QUESTOES):
            self.fim()
            return

        self.hud()

        nome, funcao_desenho, opcoes = QUESTOES[self.idx]
        texto_c(self.pen_q, 'Qual é a forma?', 0, 160, ('Arial', 26, 'bold'))

        # Desenhar a forma no centro
        self.pen_d.color('#333333')
        funcao_desenho(self.pen_d)

        # Opções (ordem fixa)
        y_base = -40
        w, h = 500, 60
        x = -w/2
        ys = [y_base + 120, y_base + 30, y_base - 60]

        for i, label in enumerate(opcoes):
            self.desenhar_botao(x, ys[i], w, h, label)
            self.botoes.append({'x': x, 'y': ys[i], 'w': w, 'h': h, 'texto': label})

        # Guardar resposta correta (string)
        self.resposta_certa = nome

        self.scr.update()

    def on_click(self, x, y):
        if not self.iniciado: return
        for bt in self.botoes:
            if bt['x'] <= x <= bt['x'] + bt['w'] and bt['y'] <= y <= bt['y'] + bt['h']:
                if bt['texto'] == self.resposta_certa:
                    self.pontos += 1
                    self.feedback('Correto! ✅', '#2f9e44')
                else:
                    self.feedback(f'Ops! Era {self.resposta_certa}', '#e03131')
                self.idx += 1
                self.nova_questao()
                break

    def feedback(self, msg, cor):
        self.pen_msg.clear()
        self.pen_msg.color(cor)
        texto_c(self.pen_msg, msg, 0, 210, ('Arial', 14, 'bold'))
        self.scr.update()

    def fim(self):
        self.iniciado = False
        self.pen_q.clear(); self.pen_ui.clear(); self.pen_msg.clear(); self.pen_d.clear()
        texto_c(self.pen_msg, 'Fim do jogo! 🎉', 0, 80, ('Arial', 28, 'bold'))
        texto_c(self.pen_msg, f'Pontos: {self.pontos}/{len(QUESTOES)}', 0, 35, ('Arial', 20, 'bold'))
        texto_c(self.pen_msg, 'Pressione ESPAÇO para jogar novamente', 0, -10, ('Arial', 14, 'normal'))
        texto_c(self.pen_msg, 'Feito apenas com turtle', 0, -260, ('Arial', 12, 'italic'))
        self.scr.update()

if __name__ == '__main__':
    JogoFormas()
    turtle.done()
