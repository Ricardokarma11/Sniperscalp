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

# Interface Visual (HTML/CSS)
html_code = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <style>
        :root { --bg-color: #0b0c10; --card-bg: rgba(22, 25, 37, 0.9); --gold-color: #d4af37; --text-color: #ffffff; }
        body { font-family: sans-serif; background-color: var(--bg-color); color: var(--text-color); margin: 0; padding: 10px; }
        .app-container { background-color: var(--card-bg); border: 1px solid var(--gold-color); border-radius: 14px; padding: 20px; }
        h2 { color: var(--gold-color); text-transform: uppercase; border-bottom: 1px solid #333; margin: 0; }
    </style>
</head>
<body>
    <div class="app-container">
        <h2>SCALP PROP</h2>
    </div>
</body>
</html>
"""

components.html(html_code, height=100)

# Lógica de Interação no Streamlit
st.subheader("Configuração da Operação")
token = st.text_input("Procurar Token (ex: BTC, SOL, ETH)", "BTC").upper()
banca = st.number_input("Saldo Bitfunded ($)", value=5000.0)
entrada = st.number_input("Preço de Entrada ($)", value=0.0, step=0.01)
sl = st.number_input("Preço de Stop Loss ($)", value=0.0, step=0.01)

if st.button("Executar Scan Automático"):
    preco_atual = get_price(token)
    
    if preco_atual:
        st.success(f"✅ Preço de {token} encontrado: ${preco_atual}")
        
        # Cálculo básico de Risco
        dist = abs(entrada - sl)
        risco = banca * 0.0025
        lote = risco / dist
        
        st.write(f"**Lote sugerido:** {lote:.4f} {token}")
        st.write(f"**Alvo 1 (1:2):** {(entrada + (dist*2)) if entrada > sl else (entrada - (dist*2)):.2f}")
    else:
        st.error(f"❌ Não foi possível rastrear o par {token}USDT. Verifica se o nome está correto.")
