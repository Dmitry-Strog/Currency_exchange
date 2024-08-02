class ExchangeDTO:
    def __init__(self, id, baseCurrency, targetCurrency, rate):
        self.id = id
        self.baseCurrency = baseCurrency
        self.targetCurrency = targetCurrency
        self.rate = rate

    def to_dict(self):
        return {
            'id': self.id,
            'baseCurrency': self.baseCurrency,
            'targetCurrency': self.targetCurrency,
            'rate': self.rate,
        }
