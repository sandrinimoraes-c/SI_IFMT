#Corrija os erros do código abaixo
#São 5 erros 

tarefas = []

def adicionar():
    tarefas.append(input("Digite a tarefa: "))

def listar():
    i = 1
    for t in tarefas:
        print("{i} - {t}")
        i += 1

while True:
    print("1-Adicionar  2-Listar  3-Sair")
    op = input("Escolha: ")
    if op == 1:
        adicionar()
    elif op == 2:
        listar()
    elif op == 3:
        break
