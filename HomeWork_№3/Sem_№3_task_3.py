# 3. Задайте список из вещественных чисел. Напишите программу,
#      которая найдёт разницу между максимальным и минимальным 
#      значением дробной части элементов.

spis = [1.1, 1.2, 3.1, 5, 10.01]
# Удаляем элемент без дробной части(тип данных "int")
spis_n = []
for el in spis:
    if str(type(el)) != "<class 'int'>": spis_n.append(el)

# Функция "frac_pr()" выводит дробную часть числа
def frac_pr(num):
    sn = str(float(num))
    r = ''
    for i in range(len(sn) - 1, -1, - 1):
        if sn[i] != '.':
            r = sn[i] + r
        else: break
    return float(f'.{r}')

spis_fr = [frac_pr(se) for se in spis_n]
print(f'{spis} => {max(spis_fr) - min(spis_fr)}')

# *************** Вывод в терминал *************
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
