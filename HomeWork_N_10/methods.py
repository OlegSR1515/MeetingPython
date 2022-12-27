import requests
from bs4 import BeautifulSoup
url = 'https://www.banki.ru/products/currency/cash/nizhniy_novgorod/'
klas = 'table-flex__cell table-flex__cell--without-padding padding-left-default'

def curs(mess = None) ->str:
    ''' Получает введеную строку. Выводит строку с результатом.'''
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    # Проверка кнопки осуществившей ввод
    if '$' in mess:
        n = 0
        v = 'доллар.'
    elif '€' in mess: 
        n = 1
        v = 'евро.'

    string = str(soup.find_all(class_= klas)[n])
    curs_v = string[string.find('>')+1:string.find('</div>'):].replace(',', '.')
    return f'{mess[:-1]}\n  *{curs_v}*  _руб./{v}_'