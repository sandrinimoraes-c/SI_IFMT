# Jogo Educativo de Matemática com Turtle
# Autor: ChatGPT
# Como jogar:
# 1) Pressione ESPAÇO para começar.
# 2) Leia a pergunta e clique na alternativa correta.
# 3) Você tem 45 segundos. Boa sorte!

import turtle
import random
import time

# -----------------------------
# Configurações do jogo
# -----------------------------
TEMPO_PARTIDA = 45  # segundos
OPS = ['+', '-', 'x']  # operações permitidas

# -----------------------------
# Utilidades
# -----------------------------
def desenhar_retangulo(t, x, y, w, h):
    t.up(); t.goto(x, y); t.down()
    for _ in range(2):
        t.forward(w); t.left(90); t.forward(h); t.left(90)
    t.up()

def escrever_centralizado(t, texto, x, y, fonte=('Arial', 18, 'bold')):
    t.up(); t.goto(x, y); t.down()
    t.write(texto, align='center', font=fonte)
    t.up()

def gerar_pergunta():
    op = random.choice(OPS)
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    # Evitar negativo na subtração
    if op == '-':
        a, b = max(a, b), min(a, b)
        resultado = a - b
    elif op == '+':
        resultado = a + b
    else:  # multiplicacao
        resultado = a * b
        op = 'x'
    return f'{a} {op} {b} = ?', resultado

def gerar_opcoes(resposta_certa):
    opcoes = {resposta_certa}
    while len(opcoes) < 3:
        delta = random.randint(1, 9)
        cand = resposta_certa + random.choice([-delta, delta])
        opcoes.add(cand)
    # Embaralha e retorna
    lista = list(opcoes)
    random.shuffle(lista)
    return lista

# -----------------------------
# Classe do Jogo
# -----------------------------
class JogoMatematica:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title('Jogo Educativo de Matemática - Turtle')
        self.screen.setup(width=900, height=600)
        self.screen.tracer(0)
        self.screen.bgcolor('#f7f7fb')

        # Canetas
        self.pen_ui = turtle.Turtle(visible=False)
        self.pen_ui.speed(0)
        self.pen_ui.pensize(2)

        self.pen_q = turtle.Turtle(visible=False)   # pergunta
        self.pen_q.speed(0)

        self.pen_msg = turtle.Turtle(visible=False) # mensagens (início/fim)
        self.pen_msg.speed(0)

        # Estado do jogo
        self.jogando = False
        self.tempo_restante = TEMPO_PARTIDA
        self.pontos = 0
        self.perguntas = 0
        self.resposta_certa = None
        self.botoes = []  # cada item: dict(x, y, w, h, valor)

        # Binding
        self.screen.onclick(self.on_click)
        self.screen.onkey(self.iniciar, 'space')
        self.screen.listen()

        self.tela_inicial()
        self.loop()

    # ---------- Tela ----------
    def tela_inicial(self):
        self.limpar_tudo()
        escrever_centralizado(self.pen_msg, 'Jogo Educativo de Matemática', 0, 150, ('Arial', 28, 'bold'))
        escrever_centralizado(self.pen_msg, 'Pressione ESPAÇO para começar', 0, 90, ('Arial', 18, 'normal'))
        escrever_centralizado(self.pen_msg, 'Clique na resposta correta. Você tem 45 segundos!', 0, 55, ('Arial', 14, 'normal'))
        self.desenhar_creditos()

    def desenhar_creditos(self):
        escrever_centralizado(self.pen_msg, 'Feito com Turtle 🐢', 0, -250, ('Arial', 12, 'italic'))

    def limpar_tudo(self):
        self.pen_ui.clear()
        self.pen_q.clear()
        self.pen_msg.clear()
        self.botoes = []

    # ---------- Jogo ----------
    def iniciar(self):
        if self.jogando:
            return
        self.jogando = True
        self.tempo_restante = TEMPO_PARTIDA
        self.pontos = 0
        self.perguntas = 0
        self.nova_pergunta()

    def nova_pergunta(self):
        self.pen_msg.clear()
        self.pen_q.clear()
        self.botoes.clear()

        pergunta, resposta = gerar_pergunta()
        self.resposta_certa = resposta
        self.perguntas += 1

        # UI de topo (HUD)
        self.desenhar_hud()

        # Pergunta
        escrever_centralizado(self.pen_q, pergunta, 0, 120, ('Arial', 32, 'bold'))

        # Opções como "botões"
        y_base = 20
        w, h = 500, 60
        xs = -w/2
        ys = [y_base + 90, y_base, y_base - 90]

        opcoes = gerar_opcoes(resposta)
        for i, val in enumerate(opcoes):
            self.desenhar_botao(xs, ys[i], w, h, str(val))
            self.botoes.append({'x': xs, 'y': ys[i], 'w': w, 'h': h, 'valor': val})

        self.screen.update()

    def desenhar_hud(self):
        self.pen_ui.clear()
        # Caixa superior
        self.pen_ui.color('#cccccc')
        desenhar_retangulo(self.pen_ui, -430, 230, 860, 60)

        # Texto HUD
        self.pen_ui.color('#333333')
        escrever_centralizado(self.pen_ui, f'Tempo: {self.tempo_restante:02d}s', -220, 245, ('Arial', 16, 'bold'))
        escrever_centralizado(self.pen_ui, f'Pontos: {self.pontos}', 0, 245, ('Arial', 16, 'bold'))
        acertos = f'{(self.pontos / self.perguntas * 100):.0f}%' if self.perguntas else '0%'
        escrever_centralizado(self.pen_ui, f'Aproveitamento: {acertos}', 220, 245, ('Arial', 16, 'bold'))

    def desenhar_botao(self, x, y, w, h, texto):
        self.pen_ui.color('#4c6ef5')
        desenhar_retangulo(self.pen_ui, x, y, w, h)
        escrever_centralizado(self.pen_ui, texto, x + w/2, y + h/2 - 10, ('Arial', 22, 'bold'))

    def on_click(self, x, y):
        if not self.jogando:
            return
        for bt in self.botoes:
            if bt['x'] <= x <= bt['x'] + bt['w'] and bt['y'] <= y <= bt['y'] + bt['h']:
                # Verifica resposta
                if bt['valor'] == self.resposta_certa:
                    self.pontos += 1
                    self.feedback('Correto! ✅', '#2f9e44')
                else:
                    self.feedback(f'Ops! A certa era {self.resposta_certa}', '#e03131')
                self.nova_pergunta()
                break

    def feedback(self, texto, cor):
        self.pen_msg.clear()
        self.pen_msg.color(cor)
        escrever_centralizado(self.pen_msg, texto, 0, -150, ('Arial', 16, 'bold'))
        self.screen.update()

    def terminar(self):
        self.jogando = False
        self.pen_q.clear()
        self.pen_ui.clear()
        self.pen_msg.clear()

        escrever_centralizado(self.pen_msg, 'Fim do jogo! ⏱️', 0, 100, ('Arial', 28, 'bold'))
        escrever_centralizado(self.pen_msg, f'Pontos: {self.pontos}', 0, 50, ('Arial', 20, 'bold'))
        if self.perguntas > 0:
            aproveitamento = (self.pontos / self.perguntas) * 100
        else:
            aproveitamento = 0.0
        escrever_centralizado(self.pen_msg, f'Aproveitamento: {aproveitamento:.0f}%', 0, 15, ('Arial', 18, 'normal'))
        escrever_centralizado(self.pen_msg, 'Pressione ESPAÇO para jogar novamente', 0, -30, ('Arial', 14, 'normal'))
        self.desenhar_creditos()
        self.screen.update()

    # ---------- Loop principal ----------
    def loop(self):
        # Atualiza timer
        if self.jogando:
            self.tempo_restante -= 1 if int(time.time() * 10) % 10 == 0 else 0  # degrade mais suave
            # Corrige para decrementar 1s aproximadamente a cada 10 ticks de 100ms
        # Chamaremos update a cada 100ms
        if self.jogando:
            # Redesenha HUD com tempo
            self.desenhar_hud()
            self.screen.update()

            # Decremento de tempo real a cada 1s
            # Implemento via um contador simples usando ontimer:
            # Aqui vamos apenas checar se terminou:
            if self.tempo_restante <= 0:
                self.terminar()
        self.screen.ontimer(self.loop, 100)

# Execução
if __name__ == '__main__':
    JogoMatematica()
    turtle.done()
