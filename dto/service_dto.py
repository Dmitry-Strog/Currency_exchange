class ServiceDTO:
    def __init__(self, baseCurrency, targetCurrency, rate, amount, convertedAmount):
        self.baseCurrency = baseCurrency
        self.targetCurrency = targetCurrency
        self.rate = rate
        self.amount = amount
        self.convertedAmount = convertedAmount

    def to_dict(self):
        return {
            'baseCurrency': self.baseCurrency,
            'targetCurrency': self.targetCurrency,
            'rate': self.rate,
            'amount': self.amount,
            'convertedAmount': self.convertedAmount,
        }