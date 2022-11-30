# 5. Задайте число. Составьте список чисел Фибоначчи,
#      в том числе для отрицательных индексов.

def fibb(n):
    if n == 0: return 0
    elif n == 1 or n == - 1: return 1
    elif n < 0: return fibb(n + 2) - fibb(n + 1)
    else: return fibb(n - 1) + fibb(n - 2)

count = int(input('Для к =  '))
f_s = []
for i in range(- count, count + 1):
    f_s.append(fibb(i))
print(f'Ряд фибоначчи:{f_s}')    

# *************** Вывод в терминал *************
# Для к =  8
# Ряд фибоначчи:[-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]