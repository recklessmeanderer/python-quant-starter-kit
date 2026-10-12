"""
Standalone Position Sizer & Risk Management Engine
Calculates optimal share/contract sizing based on account balance and stop-loss distance.
MIT License - Open Source Sample from the Python Algo-Trading Starter Kit.
"""

class PositionSizer:
    def __init__(self, account_size: float, max_risk_pct: float = 0.01):
        """
        :param account_size: Total portfolio value in USD (e.g. 10000.0)
        :param max_risk_pct: Max portfolio risk per trade as a decimal (default: 0.01 = 1%)
        """
        if account_size <= 0:
            raise ValueError("Account size must be greater than zero.")
        if not (0 < max_risk_pct <= 0.10):
            raise ValueError("max_risk_pct should typically be between 0.001 (0.1%) and 0.10 (10%).")

        self.account_size = account_size
        self.max_risk_pct = max_risk_pct

    def calculate_by_stop_loss(self, entry_price: float, stop_loss_price: float) -> dict:
        """
        Calculates exact shares/units to buy so that if your stop loss is triggered,
        the dollar loss equals exactly max_risk_pct of your total account.
        """
        risk_per_unit = abs(entry_price - stop_loss_price)
        if risk_per_unit <= 0:
            raise ValueError("Entry price and stop loss price cannot be identical.")

        max_allowed_loss = self.account_size * self.max_risk_pct
        units = max_allowed_loss / risk_per_unit
        position_value = units * entry_price

        return {
            "account_size": self.account_size,
            "max_dollar_risk": round(max_allowed_loss, 2),
            "risk_per_unit": round(risk_per_unit, 2),
            "optimal_units": round(units, 4),
            "position_capital": round(position_value, 2),
            "portfolio_allocation_pct": round((position_value / self.account_size) * 100, 2)
        }
