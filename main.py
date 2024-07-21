import os
import telebot
from telebot import types
import time
from threading import Thread
import sqlite3


bot = telebot.TeleBot('code_to_bot')
conn = sqlite3.connect('db/test_db.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO test_db (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
    conn.commit()
@bot.message_handler(content_types=['text'])
def start_main(message):
    if message.text == '/start':
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_bj = types.KeyboardButton('Черный Джек')
        item_roulette = types.KeyboardButton('Рулетка')
        item_rus_roulette = types.KeyboardButton('Русская рулеточка')
        markup.add(item_bj, item_roulette, item_rus_roulette)
        bot.send_message(message.from_user.id, 'Время играть по крупному в', reply_markup=markup)
    elif message.text == 'Рулетка':
        exec(open("./roulette.py").read())

    elif message.text == 'Черный Джек':
        exec(open("./blackjack_bot.py").read())

    elif message.text == 'Русская рулеточка':
        exec(open("./rus_roulette_bot.py").read())


# bot.polling(none_stop=True, interval=0)
if __name__ == '__main__':
    bot.polling(none_stop=True)
