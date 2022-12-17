# Модуль для записи результатов вычислений

NF = 'journal.csv'
def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
            в виде |задача -> ответ|"""

    with open(NF, 'a', encoding='utf-8') as f:
        z = f'{expr} -> {result}\n'
        f.write(z)


def get_history() -> str:
    """"Возвращает строку с содержимым журнала или
        "Записей нет", если в журнале записей не было."""
    try:
        with open(NF, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return 'Записей нет.'


