def print_vacancy(vacancies: list):
    """ Вывести список вакансий в консоль"""
    print("Топ выбранных вакансии по зарплате: \n")
    [print(vacancy) for vacancy in vacancies]


def choose_params():
    """ Получить критерии отбора вакансий от пользователя """

    major_name = input("Какую профессию ищите?\n").lower()
    if not major_name:
        print('Вы не выбрали профессию')
    count = int(input("Сколько записей вывести?\n"))

    return major_name, count

def choose_container():
    """ Получить вариант приемника - тип файла в данной работе"""

    container = input('Выберите тип приемника: [json/txt/csv]')
    return  container.lower().strip()

def choose_way(question):
    """ Выбрать режим работы с файлом """
    mode = input("Вывести данные: [yes/no]?").lower().strip()
    if mode == 'yes':
        return True
    return False


def print_file(file):
    """ Печать содержимого файла"""
    print(file)

