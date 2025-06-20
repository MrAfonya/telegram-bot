import telebot

OWNER_ID = 784479521

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.from_user.id != OWNER_ID:
        bot.reply_to(message, "Извините, доступ только для владельца.")
        return
    bot.reply_to(message, f"Ты написал: {message.text}")

API_TOKEN = '8091220315:AAHDf1LMI5UeuDzdLyAANjAsirmrOlu8UIg'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram-бот.")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

bot.infinity_polling()
