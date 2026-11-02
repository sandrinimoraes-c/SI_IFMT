# Sistema de Cadastro de Pets

Terceira atividade avaliativa. Programa desenvolvido em Python com **CustomTkinter** e banco de dados **MySQL**, que registra os pets que a pessoa tem ou já teve. Reaproveita o login das atividades anteriores: cada usuário acessa e cadastra **apenas os seus próprios pets**.

---

## 📱 Especificação das Telas

O sistema é composto por quatro interfaces integradas:

1. **Tela de Login:**
   - Campos para entrada de `Usuário` e `Senha`.
   - Botão **Entrar**: valida as credenciais no banco de dados.
   - Botão **Sair**: encerra o aplicativo.
   - Link **Esqueceu a senha? Redefinir**: abre a janela de redefinição de senha.
   - Link **Novo por aqui? Cadastre-se**: abre a janela de cadastro de usuário.
2. **Cadastrar Usuário:**
   - Campos `Novo Login`, `Senha` e `Confirmar Senha`.
   - Não permite login repetido nem senhas diferentes.
3. **Redefinir Senha:**
   - Campos `Usuário`, `Senha Atual` e `Nova Senha`.
   - Só altera a senha se o usuário e a senha atual estiverem corretos.
4. **Cadastro de Pets (janela pós-login):**
   - Formulário com `Nome`, `Espécie` (Cachorro, Gato, Pássaro ou Outro), `Sexo` (Macho ou Fêmea), `Idade`, `Raça`, `Peso`, `Cor` e `Status` (Vivo ou Morto).
   - Botão **Salvar Pet**: grava o pet no banco e atualiza a lista.
   - Lista com os pets do usuário logado.
   - Botão **Sair da Conta**: volta para a tela de login.

---

## 💾 Regras de Negócio e Armazenamento

- **Banco de Dados:** MySQL (MariaDB no Codespaces), banco `sistema_login_pets`.
- **Tabela `usuarios`:** `id` (chave primária, auto incremento), `login` (único, obrigatório) e `senha` (obrigatória).
- **Tabela `pets`:** `id`, `usuario_id` (chave estrangeira para `usuarios.id`), `nome`, `especie`, `sexo`, `idade`, `raca`, `peso`, `cor` e `status_vida`, todos obrigatórios.
- **Um Usuário por Vez:** a lista de pets é filtrada por `usuario_id`, então cada usuário vê somente os seus pets.
- **Exclusão em Cascata:** ao apagar um usuário do banco, seus pets também são apagados.
- **Criação Automática:** na primeira execução, o programa cria o banco, as tabelas e o usuário padrão.
- **Usuário Padrão:** `Sandrini` / `1234`, inserido quando a tabela de usuários está vazia.
- **Funções Disponíveis:** cadastrar e listar pets. Esta versão não possui edição nem exclusão de pets.
- **Conexão:** configurada nas constantes do início do `main.py`:

```python
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "..."   # senha do seu MySQL/MariaDB
DB_NAME = "sistema_login_pets"
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
USE sistema_login_pets;
SELECT * FROM usuarios;
SELECT * FROM pets;
```

