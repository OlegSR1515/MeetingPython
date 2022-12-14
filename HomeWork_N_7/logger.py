def wr_log(note:str, nm_fl:str):
    """Записывает данные в новую строку файла "nm_fl" """    
    with open(nm_fl, 'a+', encoding="utf-8") as jr:
        jr.writelines(f'{note}\n')
    print('Контакт записан.')

def re_log(nm_fl:str) -> list:
    """Возвращает данные файла в виде списка строк"""
    with open(nm_fl, 'r', encoding="utf-8") as jr:
        sp = jr.readlines()
    return sp   