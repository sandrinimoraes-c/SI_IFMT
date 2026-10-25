num=int(input("Digite um número: "))
i=num
print(f"\nTabuada do {num}")
for i in range(1,11):
    resultado=num * i
    print(f"{num} x {i} = {resultado}")