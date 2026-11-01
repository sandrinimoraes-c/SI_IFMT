Sistema de Gerenciamento de Pets (CRUD)
Este projeto é uma aplicação desktop com interface gráfica desenvolvida em Python para o cadastro e gerenciamento de pets, incluindo um sistema integrado de autenticação de usuários. A aplicação suporta operações completas de CRUD (Criar, Ler, Atualizar e Deletar) conectadas diretamente a um banco de dados relacional.

Tecnologias Utilizadas
Linguagem: Python 3.x

Interface Gráfica: CustomTkinter (customtkinter)

Banco de Dados: MySQL / MariaDB (mysql-connector-python)

Ambiente de Desenvolvimento: GitHub Codespaces (com recurso desktop-lite para renderização visual via noVNC)

Como Executar no GitHub Codespaces
O projeto foi totalmente adaptado para rodar na nuvem, permitindo a exibição de interfaces gráficas diretamente no navegador sem a necessidade de instalações locais.

1. Preparar o Banco de Dados
O sistema requer o MariaDB (ou MySQL) ativo em segundo plano. No terminal do Codespaces, instale e configure as credenciais padrão do projeto (root com a senha 10111997):

Bash
sudo apt-get update && sudo apt-get install -y mariadb-server
sudo service mariadb start
sudo mariadb -e "ALTER USER 'root'@'localhost' IDENTIFIED BY '10111997'; FLUSH PRIVILEGES;"
2. Configurar o Ambiente Python
Isole as dependências do projeto criando um ambiente virtual e instalando as bibliotecas exigidas:

Bash
python3 -m venv .venv
source .venv/bin/activate
pip install customtkinter mysql-connector-python
3. Iniciar a Interface Gráfica
É necessário direcionar a saída de vídeo do Python para o servidor de display virtual do Codespaces antes de rodar o código. Execute:

Bash
export DISPLAY=:0
cd 4º_Semestre/Ferramentas_rad/Atividades/AtividadeAvaliativa03
python3 main.py
4. Acessar o Aplicativo
Assim que o programa estiver em execução, verifique a aba Portas (Ports) localizada ao lado do Terminal.

Localize a porta 6080 (Desktop noVNC).

Clique no ícone de globo (ou acesse a notificação pop-up) para abrir essa porta no navegador.

O ambiente de desktop virtual será carregado e a interface do sistema de Pets estará pronta para uso.

Gerenciamento de Dados (Opcional)
Para visualizar, inserir ou modificar dados diretamente no banco, você pode abrir uma nova aba de terminal (sem fechar a aplicação) e acessar o console do banco:

Bash
mariadb -u root -p
# Quando solicitado, digite a senha: 10111997
Comandos úteis no terminal SQL: USE sistema_login_pets; para selecionar o banco, seguido de SELECT * FROM usuarios; ou SELECT * FROM pets; para inspecionar os registros criados.