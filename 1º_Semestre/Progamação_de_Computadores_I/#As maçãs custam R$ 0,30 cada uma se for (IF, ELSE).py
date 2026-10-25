#As maçãs custam R$ 0,30 cada uma se forem compradas menos do que uma dúzia, e 0,25 se forem compradas pelo menos uma dúzia ou mais. Escreva um
#programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.
quantidade = int(input("Digite a quantidade de maçãs compras: "))
if quantidade < 12:
    preço = 0.30
else:
    preço = 0.25
total = quantidade * preço
print(f"O valor da compra: R${total}")