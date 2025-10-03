from config import PATH_TO_JSON
from src.JSONSaver import JSONSaver
from src.api import HeadHunterAPI
from src.utils import add_vacancy_in_lst, get_sort_vacancy, filter_vacancies, get_vacancies_by_salary, get_top_vacancies

hh = HeadHunterAPI()
js = JSONSaver()


def user_interaction():
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий через пробел: ").split()
    salary_range = input("Введите диапазон зарплат через пробел: ").split()

    hh.load_vacancies(search_query)
    vacancies_list = add_vacancy_in_lst(hh.vacancies)
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = get_sort_vacancy(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    print("Найденные результаты")
    for i in top_vacancies:
        print(f"{i.name}\n{i.url}\n{i.description}\n{i.salary}\n")

    del_command = input("Наберите команду 'del' если хотите удалить предыдущие результаты поиска: ")
    save_or_add = input("Наберите команду 'add' если вы хотите добавить результат к первичным данным, ничего если сохранить только эти данные: ")

    if del_command.lower() == "del":
        js.del_to_json(PATH_TO_JSON)

    if save_or_add.lower() == "add":
        js.add_to_json(top_vacancies, PATH_TO_JSON)
    else:
        js.save_to_json(top_vacancies, PATH_TO_JSON)


if __name__ == "__main__":
    user_interaction()
