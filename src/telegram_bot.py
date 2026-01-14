from telegram import Bot
import requests

BOT_TOKEN = "AAFZgqT9Q4be49qUq1KEb2Os3wlnQmtTtfE"
CHAT_ID = "8180391768"

bot = Bot(token=BOT_TOKEN)

def send_signal(symbol):
    r = requests.get(f"http://localhost:5000/signal/{symbol}")
    data = r.json()

    message = f"""
📊 Stock Signal
Symbol: {data['symbol']}
Action: {data['signal']}
"""
    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    send_signal("TCS")
