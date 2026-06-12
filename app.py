import streamlit as st
from tradingview_ta import TA_Handler, Interval, Exchange

# Configuração da página
st.set_page_config(page_title="Scalp Prop - Premium", layout="centered")

# Função para buscar preço no TradingView
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

# Estilização CSS
st.markdown("""
<style>
    :root { --bg-color: #0b0c10; --card-bg: rgba(22, 25, 37, 0.9); --gold-color: #d4af37; --text-color: #ffffff; }
    .app-container { background-color: var(--card-bg); border: 1px solid var(--gold-color); border-radius: 14px; padding: 20px; }
    h2 { color: var(--gold-color); text-transform: uppercase; margin: 0; }
</style>
""", unsafe_allow_html=True)

# Layout
st.markdown('<div class="app-container">', unsafe_allow_html=True)
st.markdown("<h2>SCALP PROP</h2>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Lógica de Interação
token = st.text_input("Procurar Token (ex: BTC, SOL)", "BTC").upper()
# Garantir que todos os valores numéricos são floats (ex: 5000.0) para evitar o erro de tipo
banca = st.number_input("Saldo Bitfunded ($)", value=5000.0, format="%.2f")
entrada = st.number_input("Preço de Entrada ($)", value=0.0, format="%.2f")
sl = st.number_input("Preço de Stop Loss ($)", value=0.0, format="%.2f")

if st.button("Executar Scan Automático"):
    preco_atual = get_price(token)
    if preco_atual:
        st.success(f"✅ Preço de {token} encontrado: ${preco_atual:.2f}")
        
        # Cálculo de segurança
        dist = abs(entrada - sl)
        if entrada > 0 and sl > 0 and dist > 0:
            risco = banca * 0.0025
            lote = risco / dist
            st.metric("Lote Sugerido", f"{lote:.4f} {token}")
            alvo1 = (entrada + (dist*2)) if entrada > sl else (entrada - (dist*2))
            st.write(f"**Alvo 1 (1:2):** ${alvo1:.2f}")
        else:
            st.warning("⚠️ Insira valores de Entrada e Stop válidos.")
    else:
        st.error(f"❌ Não foi possível rastrear o par {token}USDT.")
