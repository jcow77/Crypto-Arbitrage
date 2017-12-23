import ccxt
import time
#test exchanges: poloniex binance gate cryptopedia and gdax
#Loads the market for each exchange
poloniex = ccxt.poloniex({"apikey": null, 'secret': null})
gate = ccxt.gateio({"apikey": null, 'secret': null})
#save market data
#market data has the format of:
#{maker,taker,precision{amount,price},limits{amount{min,max}},price{min,max},cost{min,max}}
poloniexMarkets = poloniex.load_markets()
gateMarkets = gate.load_markets()

#prints id with market
poloniexSymbols = poloniex.symbols
gateSymbols = gate.symbols

print(poloniexSymbols)
print(gateSymbols)

def quoteMaxAmount(exchange, pair, price):
    balance = exchange.fetchBalance() #would be best to store in array
    quoteBalance = balance['free'][exchange.markets[pair]['quote']]
    amount = quoteBalance / price
    return amount

def arbitrage(exchangeA, exchangeB, pair):
    maxBought = quoteMaxAmount(exchangeA, pair, 0)
    exchangeA.createMarketBuyOrder(pair, maxBought)
    buyInfo = exchangeA.fetchOrders (symbol = pair, limit = 1) #most recent order
    if(buyInfo['status'] == 'closed'):
        exchangeA.withdraw(exchangeA.markets[pair]['quote'], none)
        if('''withdrawal is done'''):
            exchangeB.createMarketSellOrder(pair, exchangeB.markets[pair]['base'])







