# Sistema de Cadastro de Pets com Autenticação (MySQL)

Terceira atividade avaliativa. Este projeto expande o sistema de login anterior, introduzindo um sistema de gerenciamento de Pets. Utiliza um banco de dados relacional (MySQL) para garantir que cada usuário logado tenha acesso exclusivo e seguro apenas aos animais que ele próprio cadastrou.

## 🚀 Funcionalidades da Aplicação

* **Interface Visual:** Desenvolvida em Python com a biblioteca `customtkinter` para um design moderno e responsivo.
* **Autenticação Segura:** Validação de login e senha do usuário.
* **Banco de Dados Relacional:** Criação automática do banco (`sistema_login`) e das tabelas relacionadas (`usuarios` e `pets`) usando chaves estrangeiras (Foreign Keys).
* **Cadastro de Pets:** Formulário completo para registrar animais contendo: Nome, Idade, Raça, Peso e Cor.
* **Isolamento de Dados:** O painel exibe apenas os Pets pertencentes ao usuário logado no momento.

## 🛠️ Tecnologias e Dependências

* Python 3.x
* CustomTkinter (Interface Gráfica)
* MySQL Server (Banco de Dados)
* MySQL Connector/Python (Ponte de comunicação)

---

## 💻 Como Executar Localmente (VS Code)

### 1. Preparando o Ambiente Local
Certifique-se de que possui um servidor MySQL rodando em sua máquina (através de instalação nativa, XAMPP ou WAMP).
No arquivo `main.py`, verifique a variável `DB_PASSWORD` (linha 13) e ajuste para a senha do seu banco de dados local (deixe `""` se usar o padrão do XAMPP).

### 2. Instalação das Bibliotecas
Abra o terminal integrado do VS Code (`Ctrl + '`) e instale as dependências:
```bash
pip install customtkinter mysql-connector-python
```

### 3. Execução
Com o servidor MySQL ligado, execute o arquivo principal no terminal:
```bash
python main.py
```

---

## ☁️ Como Executar no GitHub (Codespaces)

O projeto está configurado via `devcontainer.json` para rodar diretamente no navegador, projetando a interface gráfica através de um desktop virtual (noVNC na porta 6080).

Como o contêiner do Codespaces inicia um ambiente "limpo", você precisará iniciar o MySQL e instalar as dependências a cada nova sessão. Siga os comandos abaixo no terminal do Codespaces:

**1. Instalar e Iniciar o MySQL Server:**
```bash
sudo apt-get update
sudo apt-get install -y mysql-server
sudo service mysql start
```

**2. Configurar a Senha Root (Opcional):**
*Nota: Se o seu arquivo `main.py` estiver com `DB_PASSWORD = ""` (vazio), você pode pular este passo, pois o usuário root já vem sem senha no Ubuntu.*
Caso tenha colocado uma senha no código, configure-a no banco rodando:
```bash
sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'sua_senha_aqui'; FLUSH PRIVILEGES;"
```

**3. Instalar as Dependências do Python:**
```bash
pip install customtkinter mysql-connector-python
```

**4. Rodar o Sistema:**
```bash
python3 main.py
```

**Acessando a Interface:** Assim que rodar o comando acima, o GitHub mostrará um alerta no canto inferior direito informando que a porta 6080 está ativa. Clique em **"Open in Browser"** (Abrir no Navegador). Uma nova aba se abrirá com a interface do seu programa rodando no desktop virtual!