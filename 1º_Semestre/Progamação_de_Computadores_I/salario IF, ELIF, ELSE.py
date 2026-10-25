salario = float(input("Digite o salário atual: "))
codigo = int(input("Digite o código do cargo(101, 102 ou 103): "))
if codigo == 101:
    porcentual = 0.10
elif codigo == 102:
    porcentual = 0.20
elif codigo == 103:
    porcentual = 0.30
else:
    porcentual = 0.40
novo_salario = salario + (salario * porcentual)
print(f"Novo salário: R${novo_salario}")