
def km_para_milhas(km):
    return km * 0.621

def milhas_para_km(milhas):
    return milhas * 1.609

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def reais_para_dolar(reais, cotacao=5.20):
    return reais / cotacao

def dolar_para_reais(dolar, cotacao=5.20):
    return dolar * cotacao