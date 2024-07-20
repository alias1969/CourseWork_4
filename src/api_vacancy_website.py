from abc import ABC, abstractmethod


class APIGetData(ABC):
    """Класс для работы с json"""

    @abstractmethod
    def get_response(self, keyword, per_page):
        """ Отправить запрос на сайт"""
        pass

    @abstractmethod
    def get_data(self, keyword, per_page):
        """ Получить данные """
        pass

    @abstractmethod
    def structure_fields(self):
        """ Вернуть структуру соответствия полей источника с полями приемника"""
        pass