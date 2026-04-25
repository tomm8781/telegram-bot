import telebot
import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN_10")
ADMIN_ID = int(os.environ.get("ADMIN_ID"))
bot = telebot.TeleBot(TELEGRAM_TOKEN)
user_map = {}

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id != ADMIN_ID:
        bot.reply_to(message, "Dong chi cung cap ten dang nhap de nhan ma OTP")

@bot.message_handler(func=lambda msg: msg.chat.id != ADMIN_ID)
def from_user(message):
    user = message.from_user
    name = user.first_name + (f" @{user.username}" if user.username else "")
    sent = bot.send_message(ADMIN_ID, f"[BOT 10] {name} (ID: {user.id}): {message.text}")
    user_map[sent.message_id] = user.id

@bot.message_handler(func=lambda msg: msg.chat.id == ADMIN_ID and msg.reply_to_message)
def from_admin(message):
    target_id = user_map.get(message.reply_to_message.message_id)
    if target_id:
        bot.send_message(target_id, message.text)
        bot.reply_to(message, "Da gui!")
    else:
        bot.reply_to(message, "Khong tim thay nguoi dung!")

print("Bot 10 dang chay...")
bot.polling()
