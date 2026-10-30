const express = require("express");
const app = express();

let itens = [
  { id: 1, nome: "The Legend of Zelda: Breath of the Wild", plataforma: "Nintendo Switch", ano: 2017 },
  { id: 2, nome: "Minecraft", plataforma: "Multiplataforma", ano: 2011 },
  { id: 3, nome: "The Witcher 3", plataforma: "PC", ano: 2015 },
  { id: 4, nome: "God of War", plataforma: "PlayStation", ano: 2018 },
  { id: 5, nome: "Celeste", plataforma: "Multiplataforma", ano: 2018 },
];

app.get("/itens", (req, res) => {
  res.json(itens);
});

app.get("/itens/:id", (req, res) => {
  const id = Number(req.params.id);
  const item = itens.find((i) => i.id === id);

  if (!item) {
    return res.status(404).json({ erro: "Item não encontrado" });
  }
  res.json(item);
});

app.delete("/itens/:id", (req, res) => {
  const id = Number(req.params.id);
  const indice = itens.findIndex((i) => i.id === id);

  if (indice === -1) {
    return res.status(404).json({ erro: "Item não encontrado" });
  }
  itens.splice(indice, 1);
  res.status(204).send();
});

app.listen(3000, () => {
  console.log("Servidor rodando em http://localhost:3000");
});