import telebot
from telebot import types
import requests
from auth_data import token

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start(start_message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        curse = types.KeyboardButton("Курсы валют")
        news = types.KeyboardButton("Новости крипто мира")
        markup.add(curse, news)

        bot.send_message(start_message.chat.id ,
                         f"<b>Добрый день, {start_message.from_user.first_name}</b>", parse_mode="html")
        bot.send_message(start_message.chat.id,
                         f"Это телеграм бот, где ты можешь следить за миром криптовалют\nВыбери что конкретно тебя интересует...", reply_markup=markup)


    @bot.message_handler(content_types = ["text"])
    def curse(curs_news_message):
        if curs_news_message.text == "Курсы валют":
            try:
                bot.send_message(curs_news_message.chat.id, "Выберите какая пара валют вас интересует?")
            except Exception as ex:
                print(ex)
                bot.send_message(curs_news_message.chat.id, "Что-то пошло не так")
        else:
            bot.send_message(curs_news_message.chat.id, "Я пока вас не понимаю")


    bot.polling(none_stop=True)

if __name__ == '__main__':
    telegram_bot(token)
