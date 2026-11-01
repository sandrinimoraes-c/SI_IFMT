Sistema de Gestão de Pets (CRUD) - Atividade 3

Este projeto é uma aplicação desktop com interface gráfica desenvolvida em Python para o registo e gestão de pets, incluindo um sistema integrado de autenticação de utilizadores. A aplicação suporta operações completas de CRUD (Criar, Ler, Atualizar e Apagar) e está configurada para funcionar em dois ambientes distintos: localmente no seu computador ou na nuvem através do GitHub Codespaces.

🛠️ Tecnologias Utilizadas

Linguagem: Python 3.x

Interface Gráfica: CustomTkinter (customtkinter)

Base de Dados (Local): MySQL (mysql-connector-python)

Base de Dados (Nuvem): MariaDB (mysql-connector-python)

Ambientes: VS Code (Local) / GitHub Codespaces (com renderização desktop-lite via noVNC)

💻 Opção 1: Como Executar Localmente (VS Code)

Utilize esta opção se estiver a correr o projeto diretamente no seu computador. Certifique-se de que tem o Python e o MySQL Server instalados.

1. Configurar a Base de Dados (MySQL)

Garanta que o serviço MySQL está ativo na sua máquina. A aplicação espera um utilizador root com a palavra-passe 10111997. Se a sua configuração local for diferente, altere as credenciais no ficheiro de ligação à base de dados do projeto.

2. Preparar o Ambiente Python

Abra o terminal integrado do VS Code na raiz do projeto e isole as dependências criando um ambiente virtual:

# 1. Criar o ambiente virtual
python -m venv .venv

# 2. Ativar o ambiente virtual
# No Windows:
.venv\Scripts\activate
# No Linux/Mac:
source .venv/bin/activate

# 3. Instalar as bibliotecas necessárias
pip install customtkinter mysql-connector-python


3. Iniciar a Aplicação

Navegue até à pasta do ficheiro principal e execute o código. A janela do programa abrir-se-á nativamente no seu sistema:

cd 4º_Semestre/Ferramentas_rad/Atividades/AtividadeAvaliativa03
python main.py


☁️ Opção 2: Como Executar no GitHub Codespaces (Nuvem)

Utilize esta opção se estiver a utilizar o ambiente de desenvolvimento online do GitHub. A interface gráfica será processada num servidor de ecrã virtual e exibida no seu navegador.

1. Iniciar a Base de Dados (MariaDB)

O Codespaces utiliza o MariaDB, que é totalmente compatível com o código MySQL da aplicação. No terminal, inicie o serviço e configure a palavra-passe:

# Instalar o servidor (apenas se for a primeira vez que cria o Codespace)
sudo apt-get update && sudo apt-get install -y mariadb-server

# Ligar o serviço (necessário sempre que o Codespace for reiniciado)
sudo service mariadb start

# Configurar a palavra-passe do projeto
sudo mariadb -e "ALTER USER 'root'@'localhost' IDENTIFIED BY '10111997'; FLUSH PRIVILEGES;"


2. Preparar o Ambiente Python

Crie e ative o ambiente virtual no terminal do Codespaces:

python3 -m venv .venv
source .venv/bin/activate
pip install customtkinter mysql-connector-python


3. Configurar o Ecrã e Iniciar a Aplicação

Direcione a saída gráfica do Python para o monitor virtual do Codespaces (DISPLAY=:0) e execute o código:

export DISPLAY=:0
cd 4º_Semestre/Ferramentas_rad/Atividades/AtividadeAvaliativa03
python3 main.py


4. Aceder à Interface Gráfica no Navegador

Com o programa em execução no terminal, procure o separador Portas (Ports) ao lado do Terminal.

Identifique a porta 6080 (Desktop noVNC).

Clique no ícone de globo para abrir a porta no navegador. A interface do sistema de Pets aparecerá pronta a ser utilizada.

🗄️ Gestão de Dados (Opcional)

Seja no ambiente local (MySQL) ou no Codespaces (MariaDB), pode interagir diretamente com a base de dados via terminal para validar os registos. Abra um novo separador de terminal e execute:

# Entrar na consola da base de dados
mysql -u root -p
# (Ou 'mariadb -u root -p' no Codespaces)
# Digite a palavra-passe quando solicitada: 10111997


Comandos SQL úteis na consola:

SHOW DATABASES; (Lista as bases de dados)

USE sistema_login_pets; (Seleciona a base de dados do projeto)

SHOW TABLES; (Lista as tabelas disponíveis)

SELECT * FROM usuarios; (Exibe todos os utilizadores registados)

SELECT * FROM pets; (Exibe todos os pets registados)

exit (Sai da consola e regressa ao terminal)

