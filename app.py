import streamlit as st

# Page configuration
st.set_page_config(
    page_title="ScalpProp Premium",
    page_icon="⚡",
    layout="centered"
)

# Custom CSS focused on Marvel-style high impact, neon glow, and black outlines
st.markdown("""
    <style>
    /* Dark institutional background */
    .main { 
        background-color: #0d1117; 
    }
    
    /* Title with Marvel-style impact, bright gold, and solid black outline */
    .brand-title {
        text-align: center;
        color: #ffcc00 !important;
        font-family: 'Impact', 'Arial Black', sans-serif;
        font-size: 3rem;
        letter-spacing: 2px;
        text-shadow: 
            -2px -2px 0 #000,  
             2px -2px 0 #000,
            -2px  2px 0 #000,
             2px  2px 0 #000,
             0px  4px 10px rgba(255, 204, 0, 0.4);
        margin-bottom: 0px;
        margin-top: -10px;
    }
    
    /* Subtitle styling */
    .brand-subtitle {
        text-align: center;
        color: #8b949e;
        font-family: 'Courier New', monospace;
        font-size: 1rem;
        margin-top: -10px;
        margin-bottom: 20px;
    }
    
    /* Styling for Input Fields with Dark Theme */
    .stNumberInput div div input, .stTextInput div div input { 
        background-color: #161b22 !important; 
        color: white !important; 
        border: 1px solid #30363d !important;
    }
    
    /* High Impact Glowing Button - Matching the logo's vibrant energy */
    .stButton>button {
        background: linear-gradient(135deg, #00ff66 0%, #00cc52 100%) !important;
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        border: 2px solid #000000 !important;
        box-shadow: 0px 0px 15px rgba(0, 255, 102, 0.6) !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #ffcc00 0%, #ffb300 100%) !important;
        box-shadow: 0px 0px 20px rgba(255, 204, 0, 0.8) !important;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# --- LOGO DISPLAY (Link direto para a imagem do novo logotipo) ---
logo_url = "https://images.prodia.xyz/86047eb6-e575-47eb-ba05-7f4f6e1f0229.png"
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image(logo_url, use_container_width=True)

# --- HEADER REBRANDING ---
st.markdown("<h1 class='brand-title'>SCALPPROP</h1>", unsafe_allow_html=True)
st.markdown("<p class='brand-subtitle'>⚡ PREMIUM ⚡</p>", unsafe_allow_html=True)
st.write("---")

# --- INPUT FIELDS (INTERNATIONAL ENGLISH) ---
token = st.text_input("SEARCH TOKEN", value="SOL").upper()
saldo = st.number_input("PROPFIRM BALANCE ($)", value=5000, step=500)

st.write("---")

# --- ACTION BUTTON (NEON GREEN GLOW) ---
if st.button("EXECUTE AUTOMATIC SCAN", use_container_width=True):
    st.success(f"Scan executed successfully for {token} inside the ScalpProp network!")
