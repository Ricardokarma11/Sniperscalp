<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sniper Calc - Mobile Premium</title>
    <style>
        :root {
            --bg-color: #0b0c10;
            --card-bg: rgba(22, 25, 37, 0.9);
            --gold-color: #d4af37;
            --gold-hover: #f3e5ab;
            --green-market: #00c853;
            --red-market: #ff3d00;
            --text-color: #ffffff;
            --text-muted: #a0a5b5;
            --border-color: #24293e;
        }

        body {
            font-family: '-apple-system', BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            background-image: 
                linear-gradient(rgba(36, 41, 62, 0.15) 1px, transparent 1px),
                linear-gradient(90deg, rgba(36, 41, 62, 0.15) 1px, transparent 1px),
                linear-gradient(to bottom, var(--green-market) 0%, var(--green-market) 100%),
                linear-gradient(to bottom, var(--green-market) 0%, var(--green-market) 100%),
                linear-gradient(to bottom, var(--red-market) 0%, var(--red-market) 100%),
                linear-gradient(to bottom, var(--red-market) 0%, var(--red-market) 100%);
            background-size: 30px 30px, 30px 30px, 14px 50px, 2px 100px, 18px 70px, 2px 130px;
            background-position: 0 0, 0 0, 8% 25%, 9.1% 15%, 88% 70%, 89.2% 65%;
            background-repeat: repeat, repeat, no-repeat, no-repeat, no-repeat, no-repeat;
            color: var(--text-color);
            margin: 0;
            padding: 15px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 95vh;
        }

        .app-container {
            width: 100%;
            max-width: 480px;
            background-color: var(--card-bg);
            border: 1px solid rgba(212, 175, 55, 0.25);
            border-radius: 14px;
            padding: 20px;
            box-shadow: 0 10px 35px rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(6px);
        }

        h2 {
            margin-top: 0;
            color: var(--gold-color);
            font-size: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        h2 span {
            font-size: 10px;
            color: var(--text-muted);
            background: rgba(212, 175, 55, 0.1);
            padding: 3px 6px;
            border-radius: 4px;
        }

        .search-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 15px;
        }

        .full-width {
            grid-column: span 2;
        }

        .input-group {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }

        label {
            font-size: 10px;
            color: var(--text-muted);
            font-weight: 700;
            text-transform: uppercase;
        }

        input, select {
            background-color: rgba(11, 12, 16, 0.95);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 10px;
            color: var(--text-color);
            font-size: 14px;
            outline: none;
            -webkit-appearance: none;
        }

        input:focus, select:focus {
            border-color: var(--gold-color);
        }

        .btn-calc {
            background-color: var(--gold-color);
            color: #0b0c10;
            border: none;
            border-radius: 6px;
            padding: 12px;
            font-weight: 700;
            font-size: 14px;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-top: 5px;
        }

        .results-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
            display: none;
            background-color: rgba(11, 12, 16, 0.6);
            border-radius: 6px;
            overflow: hidden;
        }

        .results-table th, .results-table td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
            font-size: 13px;
        }

        .results-table th {
            background-color: rgba(11, 12, 16, 0.9);
            color: var(--gold-color);
            font-size: 10px;
            text-transform: uppercase;
        }

        .badge-long { color: var(--green-market); font-weight: bold; }
        .badge-short { color: var(--red-market); font-weight: bold; }

        .co-pilot-box {
            margin-top: 15px;
            background-color: rgba(11, 12, 16, 0.9);
            border-left: 4px solid var(--gold-color);
            padding: 12px;
            border-radius: 0 8px 8px 0;
            display: none;
            border: 1px solid var(--border-color);
            border-left: 4px solid var(--gold-color);
        }

        .co-pilot-box h3 {
            margin: 0 0 6px 0;
            font-size: 12px;
            color: var(--gold-color);
            text-transform: uppercase;
        }

        .co-pilot-box p {
            margin: 5px 0;
            font-size: 12px;
            color: #e2e8f0;
            line-height: 1.4;
        }
    </style>
</head>
<body>

<div class="app-container">
    <h2>SNIPER CALC <span>MOBILE V1</span></h2>
    
    <div class="search-section">
        <div class="input-group">
            <label>Token</label>
            <input type="text" id="token" value="SOL">
        </div>
        <div class="input-group">
            <label>Operação</label>
            <select id="tipo_trade">
                <option value="SCALP">Scalp</option>
                <option value="LIMIT">Limit</option>
            </select>
        </div>
        <div class="input-group full-width">
            <label>Saldo Bitfunded ($)</label>
            <input type="number" id="banca" value="5000">
        </div>
        <div class="input-group">
            <label>Preço Entrada ($)</label>
            <input type="number" id="entrada" step="any" value="140.00">
        </div>
        <div class="input-group">
            <label>Preço Stop Loss ($)</label>
            <input type="number" id="sl" step="any" value="138.50">
        </div>
        <button class="btn-calc full-width" onclick="calcularSetup()">Calcular Matriz</button>
    </div>

    <table class="results-table" id="tabela_resultados">
        <thead>
            <tr>
                <th>Parâmetro</th>
                <th>Preço</th>
                <th>Ação / Lote</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Modo</strong></td>
                <td id="res_direcao">-</td>
                <td id="res_risco_usd">-</td>
            </tr>
            <tr>
                <td><strong>Lote</strong></td>
                <td style="color: var(--green-market); font-weight: bold;" id="res_lote_moedas">-</td>
                <td id="res_lote_usd">-</td>
            </tr>
            <tr style="background-color: rgba(0, 200, 83, 0.08);">
                <td><strong>TP1 (1:2)</strong></td>
                <td id="res_tp1" style="font-weight: 700; color: var(--green-market);">-</td>
                <td>Parcial + BE</td>
            </tr>
            <tr>
                <td><strong>TP2 (1:4)</strong></td>
                <td id="res_tp2">-</td>
                <td>Alvo Principal</td>
            </tr>
            <tr>
                <td><strong>TP3 (1:6)</strong></td>
                <td id="res_tp3">-</td>
                <td>Tendência</td>
            </tr>
        </tbody>
    </table>

    <div class="co-pilot-box" id="caixa_copiloto">
        <h3>🛡️ Gestão Ativa (Top Setup)</h3>
        <p id="txt_volman"></p>
        <p id="txt_piramide"></p>
    </div>
</div>

<script>
function calcularSetup() {
    const token = document.getElementById('token').value.toUpperCase();
    const banca = parseFloat(document.getElementById('banca').value);
    const entrada = parseFloat(document.getElementById('entrada').value);
    const sl = parseFloat(document.getElementById('sl').value);

    if (!token || isNaN(banca) || isNaN(entrada) || isNaN(sl) || entrada === sl) {
        alert("Campos inválidos.");
        return;
    }

    const riscoPercentual = 0.0025;
    const capitalEmRisco = banca * riscoPercentual;
    const distAbsoluta = Math.abs(entrada - sl);
    const direcao = entrada > sl ? "LONG" : "SHORT";
    const loteMoedas = capitalEmRisco / distAbsoluta;
    const loteUsd = loteMoedas * entrada;

    let tp1, tp2, tp3, gatilhoPiramide;
    if (direcao === "LONG") {
        tp1 = entrada + (distAbsoluta * 2);
        tp2 = entrada + (distAbsoluta * 4);
        tp3 = entrada + (distAbsoluta * 6);
        gatilhoPiramide = entrada + (distAbsoluta * 1);
    } else {
        tp1 = entrada - (distAbsoluta * 2);
        tp2 = entrada - (distAbsoluta * 4);
        tp3 = entrada - (distAbsoluta * 6);
        gatilhoPiramide = entrada - (distAbsoluta * 1);
    }

    document.getElementById('res_direcao').innerHTML = `<span class="badge-${direcao.toLowerCase()}">${direcao}</span>`;
    document.getElementById('res_risco_usd').innerText = `Risco: $${capitalEmRisco.toFixed(2)}`;
    document.getElementById('res_lote_moedas').innerText = `${loteMoedas.toFixed(4)} ${token}`;
    document.getElementById('res_lote_usd').innerText = `~$${loteUsd.toFixed(2)}`;
    document.getElementById('res_tp1').innerText = `$${tp1.toFixed(4)}`;
    document.getElementById('res_tp2').innerText = `$${tp2.toFixed(4)}`;
    document.getElementById('res_tp3').innerText = `$${tp3.toFixed(4)}`;

    document.getElementById('txt_volman').innerHTML = `<strong>⚠️ Tempo (Volman):</strong> Sem explosão em 4 velas? Corte 50% (<strong>${(loteMoedas * 0.5).toFixed(4)} ${token}</strong>).`;
    document.getElementById('txt_piramide').innerHTML = `<strong>🚀 Pirâmide:</strong> Rompimento em <strong>$${gatilhoPiramide.toFixed(4)}</strong>? Adicione +20% (<strong>+${(loteMoedas * 0.2).toFixed(4)} ${token}</strong>).`;

    document.getElementById('tabela_resultados').style.display = 'table';
    document.getElementById('caixa_copiloto').style.display = 'block';
}
</script>
</body>
</html>
