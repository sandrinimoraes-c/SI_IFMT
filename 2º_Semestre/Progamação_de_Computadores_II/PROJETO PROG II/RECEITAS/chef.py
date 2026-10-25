import json # Biblioteca para ler o arquivo
import os   # Biblioteca para verificar se o arquivo existe

def carregar_receitas():
    nome_arquivo = 'receitas.json'
    
    # Verificação de segurança: O arquivo existe?
    if not os.path.exists(nome_arquivo):
        print(f"ERRO: O arquivo '{nome_arquivo}' não foi encontrado!")
        return []
    
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            return dados
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []

def chef_python_inteligente():
    print("--- 👨‍🍳 CHEF PYTHON v3.0 (Versão JSON) ---")
    
    # 1. CARREGAR DADOS DO ARQUIVO
    livro_receitas = carregar_receitas()
    
    if not livro_receitas:
        return # Para o programa se não tiver receitas
        
    print(f"📚 {len(livro_receitas)} receitas carregadas com sucesso.")
    print("Dica: Tente 'ovo, sal, oleo, farinha, acucar'")
    
    entrada = input("\nO que tem na geladeira? (separe por virgula): ")

    # 2. LIMPEZA DE DADOS
    na_geladeira = set([item.strip().lower() for item in entrada.split(",")])

    match_exato = []
    quase_la = []

    # 3. ALGORITMO DE BUSCA
    for receita in livro_receitas:
        # CONVERSÃO IMPORTANTE:
        # No JSON, os ingredientes vêm como LISTA [].
        # Precisamos transformar em SET {} agora para fazer a conta de menos (-).
        necessarios = set(receita["ingredientes"])
        
        itens_faltantes = necessarios - na_geladeira
        qtd_falta = len(itens_faltantes)

        if qtd_falta == 0:
            match_exato.append(receita["nome"])
        
        elif qtd_falta <= 2:
            detalhe = f"{receita['nome']} (Falta: {', '.join(itens_faltantes)})"
            quase_la.append(detalhe)

    # 4. EXIBIÇÃO (igual ao anterior)
    print("\n" + "="*30)
    
    if match_exato:
        print(f"✅ VOCÊ PODE FAZER AGORA ({len(match_exato)}):")
        for prato in match_exato:
            print(f"   - {prato}")
    else:
        print("❌ Nenhuma receita exata encontrada.")

    print("-" * 30)

    if quase_la:
        print(f"🛒 FALTA POUCO PARA ({len(quase_la)}):")
        for item in quase_la:
            print(f"   - {item}")
    else:
        print("ℹ️ Nenhuma sugestão próxima encontrada.")
        
    print("="*30)

# Executar
if __name__ == "__main__":
    chef_python_inteligente()