#Criar um programa que peça ao usuário para escolher uma fruta e, usando match/case, mostrar o preço correspondente.
fruta = input("Escolha uma fruta: 1 - maçã, 2 - pera ou 3 - melancia: ")
match fruta:
    case "1":
        print("O preço da maçã é R$10,00 kg.")
    case "2":
        print("O preço da pera é R$15,00 kg.")
    case "3":
        print("O preço da melancia é R$25,00 kg.")
    case _:
        print("Não temos essa opção.")