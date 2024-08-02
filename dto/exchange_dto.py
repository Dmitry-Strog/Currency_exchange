class ExchangeDTO:
    def __init__(self, id, baseCurrencyCode, targetCurrencyCode, rate):
        self.id = id
        self.baseCurrencyCode = baseCurrencyCode
        self.targetCurrencyCode = targetCurrencyCode
        self.rate = rate

    def to_dict(self):
        return {
            'id': self.id,
            'baseCurrencyCode': self.baseCurrencyCode,
            'targetCurrencyCode': self.targetCurrencyCode,
            'rate': self.rate,
        }
