# Criação da matriz 5x5 vazia
matriz = [[0 for _ in range(5)] for _ in range(5)]

print("Insira 1 para pixel ligado e 0 para desligado")

# Preenchimento da matriz pelo usuário
for linha in range(5):
    for numero in range(5):
        # Correção da sintaxe do input e conversão para inteiro
        matriz[linha][numero] = int(input(f"Valor para posição [{linha}][{numero}]: "))

# Desenho da matriz na tela
for linha in matriz:
    desenhada = ""  # Inicializa a string vazia para a linha
    for pixel in linha:
        if pixel == 1:
            desenhada += "■ "  # Pixel ligado (preto/cheio) 
        else:
            desenhada += "□ "  # Pixel desligado (branco/vazio) 
    print(desenhada)