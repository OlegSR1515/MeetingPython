# 2. Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число:  '))
nab = [1]
for i in range(1, n):
    nab.append(nab[i - 1] * (i + 1))
print(f'пусть N = {n}, тогда {nab}')

# ************** Вывод на консоль **************
# Введите число:  4
# пусть N = 4, тогда [1, 2, 6, 24]