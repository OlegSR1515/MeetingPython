# 5'. Даны два файла, в каждом из которых находится запись многочлена.
#    Задача - сформировать файл, содержащий сумму многочленов.

import sympy
import random
# Функция "polin_wr" принимает на вход имя файла с результатом,
#  создает список случайных коэффициентов полинома и 
#  выводит в первую строку файла с результатом строку полинома.
def polin_wr(name_file):
    k = int(input('Введите степень: '))
    koef = [str(random.randint(0, 100)) for i in range(k + 1)]
    polin = ''
    for i in range(k + 1):
        if i == 0: polin = koef[i]
        elif i ==1: polin = f'{koef[i]}*x + {polin}'
        else: polin =  f'{koef[i]}*x**{i} + {polin}'
    with open(name_file, 'w') as f:
        f.write(polin) 
# Создаем два файла с полиномами.
polin_wr('f_1.txt')
polin_wr('f_2.txt')

with open('f_1.txt', 'r') as f1, open('f_2.txt', 'r') as f2,\
    open('f_rez.txt', 'w') as frez:

    p1 = f1.read()
    p2 = f2.read() 

    x = sympy.Symbol('x')

    rez = sympy.simplify(eval(p1) + eval(p2))

    frez.write(str(rez))

# ************ Результат ************
#          --- на консоли ---
# Введите степень: 2
# Введите степень: 2
#          --- в файлах ---
# "f_1.txt"    1     89*x**2 + 67*x + 60
# "f_2.txt"    1     32*x**2 + 86*x + 76
# "f_rez.txt"  1     121*x**2 + 153*x + 136

#          --- на консоли ---
# Введите степень: 5
# Введите степень: 3
#          --- в файлах ---
# "f_1.txt"    1     73*x**5 + 16*x**4 + 100*x**3 + 8*x**2 + 28*x + 97
# "f_2.txt"    1     74*x**3 + 93*x**2 + 95*x + 3
# "f_rez.txt"  1     73*x**5 + 16*x**4 + 174*x**3 + 101*x**2 + 123*x + 100

