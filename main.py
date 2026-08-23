from indicators import calc_returns
from strategy import strategy
from backtest import run_backtest
from metrics import calc_sharpe,max_drawdown,calc_annual_return,calc_annual_volatility,calc_total_return

def run_strategy(prices,initial_money=10000,fee_rate=0.0):
    signals=strategy(prices)
    result=run_backtest(prices,signals,initial_money=initial_money,fee_rate=fee_rate)
    strategy_returns=calc_returns(result.equity_history)
    sharpe=calc_sharpe(strategy_returns)
    drawdown,start,end=max_drawdown(result.equity_history)
    annual_return=calc_annual_return(result.equity_history)
    annual_volatility=calc_annual_volatility(strategy_returns)
    total_return=calc_total_return(result.equity_history)
    report = {
        "portfolio": result,
        "signals": signals,
        "strategy_returns": strategy_returns,
        "sharpe": sharpe,
        "max_drawdown": drawdown,
        "drawdown_start": start,
        "drawdown_end": end,
        "annual_return": annual_return,
        "annual_volatility": annual_volatility,
        "total_return": total_return,
    }
    return report
if __name__ == "__main__":
    prices=[100,110,120,105]
    fee_rate=0.001
    report=run_strategy(prices,fee_rate=fee_rate)
    print('money',report["portfolio"].money)
    print('signals',report["signals"])
    print('strategy returns',report["strategy_returns"])
    print('history',report["portfolio"].equity_history)
    print('trades',report["portfolio"].trades)
    print('total return', report["total_return"])
    print('annual return',report["annual_return"])
    print('annual volatility',report["annual_volatility"])
    print('sharpe', report["sharpe"])
    print('max drawdown', report["max_drawdown"])
    print('drawdown start', report["drawdown_start"])
    print('drawdown end', report["drawdown_end"])


