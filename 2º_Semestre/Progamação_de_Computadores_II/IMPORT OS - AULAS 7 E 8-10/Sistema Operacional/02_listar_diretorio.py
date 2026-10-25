import os

print("Diretório de trabalho atual:")
print(os.getcwd())

print("\nConteúdo desta pasta:")
for nome in os.listdir():
    print("-", nome)