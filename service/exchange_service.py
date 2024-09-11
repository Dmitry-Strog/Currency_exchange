from decimal import Decimal

from dao.exchange_dao import ExchangeRatesDAO
from dto.service_dto import ServiceDTO


class ExchangeService:
    def __init__(self, data):
        self.data: dict = data
        self.dao = ExchangeRatesDAO()

    def select_exchange_rate(self):
        response = self.get_direct_rate()
        if isinstance(response, ServiceDTO):
            return response
        response = self.get_reverse_rate()
        if isinstance(response, ServiceDTO):
            return response
        response = self.calculate_cross_rate()
        if isinstance(response, ServiceDTO):
            return response

    def get_direct_rate(self):
        base_currency, target_currency, amount = self.data.values()
        exchange_rate = self.dao.get_exchange((base_currency, target_currency))
        if exchange_rate:
            rate_ab = exchange_rate.rate
            currency_conversion = Decimal(rate_ab) * Decimal(amount)
            return ServiceDTO(exchange_rate.baseCurrency, exchange_rate.targetCurrency,
                              rate_ab, float(amount), float(currency_conversion))

    def get_reverse_rate(self):
        base_currency, target_currency, amount = self.data.values()
        exchange_rate = self.dao.get_exchange((target_currency, base_currency))
        if exchange_rate:
            rate_ba = exchange_rate.rate
            rate_ab = 1 / rate_ba
            currency_conversion = Decimal(rate_ab) * Decimal(amount)
            return ServiceDTO(exchange_rate.baseCurrency, exchange_rate.targetCurrency,
                              rate_ab, float(amount), float(currency_conversion))

    def calculate_cross_rate(self):
        base_currency, target_currency, amount = self.data.values()
        exchange_usd_a = self.dao.get_exchange(("USD", base_currency))
        exchange_usd_b = self.dao.get_exchange(("USD", target_currency))
        if exchange_usd_a and exchange_usd_b:
            cross_rate = Decimal(exchange_usd_b.rate / exchange_usd_a.rate)
            currency_conversion = cross_rate * Decimal(amount)
            return ServiceDTO(base_currency, target_currency,
                              float(cross_rate), float(amount), float(currency_conversion))
