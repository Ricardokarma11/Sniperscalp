import streamlit as st
import os

# Page configuration
st.set_page_config(page_title="ScalpProp Premium", page_icon="⚡", layout="centered")

# CSS para estilo Premium/Marvel
st.markdown("""
    <style>
    .main { background-color: #0d1117; }
    .brand-title {
        text-align: center; color: #ffcc00 !important;
        font-family: 'Impact', 'Arial Black', sans-serif; font-size: 3rem;
        letter-spacing: 2px;
        text-shadow: -2px -2px 0 #000, 2px -2px 0 #000, -2px 2px 0 #000, 2px 2px 0 #000;
        margin-top: 10px;
    }
    .brand-subtitle { text-align: center; color: #8b949e; font-family: 'Courier New', monospace; font-size: 1rem; margin-top: -10px; }
    .stNumberInput div div input, .stTextInput div div input { background-color: #161b22 !important; color: white !important; border: 1px solid #30363d !important; }
    .stButton>button {
        background: linear-gradient(135deg, #00ff66 0%, #00cc52 100%) !important; color: #000000 !important;
        font-weight: bold !important; font-size: 1.1rem !important; border: 2px solid #000000 !important;
        box-shadow: 0px 0px 15px rgba(0, 255, 102, 0.6) !important;
    }
    </style>
""", unsafe_allow_html=True)

# LOGO: Apenas tenta mostrar se o ficheiro existir, caso contrário não faz nada
if os.path.exists("logo.png"):
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.png", use_container_width=True)

st.markdown("<h1 class='brand-title'>SCALPPROP</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>⚡ PREMIUM ⚡</p>", unsafe_allow_html=True)
st.write("---")

# Inputs
token = st.text_input("SEARCH TOKEN", value="SOL").upper()
saldo = st.number_input("PROPFIRM BALANCE ($)", value=5000, step=500)

if st.button("EXECUTE AUTOMATIC SCAN", use_container_width=True):
    st.success(f"Scan executed successfully for {token} inside the ScalpProp network!")
