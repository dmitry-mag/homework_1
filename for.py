"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
def print_avg_school(school):
    total_scores = 0
    total_count = 0
    for school_class in school:
        total_scores += sum(school_class['scores'])
        total_count += len(school_class['scores'])
    print(f'Average score in school: {total_scores / total_count}')


def print_avg_class(school):
    for school_class in school:
        avg_class = sum(school_class['scores']) / len(school_class['scores'])
        current_class = school_class['school_class']
        print(f'Average score in class {current_class}: {avg_class}')


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_scores = [{'school_class': '5a', 'scores': [4, 5, 3, 4, 5, 4, 4, 5]},
                     {'school_class': '5b', 'scores': [4, 3, 3, 5, 2, 4, 4]},
                     {'school_class': '6a', 'scores': [3, 5, 5, 4, 4, 5, 4, 5, 4]},
                     {'school_class': '6b', 'scores': [2, 3, 4, 3, 4, 4, 3, 5]},
                     {'school_class': '7a', 'scores': [5, 5, 3, 4, 3, 3, 4, 3, 3]},
                     {'school_class': '7b', 'scores': [3, 3, 5, 3, 4, 2, 4, 4]},
                    ]
    print_avg_school(school_scores)
    print_avg_class(school_scores)
    
if __name__ == "__main__":
    main()
