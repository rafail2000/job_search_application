import json
from abc import ABC, abstractmethod

from config import PATH_TO_JSON


class AbstractJSONSaver(ABC):
    """ Абстрактный класс AbstractJSONSaver """

    @abstractmethod
    def save_to_json(self, data: list) -> None:
        """ Абстрактный метод для сохранения вакансий в файле """

        pass

    @abstractmethod
    def add_to_json(self, data: list) -> None:
        """ Абстрактный метод для добавления вакансий в файл """

        pass

    @abstractmethod
    def del_to_json(self) -> None:
        """ Абстрактный метод Удаление данных из файла vacancy.json """

        pass

    @abstractmethod
    def receiving_data(self) -> None:
        """ Абстрактный метод получение данных из файла """

        pass


class JSONSaver(AbstractJSONSaver):
    """ Класс для сохранения вакансий"""

    def __init__(self, path: str = PATH_TO_JSON):
        self.path = path

    def save_to_json(self, data: list) -> None:
        """ Метод сохранения вакансий в файле """

        with open(self.path, 'w', encoding='utf-8') as file:
            res = []
            for i in data:
                res.append({"name": i.name,
                            "url": i.url,
                            "description": i.description,
                            "salary": i.salary
                            })
            #noinspection PyTypeChecker
            json.dump(res, file, ensure_ascii=False, indent=4)

    def add_to_json(self, data: list=None) -> None:
        """ Метод для добавления вакансий в файл """

        with open(self.path, 'r', encoding='utf-8') as file:
            load_file = json.load(file)

        with open(self.path, 'w', encoding='utf-8') as file:
            for i in data:
                load_file.append({"name": i.name,
                                  "url": i.url,
                                  "description": i.description,
                                  "salary": i.salary
                                  })
            # noinspection PyTypeChecker
            json.dump(load_file, file, ensure_ascii=False, indent=4)

    def del_to_json(self) -> None:
        """ Удаление данных из файла vacancy.json """

        with open(self.path, "w") as file:
            # noinspection PyTypeChecker
            json.dump([], file, ensure_ascii=False, indent=4)

    def receiving_data(self) -> None:
        """ Получение данных из файла """

        with open(self.path, 'r', encoding='utf-8') as file:
            load_file = json.load(file)
            if len(load_file) < 1:
                print("Нет данных для вывода")
            else:
                for i in load_file:
                    print(f"{i["name"]}\n{i["url"]}\n{i["description"]}\n{i["salary"]}\n")
