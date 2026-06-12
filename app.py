import streamlit as st

# Page configuration
st.set_page_config(
    page_title="ScalpProp Premium",
    page_icon="🎯",
    layout="centered"
)

# Custom CSS for Dark/Gold Premium theme
st.markdown("""
    <style>
    .main { background-color: #0d1117; }
    h1, h2, h3 { color: #ffd700 !important; font-family: 'Courier New', monospace; }
    .stNumberInput div div input { background-color: #161b22 !important; color: white !important; }
    .stTextInput div div input { background-color: #161b22 !important; color: white !important; }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<h1 style='text-align: center;'>🎯 SCALPPROP • PREMIUM</h1>", unsafe_allow_html=True)
st.write("---")

# Inputs
token = st.text_input("SEARCH TOKEN", value="SOL").upper()
saldo = st.number_input("BITFUNDED BALANCE ($)", value=5000, step=500)

st.write("---")

# Action Button
if st.button("EXECUTE AUTOMATIC SCAN", use_container_width=True):
    st.success(f"Scan executed successfully for {token}!")
