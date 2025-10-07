from abc import ABC, abstractmethod

import requests


class AbstractHeadHunterAPI(ABC):
    """ Абстрактный класс AbstractHeadHunterAPI """

    @staticmethod
    @abstractmethod
    def __validate_status_cod(response: requests.models.Response) -> bool:
        """ Абстрактный метод проверки ответа сервера """

        pass

    @abstractmethod
    def __load_vacancies(self, keyword: str) -> None:
        """ Абстрактный метод загрузки вакансий"""

        pass


class HeadHunterAPI(AbstractHeadHunterAPI):
    """ Класс для работы с API HeadHunter """

    def __init__(self) -> None:
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    @staticmethod
    def __validate_status_cod(response: requests.models.Response) -> bool:
        """ Метод проверки ответа сервера """

        if response.status_code != 200:
            print(f"status_cod {response.status_code}")
            return True

    def __load_vacancies(self, keyword: str) -> None:
        """ Метод загрузки вакансий """

        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if self.__validate_status_cod(response):
                break
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
