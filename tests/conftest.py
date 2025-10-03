import pytest

from src.api import HeadHunterAPI
from src.vacancy import Vacancy


@pytest.fixture
def api_class():
    """ Фикстура создает экземпляр API """

    return HeadHunterAPI()


@pytest.fixture
def vacancy_class():
    """ Фикстура создает экземпляр Vacancy """

    return Vacancy(
        name="Backend (Go/Python) Developer",
        url="https://api.hh.ru/vacancies/125879653?host=hh.ru",
        description="Опыт коммерческой разработки от 1 года. Уверенное программирование на <highlighttext>Python</highlighttext>. Навык и опыт написания чистых SQL-запросов (без использования ORM). ",
        salary={"from": 100000}
    )

@pytest.fixture
def vacancy_class_low_salary():
    """ Фикстура создает экземпляр Vacancy """

    return Vacancy(
        name="Backend (Go/Python) Developer",
        url="https://api.hh.ru/vacancies/125879653?host=hh.ru",
        description="Опыт коммерческой разработки от 1 года. Уверенное программирование на <highlighttext>Python</highlighttext>. Навык и опыт написания чистых SQL-запросов (без использования ORM). ",
        salary={"from": 10}
    )

