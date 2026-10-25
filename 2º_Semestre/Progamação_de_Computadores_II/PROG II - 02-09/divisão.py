def dividir (a,b):
    try:
        resultado = a/b
        print ("Resultado:", resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero")
    for i in range (3):
        dividir(i, i-1)