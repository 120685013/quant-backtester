class Portfolio:
    def __init__(self,money,fee_rate=0.0):
        if money<0:
            raise ValueError("money不能小于0")
        if fee_rate<0:
            raise ValueError("fee_rate不能小于0")
        self.money=money
        self.share=0
        self.average_cost=0
        self.trades=[]
        self.equity_history=[]
        self.realized_pnl=0
        self.fee_rate=fee_rate
    def value(self,price):

        stock_value=price*self.share
        equity=stock_value+self.money
        return equity
    def update_value(self,price):
        equity=self.value(price)
        self.equity_history.append(equity)
        return equity

    def buy(self,price,quantity):
        if price<=0:
            raise ValueError("price必须大于0")
        if quantity<=0:
            raise ValueError("quantity必须大于0")
        cost=price*quantity
        fee=cost*self.fee_rate
        total_cost=cost+fee
        if self.money<total_cost:
            print("余额不足")
            return False
        old_shares=self.share
        old_cost_value=self.average_cost*old_shares
        new_cost_value=total_cost
        self.average_cost=(old_cost_value+new_cost_value)/(old_shares+quantity)
        self.money-=total_cost
        self.share+=quantity
        trade={
            "type":'BUY',
            "price":price,
            "quantity":quantity,
            "fee":fee
        }
        self.trades.append(trade)
        return True
    def sell(self,price,quantity):
        if price<=0:
            raise ValueError("price必须大于0")
        if quantity<=0:
            raise ValueError("quantity必须大于0")
        if self.share<quantity:
            print('持仓不足')
            return False

        revenue=price*quantity
        fee=revenue*self.fee_rate
        net_revenue=revenue-fee

        realized_pnl=(price-self.average_cost)*quantity-fee
        self.realized_pnl+=realized_pnl
        self.money+=net_revenue
        self.share-=quantity
        if self.share==0:
            self.average_cost=0
        trade = {
            "type": 'SELL',
            "price": price,
            "quantity": quantity,
            "realized_pnl": realized_pnl,
            "fee": fee
        }
        self.trades.append(trade)
        return True


