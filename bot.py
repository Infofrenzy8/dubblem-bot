# dubblem - Simple Binance Trading Bot (Spot Market)

import time

# === MOCK BINANCE CLIENT ===
# This is a simulated version for environments without ccxt or real API access
class MockBinance:
    def __init__(self):
        self.price = 30000  # starting BTC price

    def fetch_ticker(self, symbol):
        # simulate small price movement
        import random
        self.price += random.uniform(-50, 100)
        return {'last': self.price}

    def create_market_buy_order(self, symbol, amount):
        return {'symbol': symbol, 'side': 'buy', 'amount': amount, 'price': self.price}

    def create_market_sell_order(self, symbol, amount):
        return {'symbol': symbol, 'side': 'sell', 'amount': amount, 'price': self.price}

# === USER SETUP ===
api_key = 'YOUR_BINANCE_API_KEY'
api_secret = 'YOUR_BINANCE_SECRET_KEY'

symbol = 'BTC/USDT'  # Change to your preferred pair
trade_amount = 0.001  # Amount of BTC to buy
profit_target = 1.02  # Sell at 2% profit

# === INIT ===
binance = MockBinance()

def get_price():
    ticker = binance.fetch_ticker(symbol)
    return ticker['last']

def place_buy():
    print("[BUY] Placing market buy order...")
    order = binance.create_market_buy_order(symbol, trade_amount)
    print("[BUY] Order executed:", order)
    return get_price()

def place_sell():
    print("[SELL] Placing market sell order...")
    order = binance.create_market_sell_order(symbol, trade_amount)
    print("[SELL] Order executed:", order)

# === BOT START ===
print("[dubblem] Bot started for", symbol)
buy_price = get_price()
print(f"[INFO] Current price: {buy_price:.2f}")

buy_price = place_buy()
target_price = buy_price * profit_target
print(f"[INFO] Target sell price: {target_price:.2f}")

while True:
    current_price = get_price()
    print(f"[CHECK] Price: {current_price:.2f}")

    if current_price >= target_price:
        place_sell()
        print("[SUCCESS] Profit target reached. Trade complete.")
        break

    time.sleep(2)  # Faster simulation for testing
