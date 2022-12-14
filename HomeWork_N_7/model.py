def list_str(spis:list) -> str:
    """Возврвщает строку с разделителем "//" """
    return f'{spis[0]}//{spis[1]}'

def note_find(spis:list, fn_el:str, pos:int) -> list:
    """Выводит результат поиска в виде списка строк"""
    for st in spis:
# Отрезаем "\n" в конце строки
        st = st[:-1]
# Выбираем фамилию-"[0]" или телефон-"[1]"
        fn = st.split('//')[pos - 1]
        if fn == fn_el: 
            return st.split('//')
