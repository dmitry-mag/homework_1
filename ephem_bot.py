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

# initialization list of cities for future games with users
CITIES = []
with open('cities.txt', 'r', encoding='utf-8') as file:
    for line in file:
        CITIES.append(line.strip().lower())
shuffle(CITIES)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
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
    
    city_name = update.message.text.split()[1].lower()
    if city_name in user_data['cities'] and (city_name[1] == user_data['last_bot_city'][-1]
                                             or not user_data['last_bot_city']):
        user_data['cities'].remove(city_name)
        for city in user_data['cities']:
            if city[1] == city_name[-1]:
                user_data['last_bot_city'] = city
                user_data['cities'].remove(city)
                update.message.reply_text(f'{city.capitalize()}, ваш ход')
                return
        update.message.reply_text(f'Поздравляю, Вы победили, я больше не знаю городов' \
                                  f' на букву {city_name[-1].upper()}')
    else:
        update.message.reply_text('Не знаю такой город или его уже называли')
    

def calculate(bot, update):
    """ Функция еще в разработке!!! """
    user_input = update.message.text
    first = ''
    second = ''
    signs = ['+', '-', '*', '/']
    sign = ''
    result = ''
    for item in user_input:
        if item.isdigit() and not sign:
            first += item
        elif item in signs and not sign:
            sign = item
        elif item in signs and sign:
            update.message.reply_text('Вводите знаки операций по одному!')
            return
        elif item.isdigit() and sign:
            second += item
        elif item in signs and sign and first and second:
            exec(f'first = str(int({first}) {sign} int({second}))')
            sign = item
            second = ''
    # похоже такой exec не работает !!!! Fix it!
    exec(f'result = str(int({first}) {sign} int({second}))')
    update.message.reply_text(f'Результат: {result}')


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
