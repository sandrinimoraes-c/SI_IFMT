import os

pasta = "Projetos"
caminho = os.path.join(os.getcwd(), pasta)

if os.path.exists(caminho):
    print(f'A pasta "{pasta}" já existia em:\n{caminho}')
else:
    os.mkdir(caminho)  # cria um nível
    print(f'Pasta "{pasta}" criada em:\n{caminho}')