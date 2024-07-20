from pathlib import Path

# Работа с файлами
ROOT_PATH = Path(__file__).parent
FILE_VACANCIES = ROOT_PATH.joinpath('data', 'vacancies.json')
FILE_TEST_VACANCIES = ROOT_PATH.joinpath('tests', 'test_vacancies.json')

# Константа, определяющая, где будут храниться данные: файл json, файл txt, файл csv или БД
TYPE_CONTAINER= 'json'

# Курсы валют (фиксированные)
COURSE_CURRENCY_USD = 90
COURSE_CURRENCY_EUR = 100