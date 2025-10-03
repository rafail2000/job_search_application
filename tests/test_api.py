from unittest.mock import patch, Mock


def test_init_api_class(api_class):
    """ Тесты инициализации класса """

    assert api_class.url == 'https://api.hh.ru/vacancies'
    assert api_class.headers == {'User-Agent': 'HH-User-Agent'}
    assert api_class.params == {'text': '', 'page': 0, 'per_page': 100}
    assert api_class.vacancies == []


@patch('src.api.requests.get')
def test_load_vacancies(mock_get, api_class):
    """ Тест загрузки вакансий """

    mock_response = Mock()
    mock_response.json.return_value = {
        'items': [
            {'id': '1', 'name': 'Python Developer', 'salary': {'from': 100000}},
            {'id': '2', 'name': 'Python Engineer', 'salary': None}
        ]
    }
    mock_get.return_value = mock_response

    api_class.load_vacancies("Python")

    assert len(api_class.vacancies) == 40
    assert api_class.vacancies[0]['name'] == 'Python Developer'

    assert mock_get.call_count == 20

    first_call = mock_get.call_args_list[0]
    url, kwargs = first_call
    assert kwargs['params']['text'] == 'Python'
    assert kwargs['params']['page'] == 20
