import requests
from requests import Response

from api_vacancy_website import APIGetData


class APIHeadHunter(APIGetData):
    """ Класс для API c hh.ru """

    def __init__(self) -> object:
        """ Инициация класса - ввод параметров подключения к сайту вакансий hh.ru"""
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "per_page": "", "only_with_salary": True}

    def get_response(self, keyword, per_page) -> Response:
        """ Отправить запрос на сайт """
        self.params["text"] = keyword
        self.params["per_page"] = per_page
        return requests.get(self.url, params=self.params)

    def get_data(self, keyword: str, per_page: int):
        """ Получить данные по вакансиям с сайта """
        return self.get_response(keyword, per_page).json()["items"]

    @property
    def structure_fields(self):
        """ Получить структуру соответствия данных сайта hh.ru классу Vacancy"""

        return {'name':'name',
                'area/name':'area_name',
                'url':'vacancies_url',
                'salary/currency':'salary_currency',
                'salary/from':'salary_from',
                'salary/to':'salary_to',
                'snippet/requirement':'requirement',
                'snippet/responsibility':'responsibility',
                'employment/name':'employment',
                'experience/name':'experience',
                'schedule/name':'schedule'
                }
