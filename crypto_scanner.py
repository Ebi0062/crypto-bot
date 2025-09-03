import requests
import os

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    'vs_currency': 'usd',
    'category': 'meme-token',
    'order': 'market_cap_desc',
    'per_page': 20,
    'page': 1
}

response = requests.get(url, params=params)
coins = response.json()

message = "🔍 میم‌کوین‌های امیدوارکننده:\n\n"
for coin in coins:
    if coin['price_change_percentage_24h'] < 100:
        message += f"• {coin['name']} ({coin['symbol'].upper()})\n"
        message += f"  💵 قیمت: ${coin['current_price']}\n"
        message += f"  📉 تغییر ۲۴h: {coin['price_change_percentage_24h']}%\n\n"
print("Message content:", message)
send_telegram_message(message)
if len(message) > 50:
    print("Message sent successfully!")
else:
    print("No coins found or message too short")
