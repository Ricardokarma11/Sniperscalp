import streamlit as st
import pandas as pd
import os

# Configuração da Página
st.set_page_config(page_title="ScalpProp Premium", page_icon="⚡", layout="centered")

# CSS Estilo Marvel/Premium
st.markdown("""
    <style>
    .main { background-color: #0d1117; }
    .brand-title {
        text-align: center; color: #ffcc00 !important;
        font-family: 'Impact', 'Arial Black', sans-serif; font-size: 3rem;
        letter-spacing: 2px;
        text-shadow: -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, 2px 2px 0 #000;
    }
    .brand-subtitle { text-align: center; color: #8b949e; font-family: 'Courier New', monospace; font-size: 1rem; margin-bottom: 20px; }
    .stButton>button {
        background: linear-gradient(135deg, #00ff66 0%, #00cc52 100%) !important; 
        color: #000000 !important; font-weight: bold !important;
        border: 2px solid #000000 !important;
        box-shadow: 0px 0px 15px rgba(0, 255, 102, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1 class='brand-title'>SCALPPROP</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>⚡ PREMIUM ⚡</p>", unsafe_allow_html=True)

# Inputs
token = st.text_input("SEARCH TOKEN", value="BTC").upper()
saldo = st.number_input("PROPFIRM BALANCE ($)", value=5000, step=500)

# A Lógica do Scan e da Tabela
if st.button("EXECUTE AUTOMATIC SCAN", use_container_width=True):
    with st.spinner('Scanning network...'):
        # Simulação de dados de mercado
        data = {
            "Signal": ["BUY", "SELL", "BUY"],
            "Entry": [65000.50, 65200.00, 64900.20],
            "Target": [66000.00, 64500.00, 65500.00],
            "Confidence": ["92%", "88%", "95%"]
        }
        df = pd.DataFrame(data)
        
        st.success(f"Scan executed successfully for {token} inside the ScalpProp network!")
        
        # AQUI É ONDE A TABELA APARECE
        st.subheader("Analysis Results")
        st.table(df) # Isto exibe a tabela que estavas à espera
