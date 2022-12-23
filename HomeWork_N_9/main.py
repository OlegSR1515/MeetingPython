import telebot
import config
import model as md

bot = telebot.TeleBot(config.token)		

@bot.message_handler(commands = ['start'])			
def tel_start(m) -> str:
    global desk_curr
    desk_curr= [el for el in range(1, 10)]
    global in_X, in_O
    in_X = set() 
    in_O = set()
    message = '.       Сыграем ?\n' + md.biuld_desk(desk_curr) + '\nСделайте свой ход -'
    bot.send_message(m.chat.id, message)
# **********************************************

@bot.message_handler(func=lambda message: True)	
def tel_game(m):
    n_X = md.prov(in_X, in_O, m)
    if not n_X: pass
    else:
        desk_curr[n_X - 1] = 'X'
        in_X.add(n_X)
        if desk_curr.count('O') < 4:
            n_O = md.bot_O(desk_curr)
            desk_curr[n_O - 1] = 'O'
            in_O.add(n_O)

        message = md.biuld_desk(desk_curr)
        bot.send_message(m.chat.id, message)          

        if md.res_g(in_O) == 1:
            message = 'Вы проиграли.. (\nЕщё раз - нажмите\n       /start'
        elif md.res_g(in_X) == 1:
            message = '.     Победа !\nЕщё раз - нажмите\n         /start'
        elif desk_curr.count('X') == 5:
            message = '.     НИЧЬЯ.\nЕщё раз - нажмите\n           /start'
        else: 
            message = '\nСделайте свой ход -'    
        bot.send_message(m.chat.id, message)          

bot.infinity_polling()	
