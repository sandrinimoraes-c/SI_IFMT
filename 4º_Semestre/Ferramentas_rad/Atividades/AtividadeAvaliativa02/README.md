Sistema de Autenticação com Interface Gráfica (Atividade 2)

Este projeto é uma aplicação desktop desenvolvida em Python que implementa um sistema de controle de acesso (login) e redefinição de senhas. A aplicação possui um recurso de inicialização inteligente: na primeira execução, ela cria automaticamente o banco de dados, as tabelas necessárias e insere um usuário padrão para testes. O sistema pode ser executado localmente no seu computador ou na nuvem através do GitHub Codespaces.

🔑 Credenciais Padrão de Acesso

Ao rodar a aplicação pela primeira vez, o seguinte usuário é criado automaticamente no banco de dados para que você possa testar o sistema:

Usuário: Sandrini

Senha: 1234

🛠️ Tecnologias Utilizadas

Linguagem: Python 3.x

Interface Gráfica: CustomTkinter (customtkinter) e Tkinter nativo

Base de Dados (Local): MySQL (mysql-connector-python)

Base de Dados (Nuvem): MariaDB (mysql-connector-python)

Ambientes: VS Code (Local) / GitHub Codespaces (com renderização desktop-lite via noVNC)

💻 Opção 1: Como Executar Localmente (VS Code)

Utilize esta opção se estiver rodando o projeto diretamente no seu computador. Certifique-se de ter o Python e o MySQL Server instalados.

1. Configurar o Banco de Dados (MySQL)

Garanta que o serviço MySQL está ativo na sua máquina. A aplicação utiliza o usuário root com a senha 10111997. O banco de dados sistema_login será criado automaticamente pelo próprio código Python.

2. Preparar o Ambiente Python

Abra o terminal integrado do VS Code na raiz do projeto e crie um ambiente virtual:

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

Navegue até a pasta onde o arquivo da Atividade 2 está salvo e execute o código:

# Substitua 'nome_do_arquivo.py' pelo nome correto do seu script Python
python nome_do_arquivo.py


☁️ Opção 2: Como Executar no GitHub Codespaces (Nuvem)

Utilize esta opção se estiver utilizando o ambiente de desenvolvimento online do GitHub. A interface gráfica será processada em um servidor de tela virtual e exibida no seu navegador.

1. Iniciar o Banco de Dados (MariaDB)

O Codespaces utiliza o MariaDB, que é compatível com o código. No terminal, inicie o serviço e configure a senha do servidor:

# Instalar o servidor (apenas se for a primeira vez criando o Codespace)
sudo apt-get update && sudo apt-get install -y mariadb-server

# Ligar o serviço (necessário sempre que o Codespace for reiniciado)
sudo service mariadb start

# Configurar a senha do servidor MySQL/MariaDB para o projeto
sudo mariadb -e "ALTER USER 'root'@'localhost' IDENTIFIED BY '10111997'; FLUSH PRIVILEGES;"


2. Preparar o Ambiente Python

Crie e ative o ambiente virtual no terminal do Codespaces:

python3 -m venv .venv
source .venv/bin/activate
pip install customtkinter mysql-connector-python


3. Configurar a Tela e Iniciar a Aplicação

Direcione a saída gráfica do Python para o monitor virtual do Codespaces (DISPLAY=:0) e execute o código:

export DISPLAY=:0
# Substitua 'nome_do_arquivo.py' pelo nome correto do script
python3 nome_do_arquivo.py


4. Acessar a Interface Gráfica no Navegador

Com o programa em execução no terminal, clique na aba Portas (Ports) ao lado do Terminal.

Identifique a porta 6080 (Desktop noVNC).

Clique no ícone de globo para abrir a porta no navegador. A tela de login aparecerá pronta para uso.

🗄️ Gestão de Dados (Opcional)

Você pode verificar se a tabela e o usuário padrão foram criados corretamente abrindo uma nova aba de terminal e acessando o banco de dados:

# Entrar no console do banco de dados (use mariadb ou mysql)
mariadb -u root -p
# Digite a senha quando solicitada: 10111997


Comandos SQL úteis no console:

SHOW DATABASES; (Verifique se sistema_login aparece na lista)

USE sistema_login; (Seleciona o banco criado pela aplicação)

SELECT * FROM usuarios; (Exibe os logins e senhas registrados no sistema)

exit (Sai do banco de dados e retorna ao terminal)