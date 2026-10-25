def processar_pessoas(pessoas):
    for pessoas in pessoas:
        if pessoas["idade"]>=18:

            print(f"{pessoas['nome']} é maior de idade.")

        elif pessoas["idade"]<0:
            print(f"{pessoas['nome']} tem idade inválida.")
        else:
            print(f"{pessoas['nome']} é menor de idade.")
    lista = [{"Nome":"Ana","idade":20}, {"nome": "Beto", "idade":15}, {"nome": "Cleo", "idade": -1}]
    processar_pessoas(lista)
        