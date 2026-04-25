import telebot

TELEGRAM_TOKEN = "8592302394:AAFSDehMMinAVIeM5GzzYbk_rCkhceLqmAg"
ADMIN_ID = 5074315475

bot = telebot.TeleBot(TELEGRAM_TOKEN)

user_map = {}

@bot.message_handler(func=lambda msg: msg.chat.id != ADMIN_ID)
def from_user(message):
    user = message.from_user
    name = user.first_name + (f" @{user.username}" if user.username else "")

    sent = bot.send_message(
        ADMIN_ID,
        f"👤 *{name}*\n🆔 `{user.id}`\n💬 {message.text}",
        parse_mode="Markdown"
    )

    user_map[sent.message_id] = user.id

@bot.message_handler(func=lambda msg: msg.chat.id == ADMIN_ID and msg.reply_to_message)
def from_admin(message):
    original_id = message.reply_to_message.message_id
    target_id = user_map.get(original_id)

    if target_id:
        bot.send_message(target_id, f"💬 {message.text}")
        bot.reply_to(message, "✅ Đã gửi!")
    else:
        bot.reply_to(message, "⚠️ Không tìm thấy người dùng!")

print("Bot đang chạy...")
bot.polling()