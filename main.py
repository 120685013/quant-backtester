from indicators import calc_returns
from strategy import strategy
from backtest import run_backtest
from metrics import calc_sharpe,max_drawdown,calc_annual_return,calc_annual_volatility,calc_total_return,calc_excess_returns

def run_strategy(prices,initial_money=10000,fee_rate=0.0,benchmark_prices=None):
    signals=strategy(prices)
    result=run_backtest(prices,signals,initial_money=initial_money,fee_rate=fee_rate)
    strategy_returns=calc_returns(result.equity_history)
    total_return = calc_total_return(result.equity_history)
    benchmark_returns=None
    excess_returns=None
    benchmark_total_return = None
    excess_total_return = None
    if benchmark_prices is not None:
        benchmark_returns=calc_returns(benchmark_prices)
        excess_returns=calc_excess_returns(strategy_returns,benchmark_returns)
        benchmark_total_return=calc_total_return(benchmark_prices)
        excess_total_return=total_return-benchmark_total_return
    sharpe=calc_sharpe(strategy_returns)
    drawdown,start,end=max_drawdown(result.equity_history)
    annual_return=calc_annual_return(result.equity_history)
    annual_volatility=calc_annual_volatility(strategy_returns)


    report = {
        "portfolio": result,
        "signals": signals,
        "strategy_returns": strategy_returns,
        "benchmark_returns": benchmark_returns,
        "excess_returns": excess_returns,
        "benchmark_total_return": benchmark_total_return,
        "excess_total_return": excess_total_return,
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
    benchmark_prices=[100,105,110,108]
    fee_rate=0.001
    report=run_strategy(prices,fee_rate=fee_rate,benchmark_prices=benchmark_prices)
    print('money',report["portfolio"].money)
    print('signals',report["signals"])
    print('strategy returns',report["strategy_returns"])
    print('benchmark returns', report["benchmark_returns"])
    print('excess returns', report["excess_returns"])
    print('benchmark total returns', report["benchmark_total_return"])
    print('excess total returns', report["excess_total_return"])
    print('history',report["portfolio"].equity_history)
    print('trades',report["portfolio"].trades)
    print('total return', report["total_return"])
    print('annual return',report["annual_return"])
    print('annual volatility',report["annual_volatility"])
    print('sharpe', report["sharpe"])
    print('max drawdown', report["max_drawdown"])
    print('drawdown start', report["drawdown_start"])
    print('drawdown end', report["drawdown_end"])


