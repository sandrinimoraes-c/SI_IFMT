# Crie uma matriz com os seguintes números:
# [2, 4, 6, 8],
# [1, 3, 5, 7],
# [10, 12, 14, 16],
# [9, 11, 13, 15]

# Exiba a matriz original e depois crie uma nova matriz dobrando cada número da matriz original.

matriz = [
    [2, 4, 6, 8],
    [1, 3, 5, 7],
    [10, 12, 14, 16],
    [9, 11, 13, 15]
]

print("Matriz original:")
for linha in matriz:
    print(linha)

nova_matriz = []
for linha in matriz:
    nova_linha = []
    for numero in linha:
        nova_linha.append(numero * 2)
    nova_matriz.append(nova_linha)

print("\nMatriz com valores dobrados:")
for linha in nova_matriz:
    print(linha)
