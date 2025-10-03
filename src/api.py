from abc import ABC, abstractmethod

import requests


class AbstractHeadHunterAPI(ABC):
    """ Абстрактный класс AbstractHeadHunterAPI """

    @abstractmethod
    def load_vacancies(self, keyword: str) -> None:
        """ Абстрактный метод загрузки вакансий"""

        pass


class HeadHunterAPI(AbstractHeadHunterAPI):
    """ Класс для работы с API HeadHunter """

    def __init__(self) -> None:
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword: str) -> None:
        """ Метод загрузки вакансий """

        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
