def strategy(prices):
    signals=[]
    for i in range (1,len(prices)):
        if prices[i]>prices[i-1]:
            signal=1
        else:
            signal=0
        signals.append(signal)
    return signals