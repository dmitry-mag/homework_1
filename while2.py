"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    question_dict = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую',
                    'Как тебя зовут?': 'Чижик', 'Где живешь?': 'В интернете'}
    while True:
        user_input = input('Введите вопрос: ')
        if user_input == 'выход':
            break
        if user_input in question_dict:
            print(question_dict[user_input])


if __name__ == "__main__":
    ask_user()
