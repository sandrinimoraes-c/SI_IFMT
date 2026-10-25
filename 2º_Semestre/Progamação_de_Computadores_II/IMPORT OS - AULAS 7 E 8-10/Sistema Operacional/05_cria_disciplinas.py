import os

entrada = input("Digite 3 disciplinas separadas por vírgula: ")
disciplinas = [d.strip() for d in entrada.split(",")]

if len(disciplinas) != 3:
    raise ValueError("Informe exatamente 3 disciplinas.")

for disc in disciplinas:
    invalidos_windows = '<>:"/\\|?*'
    nome = "".join(ch for ch in disc if ch not in invalidos_windows).strip()
    nome = nome or "Disciplina_sem_nome"

    os.makedirs(nome, exist_ok=True)
    print("Criada/verificada:", nome)

print("Concluído! Pastas das 3 disciplinas prontas.")