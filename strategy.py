class Strategy:
    def decide(self, prices):
        raise NotImplementedError("The decide method must be implemented.")


class MovingAverageStrategy(Strategy):
    def decide(self, prices):
        current_price = prices[-1]
        moving_average = prices.rolling(window=20).mean()[-1]

        if current_price > moving_average:
            return "Buy"
        elif current_price < moving_average:
            return "Sell"
        else:
            return "Hold"
