import json

from file_worker import FileWorker
from settings import FILE_VACANCIES


class FileWorkerJson(FileWorker):
    """ Класс для работы с файлом данных json"""

    def __init__(self, filename: str):
        super().__init__(filename)

    def save_data(self, data: dict):
        """ Запись данные в файл json """
        with open(self.filename, "w", encoding="utf-8") as file:
            return json.dump(data, file, ensure_ascii=False, indent=4)

    def get_data(self):
        """ Получить данные из файла json """
        try:
            return json.load(open(self.filename))
        except FileNotFoundError:
            return []

    def delete_data(self):
        """ Удалить данных из файла"""
        with open(self.filename, "w", encoding="utf-8") as file:
            return json.dump([], file, ensure_ascii=False, indent=4)
