import streamlit as st
import streamlit.components.v1 as components
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

# Cabeçalho Estilizado
components.html("""
<div style="background-color: rgba(22, 25, 37, 0.9); border: 1px solid #d4af37; border-radius: 14px; padding: 15px; text-align: center;">
    <h2 style="color: #d4af37; text-transform: uppercase; margin: 0;">Scalp Prop</h2>
</div>
""", height=80)

# Lógica de Interação
st.write("---")
token = st.text_input("Procurar Token (ex: BTC, SOL)", "BTC").upper()
banca = st.number_input("Saldo Bitfunded ($)", value=5000.0)
col1, col2 = st.columns(2)
with col1:
    entrada = st.number_input("Preço de Entrada ($)", value=0.0, step=0.01)
with col2:
    sl = st.number_input("Preço de Stop ($)", value=0.0, step=0.01)

if st.button("Executar Scan Automático"):
    preco_atual = get_price(token)
    if preco_atual:
        st.success(f"✅ Preço Atual: ${preco_atual}")
        dist = abs(entrada - sl)
        risco = banca * 0.0025
        lote = risco / dist
        
        st.metric(label="Lote Sugerido", value=f"{lote:.4f} {token}")
        st.write(f"**Alvo 1 (1:2):** {(entrada + (dist*2)) if entrada > sl else (entrada - (dist*2)):.2f}")
    else:
        st.error(f"❌ Não foi possível encontrar {token}USDT.")
