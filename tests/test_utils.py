from src.utils import add_vacancy_in_lst, filter_vacancies, get_vacancies_by_salary, get_sort_vacancy, get_top_vacancies


def test_add_vacancy_in_lst(raw_data):
    """ Добавление объектов класса Vacancy в список """

    obj = add_vacancy_in_lst(raw_data)[0]
    assert obj.name == "Тестировщик комфорта квартир"
    assert obj.url == "https://api.hh.ru/vacancies/93353083?host=hh.ru"
    assert obj.salary == 350000
    assert obj.description == "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением..."


def test_filter_vacancies(lst_obj_data):
    """ Фильтрация вакансий по ключевым словам """

    res = filter_vacancies(lst_obj_data, ["Go", "SQL"])
    assert  len(res) == 2


def test_get_vacancies_by_salary(lst_obj_data):
    """  Тесты для функции фильтрации по зарплате """

    res = get_vacancies_by_salary(lst_obj_data, [80_000, 120_000])
    assert len(res) == 1


def test_get_sort_vacancy(lst_obj_data):
    """ Тест функции сортировки по зарплате """

    res = get_sort_vacancy(lst_obj_data)
    assert res[0].salary == 100_000
    assert res[1].salary == 50_000


def test_get_top_vacancies(lst_obj_data):
    """ Тесты функции по выводу Top_n """

    res = get_top_vacancies(lst_obj_data, 0)
    assert len(res) == 0
    res = get_top_vacancies(lst_obj_data, 1)
    assert len(res) == 1
    res = get_top_vacancies(lst_obj_data, 2)
    assert len(res) == 2
    res = get_top_vacancies(lst_obj_data, 3)
    assert len(res) == 2
