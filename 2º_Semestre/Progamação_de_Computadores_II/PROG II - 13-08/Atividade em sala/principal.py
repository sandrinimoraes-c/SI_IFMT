import funções

#Verificação de maioridade
idade = int(input("Digite a idade da pessoa: "))
print(funções.verificar_maioridade(idade))

#Cálculo da área do triângulo
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
print("Área do triângulo:", funções.area_triangulo(base, altura))

#Cálculo de desconto
preço = float(input("Digite o preço do produto: "))
print("Preço com desconto:", funções.calcular_desconto(preço))

#ou

# from funções import verificar_maioridade, area_triangulo, calcular_desconto

# idade = int(input("Digite a idade da pessoa: "))
# print(verificar_maioridade(idade))

# base = float(input("Digite a base do triângulo: "))
# altura = float(input("Digite a altura do triângulo: "))
# print("Área do triângulo:", area_triangulo(base, altura))

# preço = float(input("Digite o preço do produto: "))
# print("Preço com desconto:", calcular_desconto(preço))