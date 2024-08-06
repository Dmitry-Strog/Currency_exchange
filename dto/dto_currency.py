class CurrencyDTO:
    def __init__(self, id, code, fullname, sign):
        self.id = id
        self.code = code
        self.fullname = fullname
        self.sign = sign

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.fullname,
            'code': self.code,
            'sign': self.sign,
        }
