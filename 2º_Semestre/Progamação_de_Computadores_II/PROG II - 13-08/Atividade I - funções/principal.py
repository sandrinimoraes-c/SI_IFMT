from função import dobrar,dividir

n1 = float(input("Digite um número para verificarmos o dobro: "))
print(f"O dobro de {n1} é: {dobrar(n1)}")

n2 = float(input("Digite um número para verificarmos a metade: "))
print(f"A metade de {n2} é: {dividir(n2)}")

from operações import somar, subtrair, multiplicar

a =float(input("Digite um número x: "))
b = float(input("Digite um número y: "))

print(f"A soma de x,y é: {somar(a,b)}")
print(f"A subtração de x,y é: {subtrair(a,b)}")
print(f"A multiplicação de x,y é: {multiplicar(a,b)}")