import json
from abc import ABC, abstractmethod


class AbstractJSONSaver(ABC):
    """ Абстрактный класс AbstractJSONSaver """

    @abstractmethod
    def save_to_json(self, data: list, path: str) -> None:
        """ Абстрактный метод сохранения вакансий в файле """

        pass


class JSONSaver(AbstractJSONSaver):
    """ Класс для сохранения вакансий"""

    def save_to_json(self, data: list, path: str) -> None:
        """ Метод сохранения вакансий в файле """

        with open(path, 'a+', encoding='utf-8') as file:
            res = []
            for i in data:
                res.append({"name": i.name,
                            "url": i.url,
                            "description": i.description,
                            "salary": i.salary
                            })

            json.dump(res, file, ensure_ascii=False, indent=4)

    @staticmethod
    def del_to_json(path: str) -> None:
        """ Удаление данных из файла vacancy.json """

        with open(path, "w") as file:
            file.truncate()
