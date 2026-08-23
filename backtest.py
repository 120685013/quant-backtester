from quant_project.portfolio import Portfolio
def run_backtest(prices,signals,initial_money=10000,fee_rate=0.0):
    if initial_money<0:
        raise ValueError('initial_money不能小于0')
    portfolio = Portfolio(initial_money,fee_rate)
    if len(prices) == 0:
        if len(signals)!=0:
             raise ValueError("prices为空时signals也必须为空")
        return portfolio
    for price in prices:
      if price <= 0:
          raise ValueError('price必须大于0')

    if len(signals)!=len(prices)-1:
        raise ValueError('signals数量必须比prices少1')
    for signal in signals:
      if signal not in [0,1]:
        raise ValueError('signals只能是0或1')
    portfolio.update_value(prices[0])
    for price,signal in zip(prices[1:],signals):
       if signal==1 and portfolio.share==0:
          portfolio.buy(price,10)
       elif signal==0 and portfolio.share>0:
            portfolio.sell(price,portfolio.share)
       portfolio.update_value(price)
    return portfolio
