from view import get_expr as gex, show_res as shr
from model import execute_expr as ee
from logger import get_history as hlog, log_exec as elog

# Реализовать калькулятор с системой логирования:
# 1) решение вводимых примеров (2+3) -> 5 ; 2**3 + (3+6)/(1+2) ->  11
# 2) решение уравнений (x+3 = 0) -> -3
# 3) упрощение многочленов (x*2 + 3*x2 + 4) -> 4*x*2 + 4
# Записать в файл "задачу" от пользователя и ответ.

def run_calc():
    expr_0 = gex()
# Удаляем пробелы
    expr = expr_0.replace(' ', '') 
# Выбираем просмотр журнала
    if expr == '':
        rez = f'Проверка журнала:\n{hlog()}'
# Выбираем уравнение для решения. Выводим корни через ";".
    elif '=0' in expr:
        rez = ee(expr, 1).replace(',', ';') 
        elog(expr_0, rez)
# Выбираем выражение для упрощения.
    else:
        rez = ee(expr, 0)
        elog(expr_0, rez)
    shr(rez)