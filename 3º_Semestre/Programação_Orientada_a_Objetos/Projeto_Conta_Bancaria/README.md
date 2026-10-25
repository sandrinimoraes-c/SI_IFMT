# Sistema Bancário Simples (POO - Projeto 01)

Este é um projeto simples de sistema bancário desenvolvido em Java para demonstrar conceitos fundamentais de **Programação Orientada a Objetos (POO)**.

O sistema funciona via terminal (CLI) e permite o gerenciamento básico de uma conta bancária associada a um cliente.

## 📋 Funcionalidades

O sistema oferece um menu interativo com as seguintes opções:

*   **Criar Cliente e Conta**: Cadastra um novo titular (Nome e CPF) e inicia uma conta com saldo zero.
*   **Depositar**: Adiciona saldo à conta criada.
*   **Sacar**: Retira valores da conta (com validação de saldo suficiente).
*   **Ver Dados da Conta**: Exibe o titular, CPF, número da conta e saldo atual.

## 📂 Estrutura do Projeto

O projeto é composto pelas seguintes classes principais:

*   **`Cliente.java`**: Representa o titular da conta. Armazena dados pessoais como `nome` e `cpf`.
*   **`ContaBancaria.java`**: Representa a conta em si. Contém a lógica de negócios para `depositar`, `sacar` e mantém o estado do `saldo`.
*   **`MyApp.java`**: Classe principal que contém o método `main`. Gerencia a interação com o usuário através de um menu no console.
*   **`diagrama.puml`**: Arquivo PlantUML contendo o diagrama de classes do sistema.

## 🚀 Como Executar

### Pré-requisitos

*   Ter o **Java JDK** (Java Development Kit) instalado na sua máquina (versão 8 ou superior recomendada).

### Passo a Passo

1.  **Clone o repositório** ou baixe os arquivos para uma pasta local.
2.  **Abra o terminal** na pasta onde os arquivos estão salvos.
3.  **Compile os arquivos Java**:
    ```bash
    javac *.java
    ```
4.  **Execute a aplicação**:
    ```bash
    java MyApp
    ```

## 🛠 Exemplo de Uso

Ao rodar o programa, você verá o seguinte menu:

```text
=== MENU ===
1 - Criar cliente e conta
2 - Depositar
3 - Sacar
4 - Ver dados da conta
0 - Sair
Escolha uma opção: 
```

Basta digitar o número da opção desejada e pressionar `Enter`.

## 📝 Diagrama de Classes

O projeto inclui um arquivo `diagrama.puml` que modela a relação entre as classes:
*   Uma `ContaBancaria` **possui** um `Cliente`.
*   A classe `MyApp` é responsável por instanciar e utilizar esses objetos.

---
Desenvolvido para fins educacionais na disciplina de POO.
