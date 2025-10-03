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

@pytest.fixture
def raw_data():
    """ Фикстура с данными с сайта hh """

    return [{
      "id": "93353083",
      "premium": False,
      "name": "Тестировщик комфорта квартир",
      "department": False,
      "has_test": False,
      "response_letter_required": False,
      "area": {
        "id": "26",
        "name": "Воронеж",
        "url": "https://api.hh.ru/areas/26"
      },
      "salary": {
        "from": 350000,
        "to": 450000,
        "currency": "RUR",
        "gross": False
      },
      "type": {
        "id": "open",
        "name": "Открытая"
      },
      "address": False,
      "response_url": False,
      "sort_point_distance": False,
      "published_at": "2024-02-16T14:58:28+0300",
      "created_at": "2024-02-16T14:58:28+0300",
      "archived": False,
      "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=93353083",
      "branding": {
        "type": "CONSTRUCTOR",
        "tariff": "BASIC"
      },
      "show_logo_in_search": False,
      "insider_interview": False,
      "url": "https://api.hh.ru/vacancies/93353083?host=hh.ru",
      "alternate_url": "https://hh.ru/vacancy/93353083",
      "relations": [],
      "employer": {
        "id": "3499705",
        "name": "Специализированный застройщик BM GROUP",
        "url": "https://api.hh.ru/employers/3499705",
        "alternate_url": "https://hh.ru/employer/3499705",
        "logo_urls": {
          "original": "https://hhcdn.ru/employer-logo-original/1214854.png",
          "240": "https://hhcdn.ru/employer-logo/6479866.png",
          "90": "https://hhcdn.ru/employer-logo/6479865.png"
        },
        "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3499705",
        "accredited_it_employer": False,
        "trusted": False
      },
      "snippet": {
        "requirement": "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...",
        "responsibility": "Оценивать вид из окна: встречать рассветы на кухне, и провожать алые закаты в спальне. Оценивать инфраструктуру района: ежедневно ходить на..."
      },
      "contacts": False,
      "schedule": {
        "id": "flexible",
        "name": "Гибкий график"
      },
      "working_days": [],
      "working_time_intervals": [],
      "working_time_modes": [],
      "accept_temporary": False,
      "professional_roles": [
        {
          "id": "107",
          "name": "Руководитель проектов"
        }
      ],
      "accept_incomplete_resumes": False,
      "experience": {
        "id": "noExperience",
        "name": "Нет опыта"
      },
      "employment": {
        "id": "full",
        "name": "Полная занятость"
      },
      "adv_response_url": False,
      "is_adv_vacancy": False,
      "adv_context": False
    }]


@pytest.fixture
def lst_obj_data():
    """ Фикстура с объектами класс Vacancy """

    return [Vacancy(
        name="Backend (Go/Python) Developer",
        url="https://api.hh.ru/vacancies/125868593?host=hh.ru",
        description="Нужно: 1–3+ лет коммерческой разработки на <highlighttext>Python</highlighttext> или Go (желательно оба). Уверенный SQL, PostgreSQL (индексы, планы, транзакции). ",
        salary={"from": 50000}
    ),
        Vacancy(
            name="Backend (Go/Python) Developer",
            url="https://api.hh.ru/vacancies/125868593?host=hh.ru",
            description="Нужно: 1–3+ лет коммерческой разработки на <highlighttext>Python</highlighttext> или (желательно оба). Уверенный, PostgreSQL (индексы, планы, транзакции). ",
            salary={"from": 100000}
        )]