import streamlit as st
import json
import os

# --- LÓGICA DE BACKEND (Igual ao anterior) ---
def carregar_receitas():
    # Verifica se o arquivo existe, senão cria um exemplo na memória
    if not os.path.exists('receitas.json'):
        return []
    try:
        with open('receitas.json', 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except Exception:
        return []

def buscar_receitas(ingredientes_usuario, livro_receitas):
    # Transforma input do usuário em conjunto (Set)
    na_geladeira = set([item.strip().lower() for item in ingredientes_usuario.split(",")])
    
    match_exato = []
    quase_la = []

    for receita in livro_receitas:
        necessarios = set(receita["ingredientes"])
        # Diferença de conjuntos (Matemática)
        itens_faltantes = necessarios - na_geladeira
        qtd_falta = len(itens_faltantes)

        if qtd_falta == 0:
            match_exato.append(receita)
        elif qtd_falta <= 2:
            # Adiciona o que falta no dicionário da receita para exibir depois
            receita["faltam"] = list(itens_faltantes) 
            quase_la.append(receita)
            
    return match_exato, quase_la

# --- INTERFACE GRÁFICA (Frontend) ---

# Configuração da Página
st.set_page_config(page_title="Chef Python", page_icon="👨‍🍳")

# Título e Subtítulo
st.title("👨‍🍳 Chef Python")
st.write("Descubra o que cozinhar com o que você tem em casa!")

# Barra lateral (Sidebar) para informações extras
with st.sidebar:
    st.header("Sobre o Projeto")
    st.info("Projeto Acadêmico - 2º Semestre SI")
    st.write("Este sistema utiliza **Teoria dos Conjuntos** para encontrar a melhor receita para você.")

# Entrada de Dados
entrada = st.text_area("O que tem na geladeira?", placeholder="Ex: ovo, sal, leite, farinha...")

# Botão de Ação
if st.button("Buscar Receitas 🔎"):
    if not entrada:
        st.warning("Por favor, digite alguns ingredientes!")
    else:
        livro = carregar_receitas()
        
        if not livro:
            st.error("Arquivo 'receitas.json' não encontrado!")
        else:
            exatos, proximos = buscar_receitas(entrada, livro)
            
            # --- RECEITAS EXATAS ---
            st.subheader(f"✅ Você pode fazer agora ({len(exatos)})")
            if exatos:
                for r in exatos:
                    # O expander cria a caixinha que abre e fecha
                    with st.expander(f"**{r['nome']}** (Dificuldade: {r['dificuldade']})"):
                        
                        st.markdown("#### 🛒 Ingredientes")
                        st.write(", ".join(r['ingredientes']))
                        
                        st.markdown("#### 👩‍🍳 Modo de Preparo")
                        # Aqui fazemos um loop para mostrar passo a passo
                        for i, passo in enumerate(r['preparo'], 1):
                            st.write(f"{i}. {passo}")
                            
                        st.success("Pronto para cozinhar!")
            else:
                st.info("Nenhuma receita exata encontrada.")
            
            st.divider() 
            
            # --- RECEITAS APROXIMADAS ---
            st.subheader(f"🛒 Falta pouco para ({len(proximos)})")
            if proximos:
                for r in proximos:
                    with st.expander(f"**{r['nome']}**"):
                        # Mostra o que falta em vermelho (destaque visual)
                        st.error(f"⚠️ Falta comprar: {', '.join(r['faltam'])}")
                        
                        st.markdown("#### 🛒 Ingredientes Necessários")
                        st.write(", ".join(r['ingredientes']))

                        st.markdown("#### 👩‍🍳 Modo de Preparo")
                        for i, passo in enumerate(r['preparo'], 1):
                            st.write(f"{i}. {passo}")
            else:
                 st.write("Nenhuma sugestão próxima.")