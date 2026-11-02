# Sistema de Login e Recuperação de Senha com MySQL

Segunda atividade avaliativa. Evolução da Atividade 1: o programa continua em Python com **CustomTkinter**, mas agora os usuários são armazenados e consultados em um banco de dados **MySQL**, em vez de um arquivo de texto.

---

## 📱 Especificação das Telas

O sistema é composto por três interfaces integradas:

1. **Tela de Login:**
   - Campos para entrada de `Usuário` e `Senha`.
   - Botão **Entrar**: valida as credenciais no banco de dados.
   - Botão **Sair**: encerra o aplicativo.
   - Link **Esqueceu sua senha? Redefinir**: abre a janela de redefinição de senha.
2. **Janela Pós-Login (Área do Sistema):**
   - Só é acessível mediante autenticação válida.
   - Exibe o `Usuário` e a `Senha` do usuário logado.
   - Botão **Voltar para o Login**: retorna à tela inicial com os campos limpos.
3. **Redefinir Senha:**
   - Janela que exige `Confirmar Usuário`, `Nova Senha` e `Confirmar Nova Senha`.
   - Botões **Salvar** e **Cancelar**.

---

## 💾 Regras de Negócio e Armazenamento

- **Banco de Dados:** MySQL (MariaDB no Codespaces), banco `sistema_login`.
- **Tabela `usuarios`:** `id` (chave primária, auto incremento), `login` (único, obrigatório) e `senha` (obrigatória).
- **Criação Automática:** na primeira execução, o programa cria o banco, a tabela e o usuário padrão.
- **Usuário Padrão:** `Sandrini` / `1234`, inserido quando a tabela está vazia.
- **Redefinição de Senha:** só é gravada se o usuário existir e as duas senhas digitadas forem iguais.
- **Consultas Parametrizadas:** os comandos SQL usam `%s`, o que evita injeção de SQL.
- **Conexão:** configurada nas constantes do início do `main.py`:

```python
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "..."   # senha do seu MySQL/MariaDB
DB_NAME = "sistema_login"
```

---

## 🚀 Pré-requisitos e Como Executar

### 1. Instalar Dependências
Recomenda-se usar um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install customtkinter mysql-connector-python
```

### 2. Preparar o Banco de Dados

**Localmente:** mantenha o MySQL Server em execução e confira se `DB_PASSWORD` no `main.py` é a senha do seu usuário `root`.

**No GitHub Codespaces (MariaDB):**

```bash
# apenas na primeira vez
sudo apt-get update && sudo apt-get install -y mariadb-server

# sempre que o Codespace for reiniciado
sudo service mariadb start

# use a mesma senha definida em DB_PASSWORD
sudo mariadb -e "ALTER USER 'root'@'localhost' IDENTIFIED BY 'SUA_SENHA'; FLUSH PRIVILEGES;"
```

### 3. Suporte de Sistema (Linux e Codespaces)
Em distribuições Debian/Ubuntu, instale o Tkinter caso o sistema acuse falta de display gráfico:

```bash
sudo apt install python3-tk
```

No Codespaces, o arquivo `.devcontainer/devcontainer.json` (na raiz do repositório) cria o desktop virtual e já instala o `python3-tk`. Se o Codespace foi criado antes desse arquivo, reconstrua-o com `Ctrl+Shift+P` → **Codespaces: Full Rebuild Container**.

### 4. Executando o Projeto
Com o terminal aberto na pasta do arquivo, rode:

```bash
python3 main.py
```

### 5. Acessando a Interface no Codespaces
1. Abra a aba **Ports** (ao lado do Terminal).
2. Na porta **6080**, clique no ícone de globo.
3. Clique em **Connect** e informe a senha `vscode`.

A tela de login aparece no navegador.

---

## 🔎 Conferindo os Dados (opcional)

```bash
mariadb -u root -p        # no computador local: mysql -u root -p
```

```sql
USE sistema_login;
SELECT * FROM usuarios;
```