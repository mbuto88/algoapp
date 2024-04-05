class Strategy:
    def decide(self, prices):
        raise NotImplementedError("The decide method must be implemented.")


class MovingAverageStrategy(Strategy):
    def decide(self, prices):
        current_price = prices.iloc[-1]
        moving_average = prices.rolling(window=20).mean().iloc[-1]

        if current_price > moving_average:
            return "Buy"
        elif current_price < moving_average:
            return "Sell"
        else:
            return "Hold"
