from os import stat
import telebot
import random
from telebot import types
from main import bot

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4 + [10] * 12
random.shuffle(cards)

winner = 'none'
packs = {'main': 0, 'croupier': 0}
stats = {'wins': 0, 'loses': 0, 'nones': 0, 'games': 0, 'kd': 0}


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global packs
    global stats

    wins = str(stats['wins'])
    loses = str(stats['loses'])
    nones = str(stats['nones'])
    games = str(stats['games'])
    kd = str(stats['kd'])

    if message.text == 'Черный Джек':
        set_default_packs()
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        hit = types.KeyboardButton("Начать игру")
        stand = types.KeyboardButton("Статистика")
        markup.add(hit, stand)
        bot.send_message(message.from_user.id, 'Добро пожаловать!', reply_markup=markup)

    elif message.text == 'Статистика':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        hit = types.KeyboardButton("Начать игру")
        markup.add(hit)
        if stats['games'] > 20:
            bot.send_message(message.from_user.id,
                             'Статистика:\n\nПобед: ' + wins + '\n\nПоражений: ' + loses + '\n\nНичьих: ' + nones + '\n\nСыграно игр: ' + games + '\n\nПроцент побед: ' + kd,
                             reply_markup=markup)
        elif stats['games'] < 20:
            bot.send_message(message.from_user.id,
                             'Статистика:\n\nПобед: ' + wins + '\n\nПоражений: ' + loses + '\n\nНичьих: ' + nones + '\n\nСыграно игр: ' + games + '\n\nПроцент побед: доступно только после 20 игр!',
                             reply_markup=markup)

    elif message.text == 'Начать игру' or message.text == 'Hit':
        if message.text == 'Начать игру':
            get_cards_main()
            get_cards_croupier()
        if packs['main'] < 21:
            get_cards_main()
            get_cards_croupier()
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            hit = types.KeyboardButton("Hit")
            stand = types.KeyboardButton("Stand")
            markup.add(hit, stand)
            if packs['main'] < 21:
                bot.send_message(message.from_user.id, 'Вы взяли карту.\nБаланс: ' + str(packs['main']),
                                 reply_markup=markup)

            elif packs['main'] > 21:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                hit = types.KeyboardButton("Начать игру")
                markup.add(hit)
                bot.send_message(message.from_user.id,
                                 'Вы проиграли!\nВаш баланс: ' + str(packs['main']) + '\nБаланс крупье: ' + str(
                                     packs['croupier']), reply_markup=markup)
                set_default_packs()

    elif message.text == 'Stand':
        while packs['croupier'] <= 16:
            get_cards_croupier()

        get_winner()
        if winner == 'self':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            hit = types.KeyboardButton("Начать игру")
            stand = types.KeyboardButton("Статистика")
            markup.add(hit, stand)
            bot.send_message(message.from_user.id,
                             'Вы выиграли!\nВаш баланс: ' + str(packs['main']) + '\nБаланс крупье: ' + str(
                                 packs['croupier']), reply_markup=markup)
            set_default_packs()

        elif winner == 'croupier':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            hit = types.KeyboardButton("Начать игру")
            stand = types.KeyboardButton("Статистика")
            markup.add(hit, stand)
            bot.send_message(message.from_user.id,
                             'Вы проиграли!\nВаш баланс: ' + str(packs['main']) + '\nБаланс крупье: ' + str(
                                 packs['croupier']), reply_markup=markup)
            set_default_packs()

        elif winner == 'none':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            hit = types.KeyboardButton("Начать игру")
            stand = types.KeyboardButton("Статистика")
            markup.add(hit, stand)
            bot.send_message(message.from_user.id,
                             'Ничья!\nВаш баланс: ' + str(packs['main']) + '\nБаланс крупье: ' + str(
                                 packs['croupier']), reply_markup=markup)
            set_default_packs()

    if packs['main'] == 21:
        get_winner()
        if winner == 'self':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            hit = types.KeyboardButton("Начать игру")
            stand = types.KeyboardButton("Статистика")
            markup.add(hit, stand)
            bot.send_message(message.from_user.id,
                             'Вы выиграли!\nВаш баланс: ' + str(packs['main']) + '\nБаланс крупье: ' + str(
                                 packs['croupier']), reply_markup=markup)
            set_default_packs()

    return


def get_cards_main():
    global packs
    packs['main'] += cards.pop()
    return


def get_cards_croupier():
    global packs

    if packs['croupier'] <= 16:
        packs['croupier'] += cards.pop()
    return


def set_default_packs():
    global cards
    global packs

    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4 + [10] * 12
    random.shuffle(cards)
    packs['main'] = 0
    packs['croupier'] = 0
    return


def get_winner():
    global stats
    global winner
    global packs

    if packs['main'] <= 21 and (packs['croupier'] < packs['main'] or packs['croupier'] > 21):
        winner = 'self'
        stats['wins'] += 1
    elif packs['main'] == packs['croupier']:
        winner = 'none'
        stats['nones'] += 1
    else:
        winner = 'croupier'
        stats['loses'] += 1

    stats['games'] += 1
    if stats['games'] > 20:
        wins_loses_percent = round(stats['wins'] / stats['loses'], 2)
        stats['kd'] = wins_loses_percent

    return


bot.polling(none_stop=True, interval=0)

