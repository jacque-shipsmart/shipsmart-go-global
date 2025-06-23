
import streamlit as st
import random
import json
import game_logic

# --- Configuração da página ---
st.set_page_config(
    page_title="ShipSmart Go Global",
    page_icon="🌎",
    layout="centered"
)

# --- Logo e título ---
st.markdown(
    f'<img src="https://shipsmart.global/wp-content/uploads/2025/04/logo-shipsmart.png" width="180">',
    unsafe_allow_html=True
)

st.markdown("<h1 style='font-family:Inter; color:#151383;'>ShipSmart Go Global</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-family:Inter; font-size:1rem;'>🎯 Sua missão: levar sua marca do Brasil para o mundo superando os desafios do comércio cross-border.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Carregar dados do jogo ---
casas, cartas = game_logic.carregar_dados()
max_casas = len(casas)

# --- Estado do jogador ---
if "posicao" not in st.session_state:
    st.session_state.posicao = 0

if "mensagem_carta" not in st.session_state:
    st.session_state.mensagem_carta = ""

# --- Exibir casa atual ---
casa_atual = casas[st.session_state.posicao]
st.markdown(f"<h4 style='color:#1F1CBF;'>📍 Etapa atual: {casa_atual['titulo']}</h4>", unsafe_allow_html=True)
st.markdown(f"<p style='font-size:1rem'>{casa_atual['descricao']}</p>", unsafe_allow_html=True)

# --- Botão para jogar dado ---
if st.button("🎲 Jogar dado"):
    dado = game_logic.jogar_dado()
    st.success(f"Você tirou {dado} no dado!")

    nova_pos = game_logic.obter_proxima_casa(st.session_state.posicao, dado, max_casas)
    st.session_state.posicao = nova_pos

    # Sorteia uma carta aleatória (20% de chance)
    if random.random() < 0.2:
        carta = random.choice(cartas)
        st.session_state.posicao = max(0, min(st.session_state.posicao + carta["movimento"], max_casas - 1))
        tipo = "✅" if carta["tipo"] == "bonus" else "⚠️"
        st.session_state.mensagem_carta = f"{tipo} {carta['mensagem']}"
    else:
        st.session_state.mensagem_carta = ""

# --- Mostrar carta se houver ---
if st.session_state.mensagem_carta:
    st.info(st.session_state.mensagem_carta)

# --- Progresso ---
progresso = (st.session_state.posicao + 1) / max_casas
st.progress(progresso, text=f"{int(progresso * 100)}% da jornada concluída")
