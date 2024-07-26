class CurrencyDTO:
    def __init__(self, id, code, fullname, sign):
        self.id = id
        self.code = code
        self.fullname = fullname
        self.sign = sign

    def to_dict(self):
        return {
            'id': self.id,
            'code': self.code,
            'fullname': self.fullname,
            'sign': self.sign,
        }
