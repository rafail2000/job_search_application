from abc import ABC, abstractmethod


class AbstractVacancy(ABC):
    """ Абстрактный класс вакансий """

    @staticmethod
    @abstractmethod
    def _validate_name(name: str) -> str:
        """ Абстрактный метод проверка имени """

        pass

    @staticmethod
    @abstractmethod
    def _validate_url(url: str) -> str:
        """ Абстрактный метод проверка url """

        pass

    @staticmethod
    @abstractmethod
    def _validate_salary(salary: dict) -> float:
        """ Абстрактный метод проверки зарплаты """

        pass

    @staticmethod
    @abstractmethod
    def _validate_description(description: str) -> str:
        """ Абстрактный метод проверки описания """

        pass


class Vacancy(AbstractVacancy):
    """ Класс вакансий """

    __slots__ = "name", "url", "salary", "description"

    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = self._validate_salary(salary)
        self.description = description

    @staticmethod
    def _validate_name(name: str) -> str:
        """ Метод проверка имени """

        if name:
            return name
        return "None"

    @staticmethod
    def _validate_url(url: str) -> str:
        """ Метод проверка url """

        if url:
            return url
        return "None"

    @staticmethod
    def _validate_salary(salary: dict) -> float:
        """ Получение зарплаты из вакансии """

        return 0 if not salary\
            else salary.get('from')\
            if salary.get('from', False)\
            else 0

    @staticmethod
    def _validate_description(description: str) -> str:
        """ Метод проверки описания """

        if description:
            return description
        return "None"

    def __le__(self, other):
        """ Определяет поведение оператора меньше или равно, <= """

        return self.salary <= other.salary

    def __ge__(self, other):
        """ Определяет поведение оператора больше или равно, >= """
        return self.salary >= other.salary