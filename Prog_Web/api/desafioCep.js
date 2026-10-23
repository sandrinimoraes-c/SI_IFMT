async function buscarDdd(ddd) {
  try {
    const resposta = await fetch(`https://brasilapi.com.br/api/ddd/v1/${ddd}`);

    if (!resposta.ok) {
      throw new Error(`DDD inválido ou erro na API (status ${resposta.status})`);
    }

    const dados = await resposta.json();

    console.log(`1. Estado: ${dados.state}`);
    console.log(`2. Quantidade de cidades: ${dados.cities.length}`);
    console.log("3. Cidades:");
    dados.cities.forEach((cidade, i) => {
      console.log(`${i + 1}. ${cidade}`);
    });
  } catch (erro) {
    console.error("Erro ao buscar DDD:", erro.message);
  }
}

buscarDdd("65");