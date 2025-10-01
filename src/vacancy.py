from abc import ABC, abstractmethod


class AbstractVacancy(ABC):
    """ Абстрактный класс вакансий """

    @abstractmethod
    def __le__(self, other):
        """ Определяет поведение оператора меньше или равно, <= """

        pass

    @abstractmethod
    def __ge__(self, other):
        """ Определяет поведение оператора меньше или равно, <= """

        pass


class Vacancy(AbstractVacancy):
    """ Класс вакансий """

    __slots__ = "name", "url", "salary", "description"

    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = 0 if not salary else salary.get('from') if salary.get('from', False) else 0
        self.description = description

    def __le__(self, other):
        """ Определяет поведение оператора меньше или равно, <= """

        return self.salary <= other.salary

    def __ge__(self, other):
        """ Определяет поведение оператора больше или равно, >= """
        return self.salary >= other.salary