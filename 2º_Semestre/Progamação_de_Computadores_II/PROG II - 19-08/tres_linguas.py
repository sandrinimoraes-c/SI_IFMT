#Criar um menu que mostre mensagens de saudação em 3 línguas diferentes, dependendo da opção escolhida.
saudacao = input("Escolha uma opção: 1, 2 ou 3: ")
match saudacao:
    case "1":
        print("Zdravstvuyte, dobro pozhalovat!")
    case "2":
        print("Halo selamat datang!")
    case "3":
        print("Xin chào, chào mừng!")
    case _:
        print("Yo no lo conozco")