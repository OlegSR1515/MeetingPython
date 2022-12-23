import telebot
import config
import random
bot = telebot.TeleBot(config.token)		

def biuld_desk(spisok: list) -> str:
    '''Выводит строку для вывода в сообщении телеграмм'''
    p = ' ' * 5
    vv = '.' + p + 18 * '-' + '\n' + p
    for i in range(9):
        ks = '|'
        if i%3 == 2: ks = '\n' + ' ' + p + 18 * '-' + '\n' + p
        vv += f'  {str(spisok[i])}  ' + ks
    return vv

def prov(a:set, b:set, m:str) -> int: 
    '''Выводит "0" если есть ошибка при вводе позиции
    или введеное значение '''
    try:
        if int(m.text) in a|b:
            bot.send_message(m.chat.id, 'Эта позиция занята.\nСделайте другой ход -')
            return 0
        elif 0 > int(m.text) or int(m.text) > 9:
            bot.send_message(m.chat.id, 'Такой позиции нет на доске.\nСделайте другой ход -')
            return 0
        else: 
            return int(m.text)
    except ValueError:
            bot.send_message(m.chat.id, f'Введите число. Вы ввели- {m.text}.\n\
    Сделайте другой ход -')
            return 0

def bot_O(s:list) -> int:
    '''Выводит позицию случайного хода бота'''
    s_r = s.copy()
    s_in = [el for el in s if type(el) == int]
    n_rnd = random.randint(0, len(s_in) - 1)
    n_O = s_in[n_rnd]
    return n_O

def res_g(nom:list) -> int:
    '''Проверяет выигрыш игрока'''
    b = [{1, 2, 3}, {1, 4, 7}, {1, 5, 9}, {4, 5, 6}, {7, 8, 9},\
        {3, 5, 7}, {2, 5, 8}, {3, 6, 9}]
    rez = 0
    for mn in b:
        if nom >= mn: rez = 1
    return rez
 
