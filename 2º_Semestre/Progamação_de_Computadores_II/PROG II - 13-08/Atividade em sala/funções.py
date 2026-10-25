#Função para verificar maioridade
def verificar_maioridade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

#Função para calcular área de triângulo
def area_triangulo(base, altura):
    return (base * altura) / 2

#Função para calcular desconto de 10%
def calcular_desconto(preço):
    desconto = preço * 0.10
    return preço - desconto