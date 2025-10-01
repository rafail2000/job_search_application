from src.vacancy import Vacancy


def add_vacancy_in_lst(vacancy: list) -> list:
    """ Добавление объектов класса Vacancy в список """

    return [Vacancy(i['name'], i['url'], i.get('salary', 0), i['snippet']['requirement']) for i in vacancy]


def filter_vacancies(vacancies_list: list, filter_words:list) -> list:
    """ Фильтрация вакансий по ключевым словам """

    filter_none = [i for i in vacancies_list if i.description]

    return [i for i in filter_none if any(True if j in i.description else False for j in filter_words)]


def get_vacancies_by_salary(filtered_vacancies: list, salary_range: list) -> list:
    """ Фильтрация вакансий по диапазону зарплат """

    low_range, height_range = salary_range

    return [i for i in filtered_vacancies if float(low_range) <= i.salary <= float(height_range)]

def get_sort_vacancy(vacancy: list) -> list:
    """ Сортировка вакансий по убыванию """

    return sorted(vacancy, key=lambda x: x.salary, reverse=True)

def get_top_vacancies(sorted_vacancies: list, top_n: int) -> list:
    """ Получение списка из N-го кол-ва вакансий """

    if len(sorted_vacancies) < top_n + 1:
        return sorted_vacancies
    return sorted_vacancies[:top_n]
