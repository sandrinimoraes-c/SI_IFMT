# Plataforma de Agendamento de Consultas Médicas

Projeto acadêmico (IFMT) — arquitetura em camadas, DAO + Factory,
JavaFX + MySQL.

## Estrutura de pastas

```
src/main/java/com/clinica/
├── model/        → Paciente, Medico, Agendamento (entidades simples)
├── dao/          → Interfaces (contratos): PacienteDAO, MedicoDAO, AgendamentoDAO
├── dao/impl/     → Implementações com SQL real (único lugar com SQL)
├── factory/      → ConexaoFactory (cria Connection) e DAOFactory (cria os DAOs)
└── view/         → Telas JavaFX em uma única janela com abas (MainApp, CadastroPacienteView, CadastroMedicoView, AgendamentoView)

src/main/resources/
└── styles.css    → folha de estilo (cores, espaçamento, cantos arredondados)

sql/
└── criar_banco.sql   → script para criar o banco e as tabelas no MySQL
```

## Sobre a interface

A partir desta versão, o sistema abre em **uma única janela** com 3 abas
(Pacientes, Médicos, Agendamentos), em vez de 3 janelas separadas.

Cada classe `View` não abre mais sua própria janela (`Stage`) — em vez
disso, tem um método `getContent()` que devolve o formulário como um
`Node`, que a `MainApp` encaixa dentro de cada aba (`Tab`). A lógica de
DAO/Factory continua exatamente igual; só a forma de exibir mudou.

O visual é definido pelo arquivo `src/main/resources/styles.css`,
carregado pela `MainApp`. Para mudar cores ou espaçamentos, edite só
esse arquivo — não precisa tocar no código Java.

## Como configurar e rodar

### 1. Pré-requisitos
- JDK 17 ou superior instalado
- Maven instalado
- MySQL Server rodando localmente (porta padrão 3306)

### 2. Criar o banco de dados
Abra o MySQL Workbench (ou terminal `mysql -u root -p`) e execute o
arquivo `sql/criar_banco.sql`. Isso cria o banco `clinica_db` com as
tabelas `paciente`, `medico` e `agendamento`, já com alguns dados de
exemplo.

### 3. Configurar a senha do banco
Abra o arquivo:
```
src/main/java/com/clinica/factory/ConexaoFactory.java
```
E troque a linha:
```java
private static final String SENHA = "SUA_SENHA_AQUI";
```
pela senha real do seu usuário `root` do MySQL.

Se seu MySQL roda em outra porta ou outro usuário, ajuste também
`URL` e `USUARIO` nessa mesma classe.

### 4. Rodar o projeto
Na raiz do projeto (onde está o `pom.xml`), execute:

```bash
mvn clean javafx:run
```

A tela principal (menu) deve abrir com 3 botões: Pacientes, Médicos
e Agendamentos.

## Como o projeto atende cada requisito do edital

| Requisito do edital | Onde está no código |
|---|---|
| Arquitetura em camadas (model/persistência/visão) | Pastas `model`, `dao`+`dao/impl`, `view` |
| Padrão DAO | Interfaces em `dao/` + implementações em `dao/impl/` |
| Padrão Factory + polimorfismo | `factory/DAOFactory.java` (retorna o tipo da interface, ex.: `PacienteDAO`, mas a instância real é `PacienteDAOImpl`) |
| Encapsulamento — proibição de SQL na GUI | Nenhum arquivo em `view/` contém SQL; todos chamam métodos do DAO |
| Interface gráfica | JavaFX (`view/MainApp.java` e demais telas) |
| Cadastro de Paciente e Médico | `CadastroPacienteView`, `CadastroMedicoView` |
| Tela de Agendamento (vínculo data/hora) | `AgendamentoView` |
| Impedir 2 consultas no mesmo horário p/ mesmo médico | `AgendamentoDAOImpl.existeConflito()`, chamado dentro de `salvar()` antes do INSERT |
| Mapeamento no banco | `sql/criar_banco.sql` — tabelas `paciente`, `medico`, `agendamento` |

## Dica para a apresentação/relatório

Se for explicar o fluxo para o professor, use esta sequência:

1. Usuário clica em "Agendar" na tela (`AgendamentoView`)
2. A tela chama `agendamentoDAO.salvar(agendamento)` — não sabe nem
   se importa como isso é feito
3. Dentro de `AgendamentoDAOImpl.salvar()`, primeiro verifica-se
   `existeConflito()` com um SELECT
4. Se houver conflito, lança exceção e a tela mostra um alerta
5. Se não houver conflito, executa o INSERT

Isso demonstra a separação de camadas e o encapsulamento da regra
de negócio na camada de persistência.
