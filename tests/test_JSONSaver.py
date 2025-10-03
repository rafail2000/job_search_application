import json
from unittest.mock import mock_open, patch

import pytest

from src.JSONSaver import JSONSaver
from src.vacancy import Vacancy


class TestJSONSaver:
    """Тесты для класса JSONSaver"""

    @pytest.fixture
    def sample_vacancies(self):
        """Фикстура с тестовыми вакансиями"""
        return [
            Vacancy(
                name="Python Developer",
                url="https://hh.ru/vacancy/1",
                description="Разработка на Python",
                salary={"from": 100000}
            ),
            Vacancy(
                name="Data Scientist",
                url="https://hh.ru/vacancy/2",
                description="Анализ данных",
                salary={"from": 150000}
            )
        ]

    @patch("builtins.open", new_callable=mock_open)
    def test_save_to_json_success(self, mock_file, sample_vacancies):
        """Тест успешного сохранения вакансий в JSON"""

        # Вызываем тестируемый метод
        JSONSaver.save_to_json(sample_vacancies, "test_vacancies.json")

        # Проверяем что файл был открыт для записи
        mock_file.assert_called_once_with("test_vacancies.json", "w", encoding="utf-8")

        # Получаем ВСЕ данные которые были записаны в файл
        write_calls = mock_file().write.call_args_list
        all_written_data = "".join(call[0][0] for call in write_calls)

        # Декодируем JSON
        parsed_data = json.loads(all_written_data)

        # Проверяем структуру данных
        assert len(parsed_data) == 2
        assert parsed_data[0]["name"] == "Python Developer"
        assert parsed_data[0]["salary"] == 100000
        assert parsed_data[1]["name"] == "Data Scientist"
        assert parsed_data[1]["url"] == "https://hh.ru/vacancy/2"
