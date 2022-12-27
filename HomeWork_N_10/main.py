import telebot
from telebot import types 
import config
import methods as md

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Курс ЦБ на сегодня: 🇺🇸 $", "Курс ЦБ на сегодня: 🇪🇺 €"]
    markup.add(*buttons)
    bot.send_message(message.chat.id, 'Нажмите на кнопку-', reply_markup = markup)

@bot.message_handler(content_types=['text'])
def chatting(message):

    mtx = message.text
    if 'ЦБ' in mtx:
        bot.delete_message(message.chat.id, message.message_id)
        mtx = md.curs(mtx)
        bot.send_message(message.chat.id, mtx, parse_mode="Markdown")

    elif mtx == "d":
            d = telebot.types.ReplyKeyboardRemove()
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, "_Кнопки удалены._", reply_markup = d, parse_mode="Markdown")   

bot.polling(none_stop=True)
