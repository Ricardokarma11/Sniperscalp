import streamlit as st
from tradingview_ta import TA_Handler, Interval, Exchange

# Configuração da página
st.set_page_config(page_title="Scalp Prop - Premium", layout="centered")

# Função para buscar o preço real via TradingView
def get_price(token):
    try:
        handler = TA_Handler(
            symbol=f"{token}USDT",
            screener="crypto",
            exchange="BINANCE",
            interval=Interval.INTERVAL_1_MINUTE
        )
        analysis = handler.get_analysis()
        return analysis.indicators["close"]
    except:
        return None

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

# Layout
st.markdown('<div class="app-container">', unsafe_allow_html=True)
st.markdown("<h2>SCALP PROP <span>PREMIUM</span></h2>", unsafe_allow_html=True)

token = st.text_input("Token", "BTC").upper()
banca = st.number_input("Saldo Bitfunded ($)", value=5000.0)

# Botão para buscar preço atual
if st.button("Obter Preço Atual"):
    preco_atual = get_price(token)
    if preco_atual:
        st.success(f"Preço atual de {token}: ${preco_atual:.2f}")
        st.session_state['preco_atual'] = preco_atual
    else:
        st.error(f"Não foi possível rastrear o par {token}USDT.")

entrada = st.number_input("Preço Entrada ($)", value=st.session_state.get('preco_atual', 0.0), step=0.01)
sl = st.number_input("Preço Stop Loss ($)", value=0.0, step=0.01)

if st.button("Calcular Matriz"):
    if entrada > 0 and sl > 0 and entrada != sl:
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
    else:
        st.warning("Por favor, insira preços de Entrada e Stop válidos.")

st.markdown('</div>', unsafe_allow_html=True)
