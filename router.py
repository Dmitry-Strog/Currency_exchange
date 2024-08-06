from controller.handler_currencies import CurrenciesHandler
from controller.handler_currency import CurrencyHandler
from controller.handler_exchange import ExchangeHandler
from controller.handler_exchange_rate import ExchangeRateHandler
from controller.handler_exchange_rates import ExchangeRatesHandler

routers = {
    "/currencies": CurrenciesHandler,
    "/currency/": CurrencyHandler,
    "/exchangeRates": ExchangeRatesHandler,
    "/exchangeRate/": ExchangeRateHandler,
    "/exchange": ExchangeHandler,
}
