# API REST de Jogos com Express

API simples feita com **Node.js** e **Express** para a disciplina de Programação Web do IFMT (Instituto Federal de Mato Grosso). Os dados ficam em um array dentro do código, sem banco de dados.

## Tecnologias

- Node.js
- Express

## Como executar

1. Clone o repositório e entre na pasta da atividade:

```bash
git clone https://github.com/sandrinimoraes-c/SI_IFMT.git
cd "SI_IFMT/4º_Semestre/Prog_Web/API REST com Express"
```

2. Instale as dependências:

```bash
npm install
```

3. Inicie o servidor:

```bash
node index.js
```

O servidor ficará disponível em `http://localhost:3000`.

## Estrutura dos dados

Cada jogo possui os campos:

| Campo        | Tipo   | Descrição                  |
|--------------|--------|----------------------------|
| `id`         | número | Identificador do jogo      |
| `nome`       | texto  | Nome do jogo               |
| `plataforma` | texto  | Plataforma principal       |
| `ano`        | número | Ano de lançamento          |

Exemplo:

```json
{
  "id": 1,
  "nome": "The Legend of Zelda: Breath of the Wild",
  "plataforma": "Nintendo Switch",
  "ano": 2017
}
```

## Rotas

| Método   | Rota         | Descrição                          | Respostas        |
|----------|--------------|------------------------------------|------------------|
| `GET`    | `/itens`     | Retorna a lista completa de jogos  | `200`            |
| `GET`    | `/itens/:id` | Retorna o jogo com o id informado  | `200`, `404`     |
| `DELETE` | `/itens/:id` | Remove o jogo com o id informado   | `204`, `404`     |

Quando o id não existe, a API responde com status `404` e o corpo:

```json
{ "erro": "Item não encontrado" }
```

## Exemplos de uso

```bash
# Listar todos os jogos
curl http://localhost:3000/itens

# Buscar um jogo pelo id
curl http://localhost:3000/itens/2

# Remover um jogo
curl -X DELETE http://localhost:3000/itens/2 -i
```

> Os dados ficam apenas em memória: ao reiniciar o servidor, os itens removidos voltam ao estado original.
