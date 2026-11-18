const express = require('express');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Dados em memória (reiniciam quando o servidor é reiniciado)
let produtos = [
  { id: 1, nome: 'Caderno universitário', categoria: 'Papelaria', preco: 24.9, estoque: 40 },
  { id: 2, nome: 'Mouse sem fio', categoria: 'Informática', preco: 59.9, estoque: 15 },
  { id: 3, nome: 'Garrafa térmica', categoria: 'Utilidades', preco: 79.0, estoque: 22 }
];
let proximoId = 4;

// Valida o corpo da requisição; retorna a mensagem de erro ou null
function validar(corpo) {
  if (!corpo || typeof corpo !== 'object') {
    return 'O corpo da requisição deve ser um JSON';
  }
  for (const campo of ['nome', 'categoria']) {
    if (typeof corpo[campo] !== 'string' || corpo[campo].trim() === '') {
      return `O campo ${campo} é obrigatório`;
    }
  }
  if (corpo.preco === undefined || corpo.preco === null || corpo.preco === '') {
    return 'O campo preco é obrigatório';
  }
  if (typeof corpo.preco !== 'number' || Number.isNaN(corpo.preco) || corpo.preco < 0) {
    return 'O campo preco deve ser um número maior ou igual a 0';
  }
  if (corpo.estoque === undefined || corpo.estoque === null || corpo.estoque === '') {
    return 'O campo estoque é obrigatório';
  }
  if (!Number.isInteger(corpo.estoque) || corpo.estoque < 0) {
    return 'O campo estoque deve ser um número inteiro maior ou igual a 0';
  }
  return null;
}

function buscarPorId(req) {
  const id = Number(req.params.id);
  return produtos.find((p) => p.id === id);
}

// GET /produtos - lista todos
app.get('/produtos', (req, res) => {
  res.status(200).json(produtos);
});

// GET /produtos/:id - retorna um
app.get('/produtos/:id', (req, res) => {
  const produto = buscarPorId(req);
  if (!produto) {
    return res.status(404).json({ erro: 'Produto não encontrado' });
  }
  res.status(200).json(produto);
});

// POST /produtos - cadastra
app.post('/produtos', (req, res) => {
  const erro = validar(req.body);
  if (erro) {
    return res.status(400).json({ erro });
  }
  const { nome, categoria, preco, estoque } = req.body;
  const novo = { id: proximoId++, nome: nome.trim(), categoria: categoria.trim(), preco, estoque };
  produtos.push(novo);
  res.status(201).json(novo);
});

// PUT /produtos/:id - atualiza
app.put('/produtos/:id', (req, res) => {
  const produto = buscarPorId(req);
  if (!produto) {
    return res.status(404).json({ erro: 'Produto não encontrado' });
  }
  const erro = validar(req.body);
  if (erro) {
    return res.status(400).json({ erro });
  }
  const { nome, categoria, preco, estoque } = req.body;
  produto.nome = nome.trim();
  produto.categoria = categoria.trim();
  produto.preco = preco;
  produto.estoque = estoque;
  res.status(200).json(produto);
});

// DELETE /produtos/:id - remove
app.delete('/produtos/:id', (req, res) => {
  const produto = buscarPorId(req);
  if (!produto) {
    return res.status(404).json({ erro: 'Produto não encontrado' });
  }
  produtos = produtos.filter((p) => p.id !== produto.id);
  res.status(204).send();
});

app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});
