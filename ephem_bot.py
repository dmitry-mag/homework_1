"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import shuffle

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

# use environ variable for telegram bot key, need key BOT_KEY
KEY = os.environ.get('BOT_KEY')
if not KEY:
    logging.warning('WARNING!! BOT_KEY environ variable not found!!')

# initialization list of cities for future games with users and shuffle
CITIES = []
with open('cities.txt', 'r', encoding='utf-8') as file:
    for line in file:
        CITIES.append(line.strip().lower())
shuffle(CITIES)


PROXY = {
    'proxy_url': 'socks5h://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def planet_info(bot, update):
    planet_name = update.message.text.split()[1]
    planet_class = getattr(ephem, planet_name.capitalize(), None)
    if not planet_class:
        update.message.reply_text('Не знаю такой планеты..')
        return
    planet = planet_class()
    planet.compute()
    planet_constellation = ephem.constellation(planet)[1]
    update.message.reply_text(f'Планета {planet_name.capitalize()} сегодня в' \
                                f' созвездии {planet_constellation}')


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


def play_cities(bot, update, user_data):
    """ function for cities game """

    # check for first start with current player
    if 'cities' not in user_data:
        user_data['cities'] = list(CITIES)
        user_data['last_bot_city'] = ''
    
    current_user_city = update.message.text.split()[1].lower()
    # check is the city in our list of cities
    if current_user_city in user_data['cities']:
        # check does the first letter of user city equals last letter of bot city
        # or it is first players turn
        if not user_data['last_bot_city'] or \
                        current_user_city[0] == user_data['last_bot_city'][-1]:            
            user_data['cities'].remove(current_user_city)
            # try to find good city for bot answer
            for city in user_data['cities']:
                if city[0] == current_user_city[-1]:
                    user_data['last_bot_city'] = city
                    user_data['cities'].remove(city)
                    update.message.reply_text(f'{city.capitalize()}, your turn')
                    return
            # not found city
            update.message.reply_text(f"Congratulations! You win, I don't know " \
                   f'more cities begins with "{current_user_city[-1].upper()}"')
        else:
            # user city in list, but not acceptable
            update.message.reply_text(f'Your next city must begins with ' \
                    f'"{user_data["last_bot_city"][-1].capitalize()}" letter')
    else:
        # city not in list of cities
        update.message.reply_text("I don't know this city or " \
                                             "it has already used in game")
    

def calculate(bot, update):
    """ function emulating calculator """

    # right now it is dummy
    user_input = update.message.text
    signs = ['+', '-', '*', '/']
    result_string = '2 + 2'
    for symbol in user_input:
        pass
    result = eval(result_string)
    update.message.reply_text(f'Result is {result}')


def main():
    mybot = Updater(KEY, request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("cities", play_cities, pass_user_data=True))
    dp.add_handler(CommandHandler("calc", calculate))

    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
