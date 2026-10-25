#Informar se o número é par ou impar
n = float(input("Digite um número: "))
match n % 2:
    case 0:
        print("O número é par!")
    case _:
        print("O número é ímpar!")