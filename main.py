import os
import telebot
from telebot import types



bot = telebot.TeleBot('5807437640:AAEO4V6Nva895NVkw7xdIejK2WV9BucSUJw')
@bot.message_handler(content_types=['text'])
def start_main(message):
    if message.text == '/start':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_bj = types.KeyboardButton('Черный Джек')
        item_roulette = types.KeyboardButton('Рулетка')
        item_rus_roulette = types.KeyboardButton('Русская рулеточка')
        markup.add(item_bj, item_roulette, item_rus_roulette)
        bot.send_message(message.from_user.id, 'Время играть по крупному в', reply_markup=markup)
    elif message.text == 'Рулетка':
        exec(open("roulette.py").read())
    elif message.text == 'Черный Джек':
        exec(open("blackjack_bot.py").read())
    elif message.text == 'Русская рулеточка':
        exec(open("rus_roulette_bot.py").read())

bot.polling(none_stop=True, interval=0)
