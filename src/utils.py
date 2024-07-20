from file_worker_json import FileWorkerJson
from settigs import FILE_VACANCIES, TYPE_CONTAINER


def get_data_from_website(api, keyword, per_page) -> dict:
    """ Прочитать данные с сайта в словарь """
    return api.get_data(keyword, per_page)


def get_data_from_receiver() -> dict:
    """ Получить данные из приемника в словарь"""

    if TYPE_CONTAINER == 'json':
        return FileWorkerJson(FILE_VACANCIES).get_data()
    else:
        raise f'К сожалению для типа приемника {TYPE_CONTAINER} код еше не написан'


def save_to_container(data:dict):
    """ Записать данные из словаря в приемник
    :param data: dict
    :return: None
    """
    if TYPE_CONTAINER == 'json':
        file = FileWorkerJson(FILE_VACANCIES)
        file.save_data(data)
    else:
        raise f'К сожалению для типа приемника {TYPE_CONTAINER} код еше не написан'


def get_vacancies_by_salary(min_salary, max_salary):
    """Получить из приемника список вакансий по диапазону зарплаты"""

    result = []

    # получим словарь данных из приемника
    dict_vacancies = get_data_from_receiver()

    for vacancy in dict_vacancies:
        # отбираем вакансий по диапазону зарплат
        if vacancy.salary_from >= min_salary and vacancy.salary_to <= max_salary:
            result.append(vacancy)

    return result


def get_vacancies_by_validity_area():
    """ Получить из приёмника список вакансий с указанной локаций - без пустых"""

    result = []

    # получим словарь данных из приемника
    dict_vacancies = get_data_from_receiver()

    for vacancy in dict_vacancies:
        # отбираем вакансий где указана локация
        if vacancy.area_name:
            result.append(vacancy)

    return result





