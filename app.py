import streamlit as st

# Configuração da página
st.set_page_config(page_title="ScalpProp - Mobile V1", layout="centered")

# Estilização CSS Original
st.markdown("""
<style>
    :root {
        --bg-color: #0b0c10;
        --card-bg: rgba(22, 25, 37, 0.9);
        --gold-color: #d4af37;
        --text-color: #ffffff;
    }
    .app-container {
        background-color: var(--card-bg);
        border: 1px solid var(--gold-color);
        border-radius: 14px;
        padding: 20px;
    }
    h2 { color: var(--gold-color); text-transform: uppercase; }
</style>
""", unsafe_allow_html=True)

# Layout Original
st.markdown('<div class="app-container">', unsafe_allow_html=True)
st.markdown("<h2>ScalpProp <span>MOBILE V1</span></h2>", unsafe_allow_html=True)

token = st.text_input("Token", "SOL")
tipo_trade = st.selectbox("Operação", ["SCALP", "LIMIT"])
banca = st.number_input("Saldo Bitfunded ($)", value=5000.0)
entrada = st.number_input("Preço Entrada ($)", value=140.00, step=0.01)
sl = st.number_input("Preço Stop Loss ($)", value=138.50, step=0.01)

if st.button("Calcular Matriz"):
    # Lógica de cálculo original
    risco_percentual = 0.0025
    capital_em_risco = banca * risco_percentual
    dist_absoluta = abs(entrada - sl)
    direcao = "LONG" if entrada > sl else "SHORT"
    lote_moedas = capital_em_risco / dist_absoluta
    
    st.write(f"**Modo:** {direcao}")
    st.write(f"**Lote sugerido:** {lote_moedas:.4f} {token}")
    st.write(f"**TP1 (1:2):** {(entrada + (dist_absoluta*2)) if direcao == 'LONG' else (entrada - (dist_absoluta*2)):.4f}")
    st.write(f"**TP2 (1:4):** {(entrada + (dist_absoluta*4)) if direcao == 'LONG' else (entrada - (dist_absoluta*4)):.4f}")
    st.write(f"**TP3 (1:6):** {(entrada + (dist_absoluta*6)) if direcao == 'LONG' else (entrada - (dist_absoluta*6)):.4f}")

st.markdown('</div>', unsafe_allow_html=True)
