import requests
import os

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def send_telegram_message(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {"chat_id": CHAT_ID, "text": message}
        response = requests.post(url, data=data)
        print("Telegram response:", response.status_code)
        return response
    except Exception as e:
        print("Telegram error:", str(e))
        return None

# تست مستقیم
test_message = "✅ تست ربات کار می‌کند!"
print("Sending test message:", test_message)
send_telegram_message(test_message)

print("Script completed!")
