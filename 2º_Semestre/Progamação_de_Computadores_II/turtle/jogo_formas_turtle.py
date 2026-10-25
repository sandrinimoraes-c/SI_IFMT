# Jogo Educativo de Formas Geométricas com Turtle
# Autor: ChatGPT
# Requisitos: Python 3.x
# Como executar: python jogo_formas_turtle.py

import turtle
import random
import sys

# ------------------------------
# Utilidades
# ------------------------------
def normalizar(texto: str) -> str:
    """Deixa minúsculo, sem acentos e sem espaços extras."""
    if texto is None:
        return ""
    texto = texto.strip().lower()
    # Remoção simples de acentos (sem bibliotecas externas)
    mapa = {
        "á":"a","à":"a","â":"a","ã":"a","ä":"a",
        "é":"e","è":"e","ê":"e","ë":"e",
        "í":"i","ì":"i","î":"i","ï":"i",
        "ó":"o","ò":"o","ô":"o","õ":"o","ö":"o",
        "ú":"u","ù":"u","û":"u","ü":"u",
        "ç":"c"
    }
    return "".join(mapa.get(c, c) for c in texto)

# ------------------------------
# Desenho das formas
# ------------------------------
caneta = turtle.Turtle()
caneta.hideturtle()
caneta.speed(0)
caneta.pensize(4)

def limpar():
    caneta.clear()
    caneta.up()
    caneta.home()
    caneta.setheading(0)
    caneta.down()

def cor_aleatoria():
    turtle.colormode(255)
    return (random.randint(40, 220), random.randint(40, 220), random.randint(40, 220))

def desenhar_quadrado(tam=160):
    caneta.color(cor_aleatoria())
    caneta.up(); caneta.goto(-tam/2, -tam/2); caneta.down()
    for _ in range(4):
        caneta.forward(tam)
        caneta.left(90)

def desenhar_retangulo(l=220, h=140):
    caneta.color(cor_aleatoria())
    caneta.up(); caneta.goto(-l/2, -h/2); caneta.down()
    for _ in range(2):
        caneta.forward(l); caneta.left(90)
        caneta.forward(h); caneta.left(90)

def desenhar_triangulo(tam=200):
    caneta.color(cor_aleatoria())
    # Triângulo equilátero centralizado (aproximação)
    altura = (3**0.5)/2 * tam
    caneta.up(); caneta.goto(-tam/2, -altura/2); caneta.down()
    for _ in range(3):
        caneta.forward(tam)
        caneta.left(120)

def desenhar_circulo(raio=90):
    caneta.color(cor_aleatoria())
    caneta.up(); caneta.goto(0, -raio); caneta.down()
    caneta.circle(raio)

FORMAS = {
    "quadrado": desenhar_quadrado,
    "retangulo": desenhar_retangulo,
    "triangulo": desenhar_triangulo,
    "circulo": desenhar_circulo,
}

# Aceitar variações com acento
ALIAS = {
    "quadrado": {"quadrado"},
    "retangulo": {"retangulo", "retângulo"},
    "triangulo": {"triangulo", "triângulo"},
    "circulo": {"circulo", "círculo"},
}

def eh_resposta_certa(alvo_norm: str, resposta_usuario: str) -> bool:
    r = normalizar(resposta_usuario)
    # mapear para a chave base (sem acento)
    for chave, variantes in ALIAS.items():
        if r in {normalizar(v) for v in variantes}:
            return chave == alvo_norm
    return False

# ------------------------------
# Jogo
# ------------------------------
def jogar(total_rodadas=8):
    tela = turtle.Screen()
    tela.title("Jogo de Formas Geométricas - Turtle")
    tela.setup(width=900, height=700)

    pontos = 0
    nomes_formas = list(FORMAS.keys())

    for rodada in range(1, total_rodadas + 1):
        limpar()
        alvo = random.choice(nomes_formas)  # 'quadrado', 'retangulo', 'triangulo', 'circulo'
        FORMAS[alvo]()  # desenha

        # Pergunta
        prompt = (
            f"Rodada {rodada}/{total_rodadas}\n"
            "Qual forma geométrica foi desenhada?\n"
            "(Opções: círculo, quadrado, triângulo, retângulo)\n\n"
            "Digite o nome da forma (ou Cancelar para sair):"
        )
        resposta = turtle.textinput("Pergunta", prompt)
        if resposta is None:
            break  # saiu
        if eh_resposta_certa(alvo, resposta):
            pontos += 1
            # Feedback visual simples
            caneta.up(); caneta.goto(0, 230); caneta.down()
            caneta.write("✔ Acertou!", align="center", font=("Arial", 22, "bold"))
            tela.update()
        else:
            caneta.up(); caneta.goto(0, 230); caneta.down()
            nome_correto = {"circulo":"círculo","retangulo":"retângulo","triangulo":"triângulo","quadrado":"quadrado"}[alvo]
            caneta.write(f"✘ Errou! Era {nome_correto}.", align="center", font=("Arial", 22, "bold"))
            tela.update()

        # Pequena pausa entre rodadas (espera clique)
        turtle.done  # no-op para ambientes fora do padrão
        # Para seguir para a próxima rodada com clique do mouse:
        tela.onclick(lambda x, y: None)
        tela.listen()
        # Limpa o on-click para não acumular
        tela.onclick(None)

    # Placar final
    limpar()
    caneta.up(); caneta.goto(0, 20); caneta.down()
    caneta.write(f"Fim de jogo! Você fez {pontos} ponto(s).", align="center", font=("Arial", 26, "bold"))
    caneta.up(); caneta.goto(0, -30); caneta.down()
    caneta.write("Feche a janela para encerrar.", align="center", font=("Arial", 14, "normal"))

    # Aguarda o usuário fechar a janela
    turtle.done()

if __name__ == "__main__":
    try:
        jogar(8)
    except turtle.Terminator:
        # Caso o usuário feche a janela durante o jogo
        try:
            turtle.bye()
        except Exception:
            pass
        sys.exit(0)
