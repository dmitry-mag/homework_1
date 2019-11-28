"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def check_strings(string_1, string_2):
    if not isinstance(string_1, str) or not isinstance(string_2, str):
        return 0
    if string_1 == string_2:
        return 1
    if string_1 != string_2 and len(string_1) > len(string_2):
        return 2
    if string_1 != string_2 and string_2 == 'learn':
        return 3
    
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(check_strings(14, 'elephant'))
    print(check_strings('chitah', 'chitah'))
    print(check_strings('peacock', 'dog'))
    print(check_strings('python', 'learn'))
    print(check_strings('dig', 'learn'))
    print(check_strings('some', 'someone else'))
    
if __name__ == "__main__":
    main()
