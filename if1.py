"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def what_he_doing(age):
    """ check user age, return string """
    if age < 7:
        return 'Go to the children garden, kid!'
    elif age < 18:
        return 'I think your teacher is searching you right now in the classroom'
    elif age < 24:
        return 'You has learned many things, in university, eah?'
    else:
        return 'Games over, work hard, welcom to the real world, Neo'

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    user_age = int(input('Enter your age: '))
    user_doing = what_he_doing(user_age)
    print(user_doing)

if __name__ == "__main__":
    main()
