from controller.handler_currencies import CurrenciesHandler
from controller.handler_currency import CurrencyHandler
from controller.handler_exchange import ExchangeHandler

routers = {
    "/currencies": CurrenciesHandler,
    "/currency/": CurrencyHandler,
    "/exchangeRates": ExchangeHandler,
}
