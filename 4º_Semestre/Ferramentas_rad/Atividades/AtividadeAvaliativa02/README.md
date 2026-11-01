# Sistema de Autenticação com Interface Gráfica

Este projeto é uma aplicação desktop desenvolvida em Python que implementa um sistema de controle de acesso (login) e redefinição de senhas. A aplicação possui um recurso de inicialização inteligente: na primeira execução, ela cria automaticamente o banco de dados, as tabelas necessárias e insere um usuário padrão para testes. O sistema pode ser executado localmente no seu computador ou na nuvem através do GitHub Codespaces.

## 🔑 Credenciais Padrão de Acesso
Ao rodar a aplicação pela primeira vez, o seguinte usuário é criado automaticamente no banco de dados para que você possa testar o sistema:
- **Usuário:** Sandrini
- **Senha:** 1234

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Interface Gráfica:** CustomTkinter (`customtkinter`) e Tkinter nativo
- **Base de Dados (Local):** MySQL (`mysql-connector-python`)
- **Base de Dados (Nuvem):** MariaDB (`mysql-connector-python`)
- **Ambientes:** VS Code (Local) / GitHub Codespaces (com renderização `desktop-lite` via noVNC)

---

## 💻 Opção 1: Como Executar Localmente (VS Code)

Utilize esta opção se estiver rodando o projeto diretamente no seu computador. Certifique-se de ter o **Python** e o **MySQL Server** instalados.

### 1. Configurar o Banco de Dados (MySQL)
Garanta que o serviço MySQL está ativo na sua máquina. A aplicação utiliza o usuário `root` com a senha `10111997`. O banco de dados `sistema_login` será criado automaticamente pelo próprio código Python.

### 2. Preparar o Ambiente Python
Abra o terminal integrado do VS Code na raiz do projeto e crie um ambiente virtual:

```bash
# 1. Criar o ambiente virtual
python -m venv .venv

# 2. Ativar o ambiente virtual
# No Windows:
.venv\Scripts\activate
# No Linux/Mac:
source .venv/bin/activate

# 3. Instalar as bibliotecas necessárias
pip install customtkinter mysql-connector-python