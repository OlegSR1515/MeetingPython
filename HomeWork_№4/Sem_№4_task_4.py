# 4'. Задана натуральная степень k. Сформировать случайным образом
#      список коэффициентов (значения от 0 до 100) многочлена и записать
#      в файл многочлен степени k.(записать в строку)

import random
# Функция "polin_wr" принимает на вход имя файла с результатом,
#  создает список случайных коэффициентов полинома и 
#  выводит в первую строку файла с результатом строку полинома.
def polin_wr(name_file):
    k = int(input('Введите степень: '))
    koef = [str(random.randint(0, 100)) for i in range(k + 1) ]
    polin = ''
    for i in range(k + 1):
        if i == 0: polin = koef[i]
        elif i ==1: polin = f'{koef[i]}*x + {polin}'
        else: polin =  f'{koef[i]}*x**{i} + {polin}'
    with open(name_file, 'w') as f:
        f.write(polin)

polin_wr('file_rez.txt')

# ************ Результат ************
#          --- на консоли ---
# Введите степень: 2
#          --- в файле ---
# 1   51*x**2 + 88*x + 1

# ************ Результат ************
#          --- на консоли ---
# Введите степень: 3
#          --- в файле ---
# 1   64*x**3 + 29*x**2 + 34*x + 90

# ************ Результат ************
#          --- на консоли ---
# Введите степень: 5
#          --- в файле ---
# 1   71*x**5 + 18*x**4 + 5*x**3 + 30*x**2 + 4*x + 5
        

