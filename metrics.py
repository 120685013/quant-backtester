import numpy as np
def calc_sharpe(returns):
    if len(returns)==0:
        return 0
    mean=np.mean(returns)
    std=np.std(returns)
    if std==0:
        return 0
    sharpe=mean/std*np.sqrt(252)
    return sharpe
def max_drawdown(values):
    if len(values) == 0:
        return 0, 0, 0
    peak=values[0]
    peak_index=0
    max_drawdown=0
    start=0
    end=0
    for i,value in enumerate(values):

        if value>peak:
            peak=value
            peak_index=i
        if peak==0:
            drawdown=0
        else:
          drawdown=(peak-value)/peak
        if drawdown>max_drawdown:
            max_drawdown=drawdown
            start=peak_index
            end=i
    return max_drawdown,start,end
def calc_annual_return(history):
    if len(history) <= 1:
        return 0
    if history[0]==0:
        return 0
    annual_return=(history[-1]/history[0])**(252/(len(history)-1))-1
    return annual_return
def calc_total_return(history):
    if len(history) <= 1:
        return 0
    if history[0] == 0:
        return 0
    total_return=(history[-1]-history[0])/history[0]
    return total_return
def calc_annual_volatility(strategy_returns):
    if len(strategy_returns)==0:
        return 0
    std=np.std(strategy_returns)
    return std*np.sqrt(252)
def calc_excess_returns(strategy_returns,benchmark_returns):
    if len(strategy_returns)!=len(benchmark_returns):
        raise ValueError("strategy_returns和benchmark_returns长度必须一致")
    excess_returns=[]
    for strategy_return,benchmark_return in zip(strategy_returns,benchmark_returns):
      excess_return=strategy_return-benchmark_return
      excess_returns.append(excess_return)
    return excess_returns
def calc_information_ratio(excess_returns,periods_per_year=252,min_sample=20):
    if not isinstance(periods_per_year, (int, float)):
        raise TypeError("periods_per_year must be int or float")
    if periods_per_year <= 0:
        raise ValueError("periods_per_year must be greater than 0")
    if not isinstance(min_sample, (int)):
        raise TypeError("min_sample must be int")
    if min_sample <= 0:
        raise ValueError("min_sample must be greater than 0")
    if min_sample > len(excess_returns):
        return None
    mean=np.mean(excess_returns)
    std=np.std(excess_returns)
    if np.isclose(std, 0):
        if mean>0:
            return float('inf')
        elif mean<0:
            return float('-inf')
        else:
            return 0
    information_ratio=mean/std*np.sqrt(periods_per_year)
    return information_ratio

