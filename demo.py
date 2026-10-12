"""
Quickstart Demo for Position Sizer
Run with: python3 demo.py
"""
from position_sizer import PositionSizer

def main():
    print("--- Risk-First Position Sizing Demo ---")
    
    # 1. Initialize with $25,000 account and 1% risk per trade ($250 max loss)
    sizer = PositionSizer(account_size=25000.0, max_risk_pct=0.01)

    # 2. Example Trade: Buying NVDA at $150 with a tight stop at $142.50 ($7.50 risk)
    entry = 150.0
    stop = 142.50
    trade = sizer.calculate_by_stop_loss(entry_price=entry, stop_loss_price=stop)

    print(f"Account Balance:       ${trade['account_size']:,.2f}")
    print(f"Max Allowed Risk (1%): ${trade['max_dollar_risk']:,.2f}")
    print(f"Risk per Share:        ${trade['risk_per_unit']}")
    print(f"Optimal Share Size:    {trade['optimal_units']} shares")
    print(f"Total Capital Deployed:${trade['position_capital']:,.2f} ({trade['portfolio_allocation_pct']}% of portfolio)")
    print("\nIf stop-loss hits at $142.50, you lose exactly $250.00 — zero guesswork.")

if __name__ == "__main__":
    main()
