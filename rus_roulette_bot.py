import random
import telebot
from telebot import types


bot = telebot.TeleBot('5807437640:AAEO4V6Nva895NVkw7xdIejK2WV9BucSUJw')
lvl = 1
barrel = [1, 2, 3, 4, 5, 6]
loaded_barrel = []


@bot.message_handler(content_types=['text'])
def start(message):
    global barrel
    global loaded_barrel
    global lvl


    if message.text == '/start':
        set_default_values()
        markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_start = types.KeyboardButton('Начать игру!')
        markup_start.add(item_start)
        bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=markup_start)

    elif message.text == 'Начать игру!':
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('1')
        item2 = types.KeyboardButton('2')
        item3 = types.KeyboardButton('3')
        item4 = types.KeyboardButton('4')
        item5 = types.KeyboardButton('5')
        item6 = types.KeyboardButton('6')
        markup1.add(item1, item2, item3, item3, item4, item5, item6)
        msg = bot.send_message(message.from_user.id, 'Выберите уровень сложности(1-6): ', reply_markup=markup1)
        bot.register_next_step_handler(msg, set_lvl)

    elif message.text == 'С БОГОМ!(крутануть)':
        flag = is_alive()
        if flag:
            bot.send_message(message.from_user.id, 'КТО Ж ЗНАЛ...')
        else:
            bot.send_message(message.from_user.id, 'КАК ЗАНОВО РОДИЛСЯ!')

    elif message.text == 'Крутить больше некому':
        markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_start = types.KeyboardButton('/start')
        markup_start.add(item_start)
        bot.send_message(message.from_user.id, 'А может еще по одной?', reply_markup=markup_start)






def set_default_values():
    global barrel
    global loaded_barrel

    barrel = [1, 2, 3, 4, 5, 6]
    loaded_barrel = []

def set_lvl(message):
    if message.text == '1':
        k = 1
        load_barrel(k)
    elif message.text == '2':
        k = 2
        load_barrel(k)
    elif message.text == '3':
        k = 3
        load_barrel(k)
    elif message.text == '4':
        k = 4
        load_barrel(k)
    elif message.text == '5':
        k = 5
        load_barrel(k)
    elif message.text == '6':
        k = 6
        load_barrel(k)

    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('С БОГОМ!(крутануть)')
    item2 = types.KeyboardButton('Крутить больше некому')
    markup2.add(item1, item2)
    bot.send_message(message.from_user.id, 'Крутите барабан! ', reply_markup=markup2)

def load_barrel(lvl):
    global barrel
    global loaded_barrel

    for i in range(int(lvl)):
        temp = random.choice(barrel)
        loaded_barrel.append(temp)
        barrel.remove(temp)

def is_alive():
    global barrel
    global loaded_barrel

    destiny = random.randint(1, 6)

    if destiny in loaded_barrel:
        loaded_barrel.remove(destiny)
        return True
    return False

bot.polling(non_stop=True, interval=0)