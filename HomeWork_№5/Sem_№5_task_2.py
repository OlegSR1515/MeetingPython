# 2. Создайте программу для игры в ""Крестики-нолики"".
#   (в консоли происходит выбор позиции)

from methods import show_desk, prov, bot_O, res_g

#  нарисуем игровое поле с позициями для начала игры
desk_00 = [n for n in range(1, 10)]
desk = desk_00.copy()
show_desk(desk)
#  "in_X" и "in_O" - списки позиций "X" и "O"
in_X = set()
in_O = set()
while desk.count('X') < 4:
#  ходим крестиком
    n_X = prov(in_X, in_O)
    desk[n_X - 1] = 'X'
    in_X.add(n_X)
#  проверка на досрочный выигрыш "X"
    if res_g(in_X) == 1: break
#  ход бота "bot_O" ноликом
    n_O = bot_O(desk)
    desk[n_O - 1] = 'O'
    in_O.add(n_O)
    show_desk(desk)
#  проверка на досрочный выигрыш "O"
    if res_g(in_O) == 1: break

show_desk(desk)

if res_g(in_O) == 1: print('Вы проиграли.. (')
elif res_g(in_X) == 1: print('Победа !')
else: 
    n_X = prov(in_X, in_O)
    desk[n_X - 1] = 'X'
    in_X.add(n_X)
    show_desk(desk)
    if res_g(in_X) == 1: print('Победа !')
    else: print('НИЧЬЯ')

# ******** Вывод в терминал ********
# Сделайте свой ход - 7
# -----------
#  O | O | X 
# -----------
#  4 | X | 6 
# -----------
#  X | 8 | 9 
# -----------

# Победа !
