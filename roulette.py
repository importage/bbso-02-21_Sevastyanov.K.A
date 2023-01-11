import random
import telebot
from telebot import types
from main import bot

wins = 0
looses = 0
num = None
bet = ''

@bot.message_handler(content_types=['text'])
def start(message):
    global wins
    global looses
    global bet
    global num

    if message.text == 'Рулетка':
        set_default_values()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_start = types.KeyboardButton('Начать игру!')
        markup.add(item_start)
        bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=markup)

    elif message.text == 'Начать игру!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_red = types.KeyboardButton('Красные(Четные)')
        item_black = types.KeyboardButton('Черные(нечетные)')
        item_numbers = types.KeyboardButton('Выбрать номер')
        markup.add(item_red, item_black, item_numbers)
        bot.send_message(message.from_user.id, 'На что ставим?', reply_markup=markup)

    elif message.text == 'Красные(Четные)':
        bet = 'red'
        temp = is_winner()
        markup_to_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_start = types.KeyboardButton('Начать игру!')
        markup_to_start.add(item_start)
        if temp:
            bot.send_message(message.from_user.id, f'Выпало {num}\nТы выиграл!')
            bot.send_message(message.from_user.id, f'Побед: {wins}\tПоражений: {looses}', reply_markup=markup_to_start)
        else:
            bot.send_message(message.from_user.id, f'Выпало {num}\nНичего, бывает...\nМожет еще по одной?')
            bot.send_message(message.from_user.id, f'Побед: {wins}\tПоражений: {looses}', reply_markup=markup_to_start)

    elif message.text == 'Черные(нечетные)':
        bet = 'black'
        temp = is_winner()
        markup_to_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_start = types.KeyboardButton('Начать игру!')
        markup_to_start.add(item_start)
        if temp:
            bot.send_message(message.from_user.id, f'Выпало {num}\nТы выиграл!')
            bot.send_message(message.from_user.id, f'Побед: {wins}\tПоражений: {looses}', reply_markup=markup_to_start)
        else:
            bot.send_message(message.from_user.id, f'Выпало {num}\nНичего, бывает...\nМожет еще по одной?')
            bot.send_message(message.from_user.id, f'Побед: {wins}\tПоражений: {looses}', reply_markup=markup_to_start)

    elif message.text == 'Выбрать номер':
        choice = bot.send_message(message.from_user.id, 'Введите число от 0 до 36')
        bot.register_next_step_handler(choice, set_number)


def set_default_values():
    global wins
    global looses

    wins = 0
    looses = 0

def set_number(message):
    global bet
    global num


    if message.text.isdigit() and int(message.text) <= 36 and int(message.text) >= 0:
        bet = int(message.text)


    temp = is_winner()
    markup_to_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_start = types.KeyboardButton('Начать игру!')
    markup_to_start.add(item_start)
    if temp:
        bot.send_message(message.from_user.id, f'Выпало {num}\nТы выиграл!')
        bot.send_message(message.from_user.id, f'Побед: {wins}\tПоражений: {looses}', reply_markup=markup_to_start)
    else:
        bot.send_message(message.from_user.id, f'Выпало {num}\nНичего, бывает...\nМожет еще по одной?')
        bot.send_message(message.from_user.id, f'Побед: {wins}\tПоражений: {looses}', reply_markup=markup_to_start)

def is_winner():
    global wins
    global looses
    global bet
    global num

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_start = types.KeyboardButton('Начать игру!')
    markup.add(item_start)

    ball = random.randint(0, 36)
    num = ball

    if ball % 2 == 0 and ball != 0 and bet == 'red':
        wins += 1
        return True
    elif ball % 2 == 1 and ball != 0 and bet == 'black':
        wins += 1
        return True
    elif ball == bet:
        wins += 1
        return True
    else:
        looses += 1
        return False

bot.polling(none_stop=True, interval=0)


