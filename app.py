import streamlit as st
import requests
import time

# 1. Configuração da Página e Título do Navegador
st.set_page_config(page_title="Sniper Calc - Premium", page_icon="🎯", layout="centered")

# 2. Design Visual Avançado (CSS) - Fundo de Velas, Cores Pretas, Douradas, Verdes e Vermelhas
st.markdown("""
    <style>
    /* Estilização do fundo global da App */
    .stApp {
        background-color: #0b0c10;
        background-image: 
            linear-gradient(rgba(36, 41, 62, 0.15) 1px, transparent 1px),
            linear-gradient(90deg, rgba(36, 41, 62, 0.15) 1px, transparent 1px),
            linear-gradient(to bottom, #00c853 0%, #00c853 100%),
            linear-gradient(to bottom, #00c853 0%, #00c853 100%),
            linear-gradient(to bottom, #ff3d00 0%, #ff3d00 100%),
            linear-gradient(to bottom, #ff3d00 0%, #ff3d00 100%);
        background-size: 40px 40px, 40px 40px, 16px 50px, 2px 110px, 20px 70px, 2px 140px;
        background-position: 0 0, 0 0, 8% 20%, 9.1% 10%, 90% 65%, 91.2% 55%;
        background-repeat: repeat, repeat, no-repeat, no-repeat, no-repeat, no-repeat;
    }
    
    /* Contentores dos blocos (Cards) */
    .block-container {
        padding-top: 2rem;
        max-width: 600px;
    }
    
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(22, 25, 37, 0.85);
        border: 1px solid rgba(212, 175, 55, 0.25);
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 12px 40px rgba(0,0,0,0.7);
        backdrop-filter: blur(8px);
    }
    
    /* Textos, Títulos e Labels */
    h1 {
        color: #d4af37 !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-size: 24px !important;
        text-align: center;
        border-bottom: 2px solid #24293e;
        padding-bottom: 12px;
        margin-bottom: 20px !important;
    }
    
    label {
        color: #a0a5b5 !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        font-size: 11px !important;
        letter-spacing: 0.5px;
    }
    
    /* Inputs de texto e números */
    input {
        background-color: rgba(11, 12, 16, 0.95) !important;
        color: white !important;
        border: 1px solid #24293e !important;
        border-radius: 8px !important;
    }
    
    /* Botão de Calcular */
    .stButton>button {
        background-color: #d4af37 !important;
        color: #0b0c10 !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        width: 100%;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px !important;
        transition: all 0.2s;
    }
    .stButton>button:hover {
        background-color: #f3e5ab !important;
        transform: translateY(-1px);
    }
    
    /* Tabelas Profissionais e Badges */
    .trade-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
        background-color: rgba(11, 12, 16, 0.6);
        border-radius: 8px;
        overflow: hidden;
    }
    .trade-table th, .trade-table td {
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid #24293e;
        font-size: 14px;
    }
    .trade-table th {
        background-color: rgba(11, 12, 16, 0.9);
        color: #d4af37;
        font-size: 11px;
        text-transform: uppercase;
    }
    .badge-long {
        background-color: rgba(0, 200, 83, 0.15);
        color: #00c853;
        padding: 4px 8px;
        border-radius: 4px;
        font-weight: bold;
    }
    .tp-row {
        background-color: rgba(0, 200, 83, 0.06);
    }
    
    /* Caixa de Gestão Ativa */
    .copilot-box {
        margin-top: 20px;
        background-color: rgba(11, 12, 16, 0.9);
        border-left: 4px solid #d4af37;
        padding: 15px;
        border-radius: 0 10px 10px 0;
        border-top: 1px solid #24293e;
        border-right: 1px solid #24293e;
        border-bottom: 1px solid #24293e;
    }
    .copilot-box h3 {
        margin: 0 0 8px 0;
        font-size: 13px;
        color: #d4af37;
        text-transform: uppercase;
    }
    .copilot-box p {
        margin: 5px 0;
        font-size: 13px;
        color: #e2e8f0;
        line-height: 1.4;
    }
    </style>
""", unsafe_allow_html=True)

def obter_preco_binance(token):
    # Lista de endpoints da Binance para contornar bloqueios de IP da Cloud
    urls = [
        f"https://api.binance.com/api/v3/ticker/price?symbol={token}USDT",
        f"https://api1.binance.com/api/v3/ticker/price?symbol={token}USDT",
        f"https://api3.binance.com/api/v3/ticker/price?symbol={token}USDT"
    ]
    
    for url in urls:
        for tentativa in range(3):  # Tenta até 3 vezes em cada URL
            try:
                res = requests.get(url, timeout=4)
                if res.status_code == 200:
                    return float(res.json()['price'])
            except:
                time.sleep(0.5)  # Pequena pausa antes de tentar novamente
    return None

# 3. Estrutura da Interface Visual
st.markdown("<h1>🎯 Sniper Calc &bull; Premium</h1>", unsafe_allow_html=True)

# Container Único para Inputs
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        token = st.text_input("Procurar Token", value="SOL").strip().upper()
    with col2:
        banca = st.number_input("Saldo Bitfunded ($)", value=5000, step=500)
        
    calcular = st.button("Executar Scan Automático")

# 4. Lógica e Renderização da Resposta Visual
if calcular and token:
    preco_mercado = obter_preco_binance(token)
    
    if preco_mercado:
        # Fórmulas do Top Setup
        percentual_sl = 0.015  # SL Automático de 1.5%
        preco_entrada = preco_mercado
        preco_sl = preco_entrada * (1 - percentual_sl)
        dist_absoluta = preco_entrada - preco_sl
        
        risco_percentual = 0.0025  # Risco 0.25% Prop Firm
        capital_em_risco = banca * risco_percentual
        
        lote_moedas = capital_em_risco / dist_absoluta
        lote_usd = lote_moedas * preco_entrada
        
        tp1 = preco_entrada + (dist_absoluta * 2)
        tp2 = preco_entrada + (dist_absoluta * 4)
        tp3 = preco_entrada + (dist_absoluta * 6)
        gatilho_piramide = preco_entrada + (dist_absoluta * 1)
        
        # Desenho da Tabela Executiva em HTML Nativo com Estilos Premium
        st.markdown(f"""
            <table class="trade-table">
                <thead>
                    <tr>
                        <th>Métrica do Setup</th>
                        <th>Preço Alvo</th>
                        <th>Ação em Conta</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Modo / Risco</strong></td>
                        <td><span class="badge-long">LONG</span></td>
                        <td>Alocação Rígida: <strong>${capital_em_risco:.2f}</strong> (0.25%)</td>
                    </tr>
                    <tr>
                        <td><strong>Preço de Entrada</strong></td>
                        <td><strong>${preco_entrada:.4f}</strong></td>
                        <td>Execução Imediata a Mercado</td>
                    </tr>
                    <tr>
                        <td><strong>Stop Loss Defendido</strong></td>
                        <td style="color: #ff3d00; font-weight: bold;">${preco_sl:.4f}</td>
                        <td>Margem Estrutural de 1.5%</td>
                    </tr>
                    <tr style="color: #00c853; font-weight: bold;">
                        <td><strong>LOTE SUGERIDO</strong></td>
                        <td style="font-size: 16px;">{lote_moedas:.4f} {token}</td>
                        <td>Notional: ~${lote_usd:.2f}</td>
                    </tr>
                    <tr class="tp-row">
                        <td><strong>Take Profit 1 (1:2 RR)</strong></td>
                        <td style="color: #00c853; font-weight: bold;">${tp1:.4f}</td>
                        <td>Garantir Parcial + Mover SL para BE</td>
                    </tr>
                    <tr>
                        <td><strong>Take Profit 2 (1:4 RR)</strong></td>
                        <td>${tp2:.4f}</td>
                        <td>Alvo Principal da Projeção</td>
                    </tr>
                    <tr>
                        <td><strong>Take Profit 3 (1:6 RR)</strong></td>
                        <td>${tp3:.4f}</td>
                        <td>Alvo de Tendência Estendida</td>
                    </tr>
                </tbody>
            </table>
            
            <div class="copilot-box">
                <h3>🛡️ Co-Piloto de Gestão Ativa</h3>
                <p><strong>⚠️ Tempo (Bob Volman):</strong> Sem reação forte a favor em até 4 velas? Faça o fecho manual imediato de <strong>{lote_moedas * 0.5:.4f} {token}</strong> (cortar metade do risco a mercado).</p>
                <p><strong>🚀 Pirâmide Micro:</strong> Caso o preço rompa com volume a barreira dos <strong>${gatilho_piramide:.4f}</strong>, adicione <strong>+{lote_moedas * 0.2:.4f} {token}</strong> (+20%) ao trade com o risco do lote inicial já defendido.</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error(f"A API da Binance rejeitou a ligação temporariamente. Por favor, clica novamente no botão de Scan.")
        
