from controller.handler_currencies import CurrenciesHandler
from controller.handler_currency import CurrencyHandler
from controller.handler_exchange_rate import ExchangeRateHandler
from controller.handler_exchange_rates import ExchangeHandler

routers = {
    "/currencies": CurrenciesHandler,
    "/currency/": CurrencyHandler,
    "/exchangeRates": ExchangeHandler,
    "/exchangeRate/": ExchangeRateHandler,
}
