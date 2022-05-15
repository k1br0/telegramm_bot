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
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                BTC = types.KeyboardButton("Bitcoin")
                ETH = types.KeyboardButton("Ethereum")
                LTC = types.KeyboardButton("Litecoin")
                SOL = types.KeyboardButton("Solana")
                USDT = types.KeyboardButton("Tether")
                LUNA = types.KeyboardButton("Luna")
                XLM = types.KeyboardButton("Stellar")
                BNB = types.KeyboardButton("Binance Coin")
                USD = types.KeyboardButton("Cardano")
                else_currency = types.KeyboardButton("Другая валюта")
                back_to_menu = types.KeyboardButton("Назад в меню")

                markup.add(BTC , ETH , LTC , SOL , LUNA , USDT , XLM , BNB , USD)
                markup.row(back_to_menu , else_currency)
                bot.send_message(curs_news_message.chat.id, "Выберите какая пара валют вас интересует?", reply_markup=markup)
        elif curs_news_message.text == "Назад в меню":
            back_to_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            curse = types.KeyboardButton("Курсы валют")
            news = types.KeyboardButton("Новости крипто мира")
            back_to_menu_markup.add(curse, news)

            bot.send_message(curs_news_message.chat.id,
                         f"<b>Добрый день, {curs_news_message.from_user.first_name}</b>", parse_mode="html")
            bot.send_message(curs_news_message.chat.id,
                         f"Это телеграм бот, где ты можешь следить за миром криптовалют\nВыбери что конкретно тебя интересует...",
                         reply_markup=back_to_menu_markup)

        if curs_news_message.text == "Bitcoin":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                responce = req.json()
                sell_prise = responce["btc_usd"]["sell"]
                bot.send_message(curs_news_message.chat.id,
                                 f"{sell_prise}")
            except Exception as ex:
                print(ex)
                bot.send_message(curs_news_message.chat.id,
                                 "Пока я вас не понимаю.")

        elif curs_news_message.text != "Курсы валют" and curs_news_message.text != "Назад в меню":
                bot.send_message(curs_news_message.chat.id, "Я пока вас не понимаю")
    bot.polling(none_stop=True)
if __name__ == '__main__':
    telegram_bot(token)
