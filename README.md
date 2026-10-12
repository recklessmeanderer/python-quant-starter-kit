# Python Algo-Trading & Market Intelligence Toolkit 🚀

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Gumroad](https://img.shields.io/badge/Gumroad-Full_Kit_Available-orange.svg)](https://gumroad.com)

A lightweight, institutional-grade starter toolkit for retail algorithmic traders and quantitative researchers.

This open-source repository provides our core **Risk-First Position Sizing Engine** and a **10-Asset Teaser Sample** of our AI, DePIN & Strategic Metals Market Intelligence Sheet.

---

## ⚡ Why Position Sizing Matters First

The #1 reason algorithmic traders blow up accounts isn't bad entry signals—it is **arbitrary position sizing**. 

If you risk 10% on a trade, a streak of 4 consecutive losses draws down ~35% of your capital. If you mathematically cap risk at **1% per trade**, even a 10-trade losing streak leaves over 90% of your capital intact.

### Quick Example:
```python
from position_sizer import PositionSizer

# Initialize with $25,000 account and 1% risk per trade ($250 max loss)
sizer = PositionSizer(account_size=25000.0, max_risk_pct=0.01)

# Buying NVDA at $150 with a tight stop at $142.50 ($7.50 risk/share)
trade = sizer.calculate_by_stop_loss(entry_price=150.0, stop_loss_price=142.50)

print(f"Optimal Units:   {trade['optimal_units']} shares")
print(f"Position Value:  ${trade['position_capital']}")
# Result: Buys exactly 33.33 shares ($5,000 capital).
# If stopped out at $142.50, loss is exactly $250.00 (1%).
```

Run the sample demo:
```bash
python3 demo.py
```

---

## 📦 What's in this Open-Source Repo?

* [`position_sizer.py`](position_sizer.py): Full standalone position sizer (fixed dollar risk, % account risk, and ATR stop-loss calculator).
* [`sample_market_tracker.csv`](sample_market_tracker.csv): A 10-asset preview of the AI, DePIN, and Critical Metals tracker with live `=GOOGLEFINANCE` formulas.
* [`demo.py`](demo.py): Plug-and-play demo runner.

---

## 🌟 Looking for the Full Production Suites?

We offer two complete production packages on Gumroad:

### 1. [Python Algo-Trading Starter Kit (Full Suite)](PASTE_YOUR_GUMROAD_TOOLKIT_URL_HERE)
A modular, production-ready codebase so you never have to write trading bot boilerplate from scratch:
* **Vectorized Backtesting Engine**: Instant calculation of CAGR, Annualized Sharpe Ratio, Max Drawdown %, and Daily Win Rate % with zero lookahead bias.
* **Pluggable Strategy Engine**: Pre-built Dual EMA + RSI Momentum Strategy and Bollinger Bands Mean Reversion Strategy.
* **Webhook Dispatchers**: Pre-wired Discord embeds and Telegram bot alerts using Python's standard library.
* **Full Source Code & Documentation**: 100% clean, documented Python.

👉 **[Get the Full Algo-Trading Kit on Gumroad](PASTE_YOUR_GUMROAD_TOOLKIT_URL_HERE)**

---

### 2. [AI, DePIN & Strategic Metals Intelligence Tracker (63 Assets)](PASTE_YOUR_GUMROAD_SHEET_URL_HERE)
An institutional-grade research database covering 63 highly liquid assets across the physical and digital constraints of AI:
* **Sectors Covered**: AI Silicon, Data Center Cooling (Vertiv, Carrier, Eaton), DePIN compute (TAO, NEAR, Render), Tokenized Real-World Assets (LINK, ONDO, Gold), and Critical Supply Chain Metals (Copper, Uranium, Lithium).
* **Live Formulas**: Pre-configured `=GOOGLEFINANCE` formulas for live pricing, market cap, and 52-week ranges with zero API keys required.
* **Format**: Instant 1-click import into Google Sheets, Notion, or Excel.

👉 **[Get the Complete 63-Asset Intelligence Sheet on Gumroad](PASTE_YOUR_GUMROAD_SHEET_URL_HERE)**

---

## License

This open-source sample is licensed under the [MIT License](LICENSE).
Feel free to star ⭐ this repository if it helps your quantitative workflows!
