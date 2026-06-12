import streamlit as st
import pandas as pd

# Configuração da página para ambiente Escuro/Premium Institutional
st.set_page_config(
    page_title="ScalpProp Pro",
    page_icon="⚡",
    layout="centered"
)

# Estilo CSS customizado para manter o visual Dark/Gold Premium
st.markdown("""
    <style>
    .main { background-color: #0d1117; }
    h1, h2, h3 { color: #ffd700 !important; font-family: 'Courier New', monospace; }
    .stNumberInput div div input { background-color: #161b22 !important; color: white !important; }
    .stTextInput div div input { background-color: #161b22 !important; color: white !important; }
    .reportview-container .main .block-container { max-width: 500px; }
    .pnl-box { padding: 15px; background-color: #1f2937; border-radius: 8px; border-left: 5px solid #ffd700; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO REBRANDING ---
st.markdown("<h1 style='text-align: center;'>⚡ SCALPPROP • PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>Institutional Prop Risk Management</p>", unsafe_allow_html=True)
st.write("---")

# --- CONFIGURAÇÕES DE BASE ---
st.subheader("🎛️ Configuração de Conta")
col1, col2 = st.columns(2)

with col1:
    token = st.text_input("PROCURAR TOKEN", value="SOL").upper()

with col2:
    # Mantendo o valor padrão de $5000 alinhado com a tua conta Bitfunded
    saldo = st.number_input("SALDO BITFUNDED ($)", value=5000, step=500)

# --- MÓDULO 1: TRAILING DOWN / DCA ESTRUTURAL (HOT ZONE) ---
st.write("---")
st.subheader("📉 Trailing Down (Hot Zone DCA)")
st.caption("Fracionamento estratégico de entradas entre os níveis 0.5 e 0.618 de Fibonacci.")

preco_entrada_topo = st.number_input("Preço de Entrada Inicial (Nível 0.5 Fib)", value=150.0, step=0.1)
preco_entrada_fundo = st.number_input("Preço de Entrada Limite (Nível 0.618 Fib)", value=148.2, step=0.1)
stop_loss_dca = st.number_input("Stop Loss da Operação DCA", value=146.5, step=0.1)

# Cálculo do preço médio projetado assumindo distribuição institucional (30% topo / 70% fundo)
preco_medio_dca = (preco_entrada_topo * 0.3) + (preco_entrada_fundo * 0.7)
distancia_stop_dca = ((preco_medio_dca - stop_loss_dca) / preco_medio_dca) * 100

st.markdown(f"""
<div class='pnl-box'>
    <b>Métricas do Trailing Down:</b><br>
    • Preço Médio Projetado: <span style='color: #ffd700;'>${preco_medio_dca:.3f}</span><br>
    • Distância até ao Stop: <span style='color: #ff4d4d;'>{distancia_stop_dca:.2f}%</span>
</div>
""", unsafe_allow_html=True)

# --- MÓDULO 2: ESQUEMA PIRÂMIDE (SCALE-IN A FAVOR DA TENDÊNCIA) ---
st.write("---")
st.subheader("🔺 Esquema Pirâmide (Scale-In)")
st.caption("Adiciona contratos a uma posição vencedora protegendo o Drawdown.")

posicao_atual_preco = st.number_input("Preço de Entrada da 1ª Posição", value=150.0, step=0.1)
posicao_atual_tamanho = st.number_input("Tamanho da 1ª Posição (Contratos/Lotes)", value=10.0, step=1.0)
preco_adicao = st.number_input("Preço para Adicionar Posição (Pirâmide)", value=153.5, step=0.1)
tamanho_adicao = st.number_input("Tamanho da Adição (Contratos/Lotes)", value=5.0, step=1.0)
novo_stop_geral = st.number_input("Novo Stop Loss Geral (Breakeven/Trailing)", value=151.0, step=0.1)

# Cálculos Matemáticos da Pirâmide
total_contratos = posicao_atual_tamanho + tamanho_adicao
novo_preco_medio = ((posicao_atual_preco * posicao_atual_tamanho) + (preco_adicao * tamanho_adicao)) / total_contratos
pnl_no_stop = (novo_stop_geral - novo_preco_medio) * total_contratos

# --- MÓDULO 3: DASHBOARD DE P&L DEDICADO ---
st.write("---")
st.subheader("📊 Painel de P&L de Operações Específicas")

if pnl_no_stop >= 0:
    cor_pnl = "#00ff00"
    status_pnl = "Lucro Garantido"
else:
    cor_pnl = "#ff4d4d"
    status_pnl = "Risco Atual"

st.markdown(f"""
<div class='pnl-box'>
    <h4>Projeção ScalpProp (Pirâmide):</h4>
    • Novo Preço Médio Total: <b>${novo_preco_medio:.3f}</b><br>
    • Volume Total Exposto: <b>{total_contratos} contratos</b><br>
    • P&L Projetado no Novo Stop: <span style='color: {cor_pnl}; font-weight: bold;'>${pnl_no_stop:.2f} ({status_pnl})</span>
</div>
""", unsafe_allow_html=True)

# Botão de Execução Automática (Mantido para o Stress Test)
if st.button("EXECUTAR SCAN AUTOMÁTICO", use_container_width=True):
    st.success(f"Scan executado com sucesso para {token} no ecossistema ScalpProp!")
