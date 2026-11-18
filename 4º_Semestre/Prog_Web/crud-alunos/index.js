const express = require("express");
const app = express();

app.use(express.json());

let alunos = [
  { id: 1, nome: "Sandrini Moraes Correa", curso: "Sistemas de Informação"},
  { id: 2, nome: "Fulano de Tal", curso: "Sistemas de Informação"},
];
let proximoId = 3;

// Rota para listar todos os alunos
app.get("/alunos", (req, res) => {
  res.json(alunos);
});

// Rota para buscar um aluno pelo ID
app.get("/alunos/:id", (req, res) => {
  const aluno = alunos.find((a) => a.id === parseInt(req.params.id));
  if (!aluno) return res.status(404).send("Aluno não encontrado.");
  res.json(aluno);
});

app.post("/alunos", (req, res) => {
  const { nome, curso } = req.body;
  const novoAluno = { id: proximoId++, nome, curso };
  alunos.push(novoAluno);
  res.status(201).json(novoAluno);
});

app.delete("/alunos/:id", (req, res) => {
  const id = Number(req.params.id);
  const existe = alunos.some((item) => item.id === id);
  if (!existe) 
    return res.status(404).send("Aluno não encontrado.");

  alunos = alunos.filter((item) => item.id !== id);
  res.status(204).send("Aluno removido com sucesso.");
});

app.listen(3000, () => {
  console.log("Servidor rodando em http://localhost:3000");
});

