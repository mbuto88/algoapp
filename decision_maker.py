class DecisionMaker:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_decision(self, prices):
        return self.strategy.decide(prices)
