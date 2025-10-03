def test_vacancy_init(vacancy_class):
    """ Тесты инициализации класса Vacancy """

    assert vacancy_class.name == "Backend (Go/Python) Developer"
    assert vacancy_class.url == "https://api.hh.ru/vacancies/125879653?host=hh.ru"
    assert vacancy_class.salary == 100000
    assert vacancy_class.description == "Опыт коммерческой разработки от 1 года. Уверенное программирование на <highlighttext>Python</highlighttext>. Навык и опыт написания чистых SQL-запросов (без использования ORM). "


def test_le_dunder_method(vacancy_class, vacancy_class_low_salary):
    """ Тесты магического метода __le__ """

    assert vacancy_class_low_salary <= vacancy_class


def test_ge_dunder_method(vacancy_class, vacancy_class_low_salary):
    """ Тесты магического метода __ge__ """

    assert vacancy_class >= vacancy_class_low_salary


