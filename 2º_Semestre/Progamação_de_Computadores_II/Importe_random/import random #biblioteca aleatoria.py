import random as r #biblioteca aleatoria

# numero = r.randint(1,10)
# print(f"O numero escolhido é {numero}")

nomes = ["Sandrini", "Samuel", "João"]

escolhido = r.choice(nomes)
print(f"O sortudo para responder a pergunta é: {escolhido}")