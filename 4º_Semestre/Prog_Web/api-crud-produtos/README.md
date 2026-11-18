# API CRUD de Produtos

- **Estudante:** Sandrini
- **Componente curricular:** Programação Web, IFMT (4º semestre, noturno)
- **Tema escolhido:** Produtos

## Descrição do recurso

Cada **produto** possui os campos:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | número | Gerado automaticamente pela API |
| `nome` | texto | Nome do produto (obrigatório) |
| `categoria` | texto | Categoria do produto (obrigatório) |
| `preco` | número | Preço em reais, maior ou igual a 0 (obrigatório) |
| `estoque` | inteiro | Quantidade em estoque, maior ou igual a 0 (obrigatório) |

Os dados ficam em um array em memória: ao reiniciar o servidor, voltam aos 3 itens de exemplo.

## Como executar

```bash
npm install
node index.js
```

Depois, abra no navegador: <http://localhost:3000>

## Testando a API pelo terminal

**GET /produtos** (lista todos, 200)

```bash
curl -i -X GET http://localhost:3000/produtos
```

**GET /produtos/:id** (retorna um, 200 ou 404)

```bash
curl -i -X GET http://localhost:3000/produtos/1
```

**POST /produtos** (cadastra, 201 ou 400)

```bash
curl -i -X POST http://localhost:3000/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome":"Teclado mecânico","categoria":"Informática","preco":249.9,"estoque":8}'
```

**PUT /produtos/:id** (atualiza, 200, 400 ou 404)

```bash
curl -i -X PUT http://localhost:3000/produtos/1 \
  -H "Content-Type: application/json" \
  -d '{"nome":"Caderno 10 matérias","categoria":"Papelaria","preco":29.9,"estoque":35}'
```

**DELETE /produtos/:id** (remove, 204 ou 404)

```bash
curl -i -X DELETE http://localhost:3000/produtos/1
```

Para ver um erro 400, envie um POST sem o campo `nome`; para ver um 404, use um id que não existe, como `/produtos/999`.
