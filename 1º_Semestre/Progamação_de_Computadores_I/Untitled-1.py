def salario_vendedor():
    carros_vendidos = int(input("Carros vendidos: "))
    total_vendas = float(input("Total de vendas: "))
    salario_fixo = float(input("Salário fixo: "))
    valor_por_carro = float(input("Valor por carro vendido: "))
    salario_final = salario_fixo + (carros_vendidos * valor_por_carro) + (0.05 * total_vendas)
    print(f"Salário final: R$ {salario_final:.2f}")