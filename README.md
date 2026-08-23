# Simple Quant Backtester

## Overview

Simple Quant Backtester is a basic stock strategy backtesting system.

Users can provide a stock price series, initial capital, and transaction fee rate. The system generates trading signals based on the price data, simulates buy and sell operations, and tracks portfolio performance.

The backtest reports portfolio value, trading signals, equity history, trade history, total return, annualized return, annualized volatility, Sharpe ratio, and maximum drawdown.
## Input

- `prices`: A time-ordered series of stock prices.
- `initial_money`: The initial capital used for the backtest.
- `fee_rate`: The transaction fee rate applied to each trade.
## Output

- `portfolio`: The account object after the backtest completes. It contains money, shares, average cost, trade history, equity history, realized PnL, and other portfolio information.
- `signals`: Trading signals (`0` or `1`) generated from the price series.
- `strategy_returns`: Period-by-period strategy returns calculated from the portfolio equity history.
- `sharpe`: Annualized Sharpe ratio, measuring return relative to volatility.
- `max_drawdown`: Maximum peak-to-trough decline during the backtest period.
- `drawdown_start`: Index where the maximum drawdown begins.
- `drawdown_end`: Index where the maximum drawdown ends.
- `annual_return`: Annualized compound return.
- `annual_volatility`: Annualized volatility of strategy returns.
- `total_return`: Total cumulative return over the entire backtest period.
## Usage

Run `main.py` to execute the example backtest, or import `run_strategy` into another Python file.

```python
from main import run_strategy

prices = [100, 110, 120, 105]

report = run_strategy(
    prices,
    initial_money=10000,
    fee_rate=0.001
)

print(report["total_return"])
print(report["sharpe"])
print(report["max_drawdown"])
```
## Limitations

- Currently supports only a single asset.
- Trading signals are limited to `0` and `1`; short selling is not supported.
- Price data must currently be entered manually.
- Trade size is fixed at 10 shares.
- The backtester does not yet connect to real market data.
- The Sharpe ratio currently assumes a risk-free rate of 0.
## Future Improvements

- Add configurable position sizing instead of using a fixed trade size.
- Add support for short selling and long-short strategies.
- Add a configurable risk-free rate for Sharpe ratio calculation.