import json
from abc import ABC, abstractmethod

from config import PATH_TO_JSON
from src.vacancy import Vacancy


class AbstractJSONSaver(ABC):
    """ Абстрактный класс AbstractJSONSaver """

    @staticmethod
    @abstractmethod
    def save_to_json(data: list, path: str) -> None:
        """ Абстрактный метод для сохранения вакансий в файле """

        pass

    @staticmethod
    @abstractmethod
    def add_to_json(data: list, path: str) -> None:
        """ Абстрактный метод для добавления вакансий в файл """

        pass

    @staticmethod
    @abstractmethod
    def del_to_json(path: str) -> None:
        """ Абстрактный метод Удаление данных из файла vacancy.json """

        pass


class JSONSaver(AbstractJSONSaver):
    """ Класс для сохранения вакансий"""

    @staticmethod
    def save_to_json(data: list, path: str) -> None:
        """ Метод сохранения вакансий в файле """

        with open(path, 'w', encoding='utf-8') as file:
            res = []
            for i in data:
                res.append({"name": i.name,
                            "url": i.url,
                            "description": i.description,
                            "salary": i.salary
                            })
            #noinspection PyTypeChecker
            json.dump(res, file, ensure_ascii=False, indent=4)

    @staticmethod
    def add_to_json(data: list=None, path: str=None) -> None:
        """ Метод для добавления вакансий в файл """

        with open(path, 'r', encoding='utf-8') as file:
            load_file = json.load(file)

        with open(path, 'w', encoding='utf-8') as file:
            for i in data:
                load_file.append({"name": i.name,
                                  "url": i.url,
                                  "description": i.description,
                                  "salary": i.salary
                                  })
            # noinspection PyTypeChecker
            json.dump(load_file, file, ensure_ascii=False, indent=4)


    @staticmethod
    def del_to_json(path: str) -> None:
        """ Удаление данных из файла vacancy.json """

        with open(path, "w") as file:
            # noinspection PyTypeChecker
            json.dump([], file, ensure_ascii=False, indent=4)

