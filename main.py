from settigs import FILE_VACANCIES
import src.interction as interaction
from src.api_hh import APIHeadHunter
from src.utils import get_data_from_receiver, get_data_from_website, get_vacancies_by_salary, get_vacancies_by_validity_area
from src.parser import parser_data_website
from src.file_worker_json import FileWorkerJson

def main():
    """ Запуск программы """

    user_input = input("Здравствуйте!\n"
                       "Для запуска поиска вакансий нажмите Enter\n")

    # определить формат приемник
    type_container = interaction.choose_container()
    if type_container != 'json':
        print(f"К сожалению для {type_container} код еще не написан")

    # определим параметры отбора данных
    keyword, per_page = interaction.choose_params()

    # получить данные с сайта
    hh_api = APIHeadHunter()
    vacancies_from_site = get_data_from_website(hh_api, keyword, per_page)

    # получить структуру соответствия полей сайта с атрибутами класса Vacancy
    structure_fields = hh_api.structure_fields
    vacancies = parser_data_website(vacancies_from_site, structure_fields)

    print(f"Данные считаны успешно!"
          f"Данные записаны в файл {FILE_VACANCIES}")

    if interaction.choose_way('Вывести данные? [yes/no]'):
        interaction.print_vacancy()

    if interaction.choose_way('Прочитать файл? [yes/no]'):
        if type_container == 'json':
            file = FileWorkerJson
            interaction.print_file(file.get_data())

    if interaction.choose_way('Удалить файл? [yes/no]'):
        file = FileWorkerJson
        file.delete_data()



