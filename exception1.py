"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
    """
    question_dict = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую',
                    'Как тебя зовут?': 'Чижик', 'Где живешь?': 'В интернете'}
    while True:
        try:
            user_input = input('Введите вопрос: ')
        except KeyboardInterrupt:
            print('Пока!')
            break
        if user_input in question_dict:
            print(question_dict[user_input])
    
if __name__ == "__main__":
    ask_user()
