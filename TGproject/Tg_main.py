import telebot
from telebot import types
import requests
from auth_data import token

def telegram_bot(token):
    bot = telebot.TeleBot(token)
    @bot.message_handler(commands=["start"])
    def start(message):
        bot.send_message(message.chat.id ,
                         f"<b>Добрый день, {message.from_user.first_name}</b>" ,
                     parse_mode="html")
        bot.send_message(message.chat.id, f"Это телеграм бот, где ты можешь следить за миром криптовылют\nВыбери что конкретно тебя интересует...",
                         parse_mode="html")

    @bot.message_handler(commands=["start"])
    def webite(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        curse = types.KeyboardButton("Курсы валют")
        news = types.KeyboardButton("Новости крипто мира")
        markup.add(curse , news)
        bot.send_message(message.chat.id , "Выберите Вариант", reply_markup=markup)


    bot.infinity_polling()
    bot.polling()


if __name__ == '__main__':
    telegram_bot(token)
