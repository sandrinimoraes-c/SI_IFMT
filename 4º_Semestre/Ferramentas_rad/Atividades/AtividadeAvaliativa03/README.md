# Sistema de Gestão de Pets (CRUD)

Este projeto é uma aplicação desktop com interface gráfica desenvolvida em Python para o registo e gestão de pets, incluindo um sistema integrado de autenticação de utilizadores. A aplicação suporta operações completas de CRUD (Criar, Ler, Atualizar e Apagar) e está configurada para funcionar em dois ambientes distintos: localmente no seu computador ou na nuvem através do GitHub Codespaces.

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.x
- **Interface Gráfica:** CustomTkinter (`customtkinter`)
- **Base de Dados (Local):** MySQL (`mysql-connector-python`)
- **Base de Dados (Nuvem):** MariaDB (`mysql-connector-python`)
- **Ambientes:** VS Code (Local) / GitHub Codespaces (com renderização `desktop-lite` via noVNC)

---

## 💻 Opção 1: Como Executar Localmente (VS Code)

Utilize esta opção se estiver a correr o projeto diretamente no seu computador. Certifique-se de que tem o **Python** e o **MySQL Server** instalados.

### 1. Configurar a Base de Dados (MySQL)
Garanta que o serviço MySQL está ativo na sua máquina. A aplicação espera um utilizador `root` com a palavra-passe `10111997`. Se a sua configuração local for diferente, altere as credenciais no ficheiro de ligação à base de dados do projeto.

### 2. Preparar o Ambiente Python
Abra o terminal integrado do VS Code na raiz do projeto e isole as dependências criando um ambiente virtual:

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