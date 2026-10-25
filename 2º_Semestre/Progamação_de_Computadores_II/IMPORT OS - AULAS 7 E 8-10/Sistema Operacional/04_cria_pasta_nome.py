import os

nome = input("Digite seu nome (pasta a ser criada): ").strip()

invalidos_windows = '<>:"/\\|?*'
seguro = "".join(ch for ch in nome if ch not in invalidos_windows).strip()

if not seguro:
    raise ValueError("Nome inválido ou vazio após remover caracteres proibidos.")

caminho = os.path.join(os.getcwd(), seguro)

if os.path.exists(caminho):
    print(f'A pasta "{seguro}" já existe em:\n{caminho}')
else:
    os.mkdir(caminho)
    print(f'Pasta "{seguro}" criada em:\n{caminho}')