import random
import colorama
from colorama import Fore, Style
colorama.init()

# Метод "show_desk" рисует в терминале игровое поле с ходами игроков
#   из списка "spp"
def show_desk(spp:list):
    n = 0
    print(Fore.CYAN + 11 * '-')
    for i in range(0, len(spp)):
        ks = "|"
        c_el = Fore.CYAN
        if i%3 == 2: ks = '\n' + 11 * '-' + '\n'
        if spp[i] == 'O': c_el = Fore.YELLOW
        if spp[i] == 'X': c_el = Fore.RED
        print(c_el + f' {spp[i]} ' + Fore.CYAN , end = ks)
    print(Style.RESET_ALL)

# Метод "bot_O" получает список текущей доски, выбирает случайную позицию
#   из оставшихся и возвращает её
def bot_O(s:list) -> int:
    s_r = s.copy()
    s_in = [el for el in s if type(el) == int]
    n_rnd = random.randint(0, len(s_in) - 1)
    n_O = s_in[n_rnd]
    return n_O
#  Метод "res_g" получает список позиций игрока и проверяет
#   его на выигрыш (возвращает "1")
def res_g(nom:list) -> int:
    b = [{1, 2, 3}, {1, 4, 7}, {1, 5, 9}, {4, 5, 6}, {7, 8, 9},\
        {3, 5, 7}, {2, 5, 8}, {3, 6, 9}]
    rez = 0
    for mn in b:
        if nom >= mn: rez = 1
    return rez

# Метод "prov" проверяет введённую позицию
def prov(a:set, b:set) -> int: 
    c = int(input('Сделайте свой ход - '))
    if c in a|b:
        print('Эта позиция занята.')
        return prov(a, b)
    elif 0 > c or c > 9: 
        print('Такой позиции нет на доске.')
        return prov(a, b)
    else: return c 



