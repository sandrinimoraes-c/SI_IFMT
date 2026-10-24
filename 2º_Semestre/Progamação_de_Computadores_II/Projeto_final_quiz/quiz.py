import flet as ft
import random
import os

ARQUIVO_RANKING = "ranking.txt"

# ---------------------------------------------------------
# PERGUNTAS
# ---------------------------------------------------------
QUESTOES = [
    ("Qual é a capital do Brasil?",
     ["São Paulo","Rio de Janeiro","Brasília","Salvador"], 2),
    ("Em que data foi proclamada a Independência do Brasil?",
     ["21 de abril de 1822","7 de setembro de 1822","15 de novembro de 1889","1 de maio de 1888"], 1),
    ("Quem proclamou a independência do Brasil?",
     ["Getúlio Vargas","Dom Pedro I","Juscelino Kubitschek","Tiradentes"], 1),
    ("Qual é a maior cidade do Brasil em população?",
     ["Rio de Janeiro","Brasília","Salvador","São Paulo"], 3),
    ("Qual é a moeda oficial do Brasil?",
     ["Cruzeiro","Real","Dólar","Peso"], 1),
    ("Qual estado tem a maior extensão territorial?",
     ["Pará","Amazonas","Mato Grosso","Minas Gerais"], 1),
    ("Qual bioma ocupa a maior parte do Brasil?",
     ["Caatinga","Mata Atlântica","Cerrado","Amazônia"], 3),
    ("Qual o rio mais extenso do Brasil?",
     ["Rio São Francisco","Rio Paraná","Rio Negro","Rio Amazonas"], 3),
    ("Em que ano foi inaugurada Brasília?",
     ["1956","1960","1945","1970"], 1),
    ("Presidente que construiu Brasília:",
     ["Juscelino Kubitschek","Getúlio Vargas","João Figueredo","Itamar Franco"], 0),
    ("Em que ano foi outorgada a primeira constituição do Brasil:",
     ["1500","1910","1824","1988"], 2),
    ("Festa celebrada em fevereiro no Brasil:",
     ["Carnaval","Festa Junina","Réveillon","Oktoberfest"], 0),
    ("Carnaval típico do Nordeste com trios elétricos:",
     ["Recife","Fortaleza","Salvador","Maceió"], 2),
    ("Quem foi Tiradentes?",
     ["Poeta","Herói da Inconfidência Mineira","Explorador","1º presidente"], 1),
    ("Ponto mais alto do Brasil:",
     ["Agulhas Negras","Pico da Neblina","Pico da Bandeira","Pico Cristal"], 1),
    ("Região onde se localiza o Pantanal:",
     ["Nordeste","Norte","Centro-Oeste","Sudeste"], 2),
    ("Prato típico do Sul:",
     ["Feijoada","Churrasco","Moqueca","Acarajé"], 1),
    ("Feijoada é tradicionalmente servida em:",
     ["Sexta","Sábado","Quarta","Segunda"], 1),
    ("Pai da aviação:",
     ["Santos Dumont","Julio Vernes","Bartolomeu Dias","Rebouças"], 0),
    ("Estado mais populoso do Brasil:",
     ["Minas Gerais","Rio de Janeiro","São Paulo","Bahia"], 2),
    ("Quantos prêmios Nobel tem o Brasil (2025)?",
     ["1","2","Nenhum","3"], 2),
    ("Autor da letra do Hino Nacional:",
     ["Luiz Gonzaga","Raul Seixas","Joaquim Ósorio Duque-Estrada","Carlos Drummond"], 2),
    ("Cidade onde fica o Cristo Redentor:",
     ["São Paulo","Rio de Janeiro","Belo Horizonte","Brasília"], 1),
    ("Qual o principal ritmo musical Brasileiro:",
     ["Samba","Axé","Valsa","Tango"], 0),
    ("Ano da abolição:",
     ["1888","1822","1891","1910"], 0),
    ("Qual o arquiteto mais famoso do Brasil:",
     ["Costa e Silva","Cecilia Meireles","Oscar Niemeyer","Jânio Quadros"], 2),
    ("Cor predominante da bandeira:",
     ["Azul","Verde","Amarelo","Branco"], 1),
    ("Frase da bandeira:",
     ["Ordem e Progresso","Paz","União","Liberdade"], 0),
    ("Capital do Amazonas:",
     ["Manaus","Belém","Macapá","Boa Vista"], 0),
    ("Festa típica de junho:",
     ["Carnaval","Festa Junina","Círio de Nazaré","Bumba Meu Boi"], 1),
    ("Principal produto exportado:",
     ["Soja","Café","Milho","Canela"], 0),
    ("Qual o cangaceiro mais famoso do Brasil:",
     ["Galo Cego","Lampião","Padim Ciso","Marcola"], 1),
    ("Floresta costeira bem preservada:",
     ["Cerrado","Mata Atlântica","Caatinga","Pampa"], 1),
    ("Esporte mais popular:",
     ["Vôlei","Futebol","Basquete","Handebol"], 1),
    ("Qual a fabricante de aviões do Brasil top 3 do mundo:",
     ["Embraer","Boeing","Airbus","Marcopolo"], 0),
    ("Arquipélago paradisíaco da Bahia:",
     ["Noronha","Búzios","Tinharé","Abrolhos"], 3),
    ("Cidade do Pão de Açúcar:",
     ["Fortaleza","Rio de Janeiro","Recife","Natal"], 1),
    ("Movimento artístico de 1922:",
     ["Tropicalismo","Modernismo","Barroco","Romantismo"], 1),
    ("Maior estádio do Brasil:",
     ["Maracanã","Mineirão","Morumbi","Beira-Rio"], 0),
    ("Estado do açaí:",
     ["Bahia","Amazonas","Rio Grande do Sul","Pernambuco"], 1),
    ("Primeira capital do Brasil:",
     ["Brasília","Salvador","Rio de Janeiro","São Paulo"], 1),
    ("Festival religioso de Belém:",
     ["Círio de Nazaré","Nossa Senhora Aparecida","Iemanjá","Junina"], 0),
    ("Terra do Carnaval:",
     ["São Paulo","Fortaleza","Goiânia","Rio de Janeiro"], 3),
    ("Função do STF:",
     ["Legislar","Julgar questões constitucionais","Executar as Leis","Administrar cidades"], 1),
    ("Cidade do Elevador Lacerda:",
     ["Salvador","Recife","Manaus","São Luiz"], 0),
    ("Produto símbolo colonial:",
     ["Algodão","Açúcar","Cacau","Soja"], 1),
    ("Região semiárida:",
     ["Amazônia","Pampa","Caatinga","Mata Atlântica"], 2),
    ("Qual o menor mandato de Presidente do Brasil:",
     ["Tancredo Neves","Carlos Luz","Costa e Silva","Fernando Collor"], 1),
    ("Maior festival de música do Brasil (RJ):",
     ["C6 Festival","Rock in Rio","Lollapalooza","The Town"], 1),
    ("Qual a maior usina hidrelétrica do Brasil:",
     ["3 gargantas","Itaipu","Sobradinho","Belo Monte"], 1),
]

# ---------------------------------------------------------
# Carregar ranking
# ---------------------------------------------------------
def carregar_ranking():
    if not os.path.exists(ARQUIVO_RANKING):
        return []
    with open(ARQUIVO_RANKING, "r", encoding="utf-8") as f:
        linhas = f.read().splitlines()
    ranking = []
    for linha in linhas:
        nome, pontos = linha.split(";")
        ranking.append((nome, int(pontos)))
    return ranking

# ---------------------------------------------------------
# Salvar ranking (apenas 10 melhores)
# ---------------------------------------------------------
def salvar_ranking(lista):
    lista = sorted(lista, key=lambda x: x[1], reverse=True)[:10]
    with open(ARQUIVO_RANKING, "w", encoding="utf-8") as f:
        for nome, pontos in lista:
            f.write(f"{nome};{pontos}\n")

# ---------------------------------------------------------
# Aplicação principal
# ---------------------------------------------------------
def main(page: ft.Page):

    page.title = "Quiz Brasil"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    ranking = carregar_ranking()  # carrega ranking

    # ---------- TELA INICIAL - pedir nome ----------
    nome_field = ft.TextField(label="Seu nome", width=300)
    aviso_nome = ft.Text("", color="red")

    def iniciar(e):
        if nome_field.value.strip() == "":
            aviso_nome.value = "Digite seu nome!"
            page.update()
            return
        jogador_nome = nome_field.value.strip()
        iniciar_quiz(jogador_nome)

    page.add(
        ft.Column([
            ft.Text("🇧🇷 Quiz Brasil", size=32, weight="bold"),
            nome_field,
            aviso_nome,
            ft.ElevatedButton("Iniciar", on_click=iniciar, width=200)
        ], horizontal_alignment="center")
    )

    # ---------------------------------------------------------
    # FUNÇÃO QUE INICIA O JOGO
    # ---------------------------------------------------------
    def iniciar_quiz(nome):
        page.controls.clear()

        perguntas = QUESTOES[:]
        random.shuffle(perguntas)

        indice = 0
        acertos = 0
        status_resposta = ft.Text("", size=18, weight="bold")

        titulo = ft.Text("🇧🇷 Quiz Brasil", size=22, weight="bold")
        pergunta = ft.Text("", size=18, weight="bold", text_align="center")
        progresso = ft.Text("", size=16, weight="bold")

        botoes = []

        # ----------------------------------------------------------------
        # Função para responder
        # ----------------------------------------------------------------
        def responder(i):
            nonlocal indice, acertos

            correta = perguntas[indice][2]

            if i == correta:
                acertos += 1
                status_resposta.value = "✔ Resposta correta!"
                status_resposta.color = "green"
            else:
                status_resposta.value = f"✘ Errado! Correto: {perguntas[indice][1][correta]}"
                status_resposta.color = "red"

            page.update()

            # espera 0.8s e vai para a próxima pergunta
            page.run_task(delay_proxima)

        async def delay_proxima():
            import asyncio
            await asyncio.sleep(0.8)
            status_resposta.value = ""
            proxima()

        # ----------------------------------------------------------------
        # Avançar pergunta
        # ----------------------------------------------------------------
        def proxima():
            nonlocal indice
            indice += 1
            if indice >= len(perguntas):
                return finalizar()

            mostrar_pergunta()

        # ----------------------------------------------------------------
        # Mostrar a pergunta
        # ----------------------------------------------------------------
        def mostrar_pergunta():
            pergunta.value = perguntas[indice][0]
            progresso.value = f"Pergunta {indice+1}/{len(perguntas)}"

            alternativas = perguntas[indice][1]
            letras = ["A", "B", "C", "D"]

            for i in range(4):
                botoes[i].text = f"{letras[i]} - {alternativas[i]}"

            page.update()

        # ----------------------------------------------------------------
        # Finalizar e mostrar ranking
        # ----------------------------------------------------------------
        def finalizar():
            page.controls.clear()

            # salvar no ranking
            ranking.append((nome, acertos))
            salvar_ranking(ranking)

            # gerar ranking visual
            lista = sorted(ranking, key=lambda x: x[1], reverse=True)[:10]
            ranking_texto = "\n".join([f"{i+1}. {n} - {p} pontos" for i, (n, p) in enumerate(lista)])

            page.add(
                ft.Column([
                    ft.Text("🎉 Fim do Quiz!", size=28, weight="bold"),
                    ft.Text(f"{nome}, você acertou {acertos}!", size=22),
                    ft.Text("🏆 Top 10 jogadores:", size=22, weight="bold"),
                    ft.Text(ranking_texto, size=18),
                    ft.ElevatedButton("Jogar novamente", on_click=lambda e: reiniciar())
                ], horizontal_alignment="center", spacing=15)
            )
            page.update()

        # ----------------------------------------------------------------
        # Reiniciar tudo
        # ----------------------------------------------------------------
        def reiniciar():
            page.controls.clear()
            page.add(
                ft.Column([
                    ft.Text("🇧🇷 Quiz Brasil", size=32, weight="bold"),
                    nome_field,
                    aviso_nome,
                    ft.ElevatedButton("Iniciar", on_click=iniciar, width=200)
                ], horizontal_alignment="center")
            )
            page.update()

        # Criar botões
        for i in range(4):
            botoes.append(
                ft.ElevatedButton(
                    text="Opção",
                    width=300,
                    height=50,
                    on_click=lambda e, x=i: responder(x)
                )
            )

        # Layout do quiz
        page.add(
            ft.Column([
                titulo,
                progresso,
                pergunta,
                ft.Column(botoes, spacing=10),
                status_resposta
            ], spacing=20, horizontal_alignment="center")
        )

        mostrar_pergunta()


ft.app(target=main)