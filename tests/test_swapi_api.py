from utils.api import Swapi
from utils.cheking import Checking


"""Класс тестирования работы с API SWAPI"""
class TestGetSwapi:
    film_list = []
    characters_list = []

    """Метод тестирования запроса базовой URL"""
    def test_get_film_with_DW(self):

        print("\n Метод GET, получения списка фильмов с Дартом Вейдером")
        result_get_film_list, result_get = Swapi.get_darth_vader_films_list()
        Checking.check_status_code(result_get, 200)     # Тест кода ответа
        Checking.check_json_token_value(result_get, 'name', 'Darth Vader')      # Убеждаемся что мы на странице ДВ
        assert len(result_get_film_list) > 0, f"Список фильмов пустой"          # Проверям полученный список на длину
        TestGetSwapi.film_list = result_get_film_list
        print(f"Дарт Вейдер снимался в {len(result_get_film_list)} фильмах")

    """Метод тестирования списка URL адресов персонажей снявшихся с Дартом Вейдером"""
    def test_get_characters_list(self):

        print("\n Метод GET, получения списка URL адресов персонажей снявшихся с Дартом Вейдером")
        result_get_list_URL_chars, result_get = Swapi.get_films_list(TestGetSwapi.film_list)
        Checking.check_status_code(result_get, 200)     # Тест кода ответа
        Checking.check_json_token(result_get, 'characters')         # Убеждаемся обязательного поля списка героев на станице фильма
        assert len(result_get_list_URL_chars) > 0, f"Список персонажей пустой"      # Проверям полученный список на длину
        print(f"C Дарт Вейдером снимались  {len(result_get_list_URL_chars)} героев")
        TestGetSwapi.characters_list = result_get_list_URL_chars

    """Метод тестирования получения списка имен персонажей снявшихся с Дартом Вейдером"""
    def test_get_name_from_characters_list(self):

        print("\n Метод GET, получения списка имен персонажей снявшихся с Дартом Вейдером")
        print(len(TestGetSwapi.characters_list))
        result_get_name = Swapi.get_characters_name(TestGetSwapi.characters_list)
        assert len(result_get_name) > 0     # Проверям полученный список на длину
        print(f"В списке {len(result_get_name)} имен")





