import telebot
from telebot import types

TOKEN = "8093780889:AAG4HjH7jbu8Dgkc3qphGuI7F6Wls3tVKuI"
ADMIN_ID = 8098027492  # O'Z TELEGRAM IDINGNI QOY

bot = telebot.TeleBot(TOKEN)

premium_users = []

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id in premium_users:
        bot.send_message(message.chat.id, "👑 Siz premium usersiz!")
    else:
        bot.send_message(message.chat.id, "Salom! Premium olish uchun /premium yozing 💎")

@bot.message_handler(commands=['premium'])
def premium(message):
    bot.send_message(message.chat.id, "To‘lov qiling va admin sizga premium beradi 💰")

@bot.message_handler(commands=['give'])
def give_premium(message):
    if message.from_user.id == ADMIN_ID:
        try:
            user_id = int(message.text.split()[1])
            premium_users.append(user_id)
            bot.send_message(message.chat.id, "✅ Premium berildi!")
            bot.send_message(user_id, "🎉 Sizga premium berildi!")
        except:
            bot.send_message(message.chat.id, "Foydalanish: /give user_id")
    else:
        bot.send_message(message.chat.id, "⛔ Siz admin emassiz!")

bot.infinity_polling()
