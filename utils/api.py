from utils.httpmethods import HttpMethods
from logger import Logger

BASE_URL = "https://swapi.dev/api/people/4/"    # Базовый URL страницы ДВ

"""Класс для работа с API SWAPI"""
class Swapi:
    """Метод запроса фильмов в который снимается ДВ"""
    @staticmethod
    def get_darth_vader_films_list():
        result_get = HttpMethods.get(BASE_URL)
        json_data = result_get.json()
        film_list = json_data.get('films')
        return film_list, result_get        # в ответе получаем список URL фильмов с ДВ, ответ запроса ГЕТ

    """Метод запроса URL адресов героев фильмов в который снимается ДВ"""
    @staticmethod
    def get_films_list(film_list):
        characters_list = []    # Создаем пустой список куда будут записываться адреса страниц
        for film in film_list:  # перебором подставляем адреса страниц фильмов и парсим адреса страниц героев
            result_get = HttpMethods.get(film)
            json_data = result_get.json()
            chars_list = json_data.get('characters')    # парсим адерса страниц героев
            characters_list += chars_list       # добавляем в список
        characters_set = set(characters_list)   # с помощью множества отсекам дубли
        char_list = list(characters_set)        # кидаем обратно в список (методом броб и ошибок в следующем методе список отрабатывает лучше, чем множество )
        return char_list, result_get            # возвращаем список адресов стараниц героев, ответ запроса ГЕТ

    """Метод получения имен героев в который снимается ДВ"""
    @staticmethod
    def get_characters_name(char_list):
        characters_list = []    # Создаем пустой список куда будут имена геров
        for char in char_list:
            result_get = HttpMethods.get(char)      # через цикл кидаем гет запрос на адерс страница героя, парсим имя
            json_data = result_get.json()
            chars_list = json_data.get('name')      # парсим имя
            characters_list.append(chars_list)
        return characters_list                      # возвращаем список имен


film, _ = Swapi.get_darth_vader_films_list()
list_ch, _ = Swapi.get_films_list(film)
name = Swapi.get_characters_name(list_ch)

print(film)
print(list_ch)
print(name)

for n in name:
    Logger.write_name_to_file(n)        # проходим по списку имен циклом записываем в файл, каждое имя с новой строки
print(len(name))



