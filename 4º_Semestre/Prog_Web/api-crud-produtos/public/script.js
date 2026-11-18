const API_URL = '/produtos';

const lista = document.getElementById('lista-produtos');
const form = document.getElementById('form-produto');
const campoId = document.getElementById('produto-id');
const campoNome = document.getElementById('nome');
const campoCategoria = document.getElementById('categoria');
const campoPreco = document.getElementById('preco');
const campoEstoque = document.getElementById('estoque');
const btnSalvar = document.getElementById('btn-salvar');
const btnCancelar = document.getElementById('btn-cancelar');
const tituloForm = document.getElementById('titulo-form');
const caixaMensagem = document.getElementById('mensagem');

let temporizadorMensagem;

function mostrarMensagem(texto, tipo) {
  caixaMensagem.textContent = texto;
  caixaMensagem.className = tipo;
  caixaMensagem.hidden = false;
  clearTimeout(temporizadorMensagem);
  temporizadorMensagem = setTimeout(() => {
    caixaMensagem.hidden = true;
  }, 5000);
}

function formatarPreco(valor) {
  return valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
}

// Lê a mensagem de erro enviada pela API (400 ou 404)
async function lerErro(resposta) {
  try {
    const dados = await resposta.json();
    return dados.erro || 'Erro inesperado na requisição';
  } catch {
    return 'Erro inesperado na requisição';
  }
}

async function carregarProdutos() {
  try {
    const resposta = await fetch(API_URL);
    if (!resposta.ok) {
      mostrarMensagem(await lerErro(resposta), 'erro');
      return;
    }
    const produtos = await resposta.json();
    renderizarLista(produtos);
  } catch (erro) {
    mostrarMensagem('Não foi possível conectar ao servidor. Verifique se ele está rodando.', 'erro');
  }
}

function renderizarLista(produtos) {
  lista.replaceChildren();

  if (produtos.length === 0) {
    const vazio = document.createElement('li');
    vazio.className = 'vazio';
    vazio.textContent = 'Nenhum produto cadastrado. Use o formulário para adicionar o primeiro.';
    lista.appendChild(vazio);
    return;
  }

  produtos.forEach((produto) => {
    const item = document.createElement('li');

    const nome = document.createElement('span');
    nome.className = 'produto-nome';
    nome.textContent = produto.nome;

    const categoria = document.createElement('p');
    categoria.className = 'produto-info';
    categoria.textContent = `Categoria: ${produto.categoria}`;

    const estoque = document.createElement('p');
    estoque.className = 'produto-info';
    estoque.textContent = `Estoque: ${produto.estoque} un.`;

    const preco = document.createElement('p');
    preco.className = 'produto-preco';
    preco.textContent = formatarPreco(produto.preco);

    const acoes = document.createElement('div');
    acoes.className = 'acoes';

    const btnEditar = document.createElement('button');
    btnEditar.type = 'button';
    btnEditar.className = 'secundario';
    btnEditar.textContent = 'Editar';
    btnEditar.addEventListener('click', () => iniciarEdicao(produto));

    const btnExcluir = document.createElement('button');
    btnExcluir.type = 'button';
    btnExcluir.className = 'perigo';
    btnExcluir.textContent = 'Excluir';
    btnExcluir.addEventListener('click', () => excluirProduto(produto));

    acoes.append(btnEditar, btnExcluir);
    item.append(nome, categoria, estoque, preco, acoes);
    lista.appendChild(item);
  });
}

function iniciarEdicao(produto) {
  campoId.value = produto.id;
  campoNome.value = produto.nome;
  campoCategoria.value = produto.categoria;
  campoPreco.value = produto.preco;
  campoEstoque.value = produto.estoque;
  tituloForm.textContent = 'Editar produto';
  btnSalvar.textContent = 'Salvar alterações';
  btnCancelar.hidden = false;
  campoNome.focus();
}

function limparFormulario() {
  form.reset();
  campoId.value = '';
  tituloForm.textContent = 'Novo produto';
  btnSalvar.textContent = 'Cadastrar produto';
  btnCancelar.hidden = true;
}

async function salvarProduto(evento) {
  evento.preventDefault();

  const dados = {
    nome: campoNome.value,
    categoria: campoCategoria.value,
    preco: campoPreco.value === '' ? undefined : Number(campoPreco.value),
    estoque: campoEstoque.value === '' ? undefined : Number(campoEstoque.value)
  };

  const editando = campoId.value !== '';
  const url = editando ? `${API_URL}/${campoId.value}` : API_URL;
  const metodo = editando ? 'PUT' : 'POST';

  try {
    const resposta = await fetch(url, {
      method: metodo,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(dados)
    });

    if (!resposta.ok) {
      mostrarMensagem(await lerErro(resposta), 'erro');
      return;
    }

    mostrarMensagem(editando ? 'Produto atualizado com sucesso.' : 'Produto cadastrado com sucesso.', 'sucesso');
    limparFormulario();
    await carregarProdutos();
  } catch (erro) {
    mostrarMensagem('Não foi possível conectar ao servidor. Verifique se ele está rodando.', 'erro');
  }
}

async function excluirProduto(produto) {
  if (!confirm(`Deseja excluir o produto "${produto.nome}"?`)) {
    return;
  }

  try {
    const resposta = await fetch(`${API_URL}/${produto.id}`, { method: 'DELETE' });

    if (!resposta.ok) {
      mostrarMensagem(await lerErro(resposta), 'erro');
      await carregarProdutos();
      return;
    }

    mostrarMensagem('Produto excluído com sucesso.', 'sucesso');
    if (campoId.value === String(produto.id)) {
      limparFormulario();
    }
    await carregarProdutos();
  } catch (erro) {
    mostrarMensagem('Não foi possível conectar ao servidor. Verifique se ele está rodando.', 'erro');
  }
}

form.addEventListener('submit', salvarProduto);
btnCancelar.addEventListener('click', limparFormulario);
carregarProdutos();
