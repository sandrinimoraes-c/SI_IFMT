#Crie uma matriz 3x3 com números da sua escolha e calcule a soma de todos os elementos.

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

s = 0

for linha in matriz:
    for numero in linha:
        s+= numero

print(s)