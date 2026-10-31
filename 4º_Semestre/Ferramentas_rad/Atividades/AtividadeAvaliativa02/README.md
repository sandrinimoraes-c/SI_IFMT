# Sistema de Login com Banco de Dados MySQL

Segunda atividade avaliativa. O sistema de acesso foi atualizado para utilizar um banco de dados relacional (MySQL) em vez de arquivos de texto simples, garantindo maior escalabilidade e integridade no armazenamento das credenciais.

---

## 🚀 Funcionalidades da Aplicação

- **Interface Visual:** Desenvolvida em Python com a biblioteca `customtkinter` para um design moderno e responsivo.
- **Autenticação Segura:** Validação em tempo real de `Usuário` e `Senha` diretamente via consultas SQL.
- **Redefinição de Senha:** Fluxo independente que permite ao usuário alterar sua senha com validação de dados cruzados.
- **Setup Automático:** O sistema é capaz de criar automaticamente o banco de dados (`sistema_login`), a tabela (`usuarios`) e inserir um usuário administrador padrão na primeira execução, caso o banco esteja vazio.

---

## 🛠️ Tecnologias e Dependências

- Python 3.x
- CustomTkinter (UI)
- MySQL Server (Banco de Dados)
- MySQL Connector/Python (Ponte de comunicação)

---

## 💻 Como Executar Localmente (VS Code)

### 1. Preparando o Ambiente
Certifique-se de que possui um servidor MySQL rodando em sua máquina (através de instalação nativa, XAMPP ou WAMP). 
Abra o arquivo `main.py` e configure a senha do seu banco de dados na variável `DB_PASSWORD` (linha 14).

### 2. Instalação das Bibliotecas
No terminal integrado do seu editor, execute:
```bash
pip install customtkinter mysql-connector-python
```

### 3. Execução
Com as dependências instaladas e o servidor de banco de dados ativo, inicie o programa:
```bash
python main.py
```

---

## ☁️ Como Executar no GitHub (Codespaces)

Este projeto possui suporte para execução em contêineres e na nuvem, utilizando o `devcontainer.json` para renderizar a interface gráfica pelo navegador (via noVNC na porta 6080).

Como o ambiente do Codespaces é "limpo" a cada execução, você precisará configurar o servidor MySQL antes de rodar o código. Siga os passos no terminal do GitHub Codespaces:

**1. Instalar e iniciar o servidor MySQL:**
```bash
sudo apt-get update
sudo apt-get install -y mysql-server
sudo service mysql start
```

**2. Configurar a senha root (Para bater com o seu `main.py`):**
Substitua `sua_senha_aqui` pela mesma senha que está escrita no seu arquivo Python.
```bash
sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'sua_senha_aqui'; FLUSH PRIVILEGES;"
```

**3. Instalar as dependências do Python:**
```bash
pip install customtkinter mysql-connector-python
```

**4. Rodar o projeto:**
```bash
python3 main.py
```
*Após rodar, o GitHub exibirá um aviso no canto inferior direito de que um serviço está rodando na porta 6080. Clique em "Open in Browser" (Abrir no navegador) para ver e interagir com a tela do seu programa!*