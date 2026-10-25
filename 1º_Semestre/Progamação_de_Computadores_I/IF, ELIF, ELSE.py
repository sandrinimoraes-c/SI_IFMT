peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 25:
    print("Seu peso está normal.")
elif imc < 30:
    print("Você está acima do peso.")
else:
    print("Você está obeso(a).")