from abc import ABC, abstractmethod


class AbstractVacancy(ABC):
    """ Абстрактный класс вакансий """

    @staticmethod
    @abstractmethod
    def get_salary(salary):
        """ Абстрактный метод получение зарплаты из вакансии """

        pass


class Vacancy(AbstractVacancy):
    """ Класс вакансий """

    __slots__ = "name", "url", "salary", "description"

    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = self.get_salary(salary)
        self.description = description

    @staticmethod
    def get_salary(salary):
        """ Получение зарплаты из вакансии """

        return 0 if not salary else salary.get('from') if salary.get('from', False) else 0

    def __le__(self, other):
        """ Определяет поведение оператора меньше или равно, <= """

        return self.salary <= other.salary

    def __ge__(self, other):
        """ Определяет поведение оператора больше или равно, >= """
        return self.salary >= other.salary