# Atividade Avaliativa 03 - Sistema de Cadastro de Pets

Este projeto consiste numa aplicação com interface gráfica desenvolvida em Python para a gestão de pets. Inclui um sistema de autenticação e integração com uma base de dados MySQL, garantindo que cada pet registado fica associado de forma exclusiva ao utilizador que iniciou a sessão.

**⚠️ Aviso sobre o GitHub Codespaces (Ambientes Cloud)**
A interface gráfica desta aplicação (baseada na biblioteca `customtkinter`) **não pode ser executada visualmente no GitHub Codespaces**. Por ser um ambiente de terminal hospedado na nuvem, o Codespaces não possui um gestor de ecrã/monitor virtual para processar janelas gráficas (resultando no erro `$DISPLAY`). O ambiente em nuvem deve ser utilizado apenas para edição de código e comandos Git. 

Para testar a aplicação visualmente, siga as instruções de execução local abaixo.

**Tecnologias Utilizadas**
* **Python 3:** Lógica principal.
* **CustomTkinter:** Construção da interface gráfica moderna.
* **MySQL Server:** Base de dados relacional para armazenamento de utilizadores e pets.
* **mysql-connector-python:** Comunicação entre a aplicação e a base de dados.

**Como Executar na Máquina Local (Windows/macOS/Linux Desktop)**

1. Faça o clone do repositório ou garanta que os seus ficheiros estão sincronizados com um `git pull` no Visual Studio Code local.
2. Instale as bibliotecas necessárias abrindo o terminal da sua máquina e executando:
   `pip install customtkinter mysql-connector-python`
3. Certifique-se de que o serviço MySQL está ativo no seu computador (via XAMPP, WAMP ou instalação nativa).
4. No ficheiro `main.py`, verifique as credenciais de acesso ao banco de dados na secção `DB_USER` e `DB_PASSWORD`. O sistema criará a base de dados e as tabelas automaticamente na primeira execução.
5. Inicie o programa no terminal:
   `python main.py`