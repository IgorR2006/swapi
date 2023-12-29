import datetime
import os

"""Класс создания лога и записи имен в файл"""
class Logger:
    """Создаем имя файла лога"""
    file_name = f"{os.getcwd()}\\logs\\log_" + str(datetime.datetime.now().strftime('%H-%M-%S_%Y-%m-%d')) + ".log"
    """Создаем имя файла для списка имен"""
    file_name_char = f"{os.getcwd()}\\name_char_" + str(datetime.datetime.now().strftime('%H-%M-%S_%Y-%m-%d')) + ".log"

    """Метод записи лога"""
    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    """Метод записи имем геров в файл"""
    @classmethod
    def write_name_to_file(cls, chars: str):
        with open(cls.file_name_char, 'a', encoding='utf=8') as char:
            char.write(f"{chars}\n")

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Test: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += f"\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)

