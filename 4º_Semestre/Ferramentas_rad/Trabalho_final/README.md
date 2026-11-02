# Sistema de Animais de Rua e Adoção — Pontes e Lacerda (MT)

Sistema desktop (Python + CustomTkinter + MySQL) para registrar animais resgatados, acompanhar a saúde deles e gerenciar adoções.

> Documentação completa (tutorial de uso e diagrama ER) em construção. O diagrama ER já está em [`docs/diagrama-er.md`](docs/diagrama-er.md).

## Como executar

```bash
pip install -r requirements.txt

# senha do usuário root do seu MySQL/MariaDB (não fica no código)
export DB_PASSWORD="SUA_SENHA"        # Windows (PowerShell): $env:DB_PASSWORD="SUA_SENHA"

cd app
python3 main.py
```

Na primeira execução o programa cria o banco `animais_pontes_lacerda`, as tabelas e o usuário administrador:

| Usuário | Senha |
|---------|-------|
| admin | admin123 |

## Estrutura

```
banco/schema.sql      script de criação do banco
docs/                 documentação (diagrama ER)
app/main.py           ponto de entrada
app/app.py            janela principal e menu lateral
app/database.py       conexão e consultas ao MySQL
app/telas/            uma tela por arquivo
```
