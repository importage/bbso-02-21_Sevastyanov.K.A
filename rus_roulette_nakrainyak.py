#Крайне коряво, но работает
import random
import telebot
from telebot import types
from telegram.ext import Updater

bot = telebot.TeleBot('5807437640:AAEO4V6Nva895NVkw7xdIejK2WV9BucSUJw')
lvl = 1
barrel = [1, 2, 3, 4, 5, 6]
loaded_barrel = []

@bot.message_handler(commands=['rusroulette'])
def rus_roulette_start(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('1')
    item2 = types.KeyboardButton('2')
    item3 = types.KeyboardButton('3')
    item4 = types.KeyboardButton('4')
    item5 = types.KeyboardButton('5')
    item6 = types.KeyboardButton('6')
    markup1.add(item1, item2, item3, item3, item4, item5, item6)
    bot.send_message(message.chat.id, text='Welcome to the Russian roulette\n'
                 'Choose ur difficulty level(1-6)\n'
                  'Выберите уровень сложности(1-6): ', reply_markup=markup1)
    if message.chat.type == 'private':
        if message.text == '1':
            k = 1
        elif message.text == '2':
            k = 2
        elif message.text == '3':
            k = 3
        elif message.text == '4':
            k = 4
        elif message.text == '5':
            k = 5
        elif message.text == '6':
            k = 6

        for i in range(int(message.text)):
            temp = random.choice(barrel)
            loaded_barrel.append(temp)
            barrel.remove(temp)


@bot.message_handler(content_types=['text'])
def review(message):
    #keyboard2
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Speen da WHEEL!')
    item2 = types.KeyboardButton('No one left')
    markup2.add(item1, item2)


    bot.send_message(message.chat.id, text='Крути барабан\nSpeen da WHEEL!', reply_markup=markup2)
    if message.chat.type == 'private':
        if message.text == 'Speen da WHEEL!':
            destiny = random.randint(1, 6)
            if destiny in barrel:
                bot.send_message(message.chat.id, text='ALIVE!\n'
                                                   'КАК ЗАНОВО РОДИЛСЯ')
            else:
                bot.send_message(message.chat.id, text='WASTED\n'
                                                   'Кто ж знал...')
        else:
            rus_roulette_start()


bot.polling(non_stop=True)


