import conversor

while True:
    print("\n=== Conversor de Unidades ===")
    print("1 - Km → Milhas")
    print("2 - Milhas → Km")
    print("3 - Celsius → Fahrenheit")
    print("4 - Fahrenheit → Celsius")
    print("5 - Reais → Dólar")
    print("6 - Dólar → Reais")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            km = float(input("Km: "))
            print(f"{km} km = {conversor.km_para_milhas(km):.2f} milhas")

        case "2":
            milhas = float(input("Milhas: "))
            print(f"{milhas} milhas = {conversor.milhas_para_km(milhas):.2f} km")

        case "3":
            celsius = float(input("Celsius: "))
            print(f"{celsius} °C = {conversor.celsius_para_fahrenheit(celsius):.2f} °F")

        case "4":
            fahrenheit = float(input("Fahrenheit: "))
            print(f"{fahrenheit} °F = {conversor.fahrenheit_para_celsius(fahrenheit):.2f} °C")

        case "5":
            reais = float(input("Reais: R$ "))
            cotacao = float(input("Cotação do dólar: R$ "))
            print(f"R$ {reais:.2f} = US$ {conversor.reais_para_dolar(reais, cotacao):.2f}")

        case "6":
            dolar = float(input("Dólares: US$ "))
            cotacao = float(input("Cotação do dólar: R$ "))
            print(f"US$ {dolar:.2f} = R$ {conversor.dolar_para_reais(dolar, cotacao):.2f}")

        case "0":
            print("Encerrando...")
            break

        case _:
            print("Opção inválida!")