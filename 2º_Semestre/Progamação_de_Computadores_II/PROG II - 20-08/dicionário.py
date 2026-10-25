dia = int(input("Digite um numero de 1 a 7: "))

dias = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sábado"
}

print(dias.get(dia)) #forma mais segura de exibir 

print(dias[dia]) #forma de exibir 