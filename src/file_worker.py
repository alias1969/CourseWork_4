from abc import ABC, abstractmethod


class FileWorker(ABC):
    """ Абстрактный класс работы с приемником"""

    def __init__(self, filename):
        self.filename = filename

    def save_data(self):
        """ Записать данные в приемник """
        pass

    def get_data(self):
        """ Получить данные из приемника """
        pass

    def delete_data(self):
        """ Очистить приемник от данных"""
        pass
