def custo_final_carro():
    custo_fabrica = float(input("Digite o custo de fábrica do carro: "))
    distribuidor = custo_fabrica * 0.28
    impostos = custo_fabrica * 0.45
    custo_consumidor = custo_fabrica + distribuidor + impostos
    print(f"Custo final ao consumidor: R$ {custo_consumidor:.2f}")