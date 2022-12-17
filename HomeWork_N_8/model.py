# Модуль для выполнения опреаций

import sympy as sm
x = sm.Symbol('x')

def execute_expr(expr:str, t:int) -> str:
    """"Получает на вход строку-пример и переменную t=1 для решения
       уравнения и t=0 для упрощения.
    Возвращает результат примера в виде строки или "Ошибка ввода". """

    try:
        if t:
#  Отбрасываем "=0" для решения и "[" в начале и "]" в конце для вывода.
            return f'{sm.solve(expr[:-2])}'.strip('[]')
        elif not t:
            return sm.simplify(expr)
    except Exception:
        return 'Ошибка ввода'