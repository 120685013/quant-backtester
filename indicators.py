def calc_returns(prices):
    returns=[]
    for i in range(1,len(prices)):
        daily_return = (prices[i] - prices[i-1])/prices[i-1]
        returns.append(daily_return)
    return returns