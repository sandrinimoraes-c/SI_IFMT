#Corrija os erros do código abaixo
#Muitos erros



def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def main():
    while True: 

        print("CALCULADORA")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Sair")

        escolha = int(input("Escolha uma operação: "))

        if escolha == "5":
            print("Saindo da calculadora...")
            break

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

    if escolha == "1":
        resultado = somar(num1, num2)
    elif escolha == "2":
        resultado = subtrair(num1, num2)
    elif escolha == "3":
        resultado = multiplicar(num1, num2)
    elif escolha == "4":
        resultado = dividir(num1, num2)
    else:
        print("Opção inválida!")
        
        print(f"Resultado: {resultado}")

main()