
lista_principal = [
    "Alvaro Adalberto Maciel Carneiro Junior",
    "Bruno Alves Peres",
    "Bruno Vinicius Ferreira Oliveira Rocha",
    "Claudemir da Silva Ferreira",
    "Elloa Fonseca Lima",
    "Fernando Taco Martins",
    "Francielder Pereira dos Santos",
    "Guilherme Ferreira",
    "Gustavo Rodrigues De Oliveira",
    "Jheymysonn Klark Souza Andrade",
    "Joao Gabriel Macedo Guder",
    "JosÃ© Getulio Cruz Barbosa Anacleto",
    "Kauan Carvalho dos Santos",
    "Kelvem Ribeiro Mota",
    "Khiara Aiane Pinheiro De Jesus Ferreira",
    "Mariana Eliza Rodrigues Silva De Lima",
    "Mateus Henrique GonÃ§alves dos Santos",
    "Samuel Dias Barbosa",
    "Sandrini Moraes Correa",
    "Vinicio dos Santos Martins",
    "Vinicius Lourenceto Silva",
    "Vitor Martins Rubinho"
]

novos_participantes_lista = [
    "Li­via Ramos da Costa",
    "Pedro Henrique Almeida",
    "Sophia Nogueira Santos",
    "Andre Luiz Carvalho",
    "Camila Rocha Tavares"
]

participantes_para_remover = [
    "Francielder Pereira dos Santos",
    "Guilherme Ferreira",
	"Claudemir da Silva Ferreira"
]

nomes_a_corrigir = {
    "Fernando Taco Martins": "Fernando Tacoo Martins",
    "Vinicius Lourenceto Silva": "Vinicius Lourencetto Silva"
}

#ATIVIDADE 1: Cadastro Inicial
print("--- INÍCIO ATIVIDADE 1: Cadastro Inicial ---")

# Crie uma lista vazia chamada participantes
participantes = []

# Adicione os nomes de alunos usando a lista principal
print("Adicionando nomes da lista principal...")
for nome in lista_principal:
    participantes.append(nome)

# Exiba a lista completa de participantes na tela
# (economizando espaço, mostrar apenas os 5 primeiros e os 5 últimos)
print(f"Lista de participantes (5 primeiros): {participantes[:5]}")
print(f"Lista de participantes (5 últimos): {participantes[-5:]}")


# O primeiro e o último nome da lista
print(f"\nPrimeiro nome: {participantes[0]}")
print(f"Último nome: {participantes[-1]}")

# A quantidade total de nomes armazenados
quantidade_inicial = len(participantes)
print(f"Quantidade total de nomes: {quantidade_inicial}")
print("--- FIM ATIVIDADE 1 ---")


#ATIVIDADE 2: Remoção (Pop)
print("\n--- INÍCIO ATIVIDADE 2: Remoção de Participantes ---")

# Considerar a lista principal (que agora é 'participantes')
# Remover os nomes citados na lista para remove-los da lista usando pop()
removidos = [] # Armazene os nomes removidos em uma nova lista

print(f"Nomes a remover: {participantes_para_remover}")

for nome_a_remover in participantes_para_remover:
    if nome_a_remover in participantes:
        # 1. Encontrar o índice do nome
        indice = participantes.index(nome_a_remover)
        # 2. Usar pop() com o índice para remover e salvar o nome
        item_removido = participantes.pop(indice)
        # 3. Adicionar o nome removido à lista 'removidos'
        removidos.append(item_removido)
        print(f"Removido com sucesso: '{item_removido}'")
    else:
        print(f"Atenção: '{nome_a_remover}' não foi encontrado na lista.")

# Exiba:
# A lista atualizada de participantes
print(f"\nLista atualizada de participantes (primeiros 5): {participantes[:5]}")
# A lista de nomes removidos
print(f"Lista de nomes removidos: {removidos}")
# A quantidade de participantes restantes
print(f"Quantidade de participantes restantes: {len(participantes)}")
print("--- FIM ATIVIDADE 2 ---")


#ATIVIDADE 3: Correção e Inserção (Insert)
print("\n--- INÍCIO ATIVIDADE 3: Correção e Inserção ---")

# Considere a lista principal
# Parte A: Atualizar (Corrigir)
print("Iniciando correções...")
for nome_antigo, nome_novo in nomes_a_corrigir.items():
    if nome_antigo in participantes:
        # Encontra o índice do nome antigo
        indice = participantes.index(nome_antigo)
        # Atualiza o nome na lista usando o índice
        participantes[indice] = nome_novo
        print(f"Corrigido: '{nome_antigo}' -> '{nome_novo}'")
    else:
        print(f"Atenção: '{nome_antigo}' não encontrado para correção.")

print(f"Lista após correções (exibindo nome corrigido 'Fernando'):")
for nome in participantes:
    if "Fernando" in nome:
        print(f"-> {nome}")


# Parte B: Inserir (Insert)
# Considere que a lista foi feita em ordem alfabética, então observe os índices
print("\nIniciando inserções em ordem alfabética...")

for nome_novo in novos_participantes_lista:
    inserido = False
    # Itera pela lista para encontrar a posição alfabética correta
    for i in range(len(participantes)):
        # Compara o novo nome com o nome atual da lista
        if nome_novo < participantes[i]:
            # Encontrou a posição, insere no índice 'i'
            participantes.insert(i, nome_novo)
            print(f"Inserido: '{nome_novo}' no índice {i}")
            inserido = True
            break
    
    # Se o loop terminou e 'inserido' é False, o nome deve ir no final da lista
    if not inserido:
        participantes.append(nome_novo) # .append() é como .insert() no último índice
        print(f"Inserido (no final): '{nome_novo}'")

# Exiba a lista completa após as modificações
print("\nExibindo lista final completa:")
# Usando enumerate para mostrar o índice e o nome
for indice, nome in enumerate(participantes):
    print(f"Índice {indice}: {nome}")

# Mostre também o total de elementos na lista após as inserções
print(f"\nTotal final de elementos: {len(participantes)}")
print("--- FIM ATIVIDADE 3 ---")