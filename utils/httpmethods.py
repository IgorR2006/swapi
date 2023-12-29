import requests

from logger import Logger

"""Класс создания кастомного медота GET, для подключения логирования запросов"""
class HttpMethods:
    headers = {
        'Content-Type': 'application/json'
    }
    cookie = ""

    @staticmethod
    def get(url):
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        Logger.add_response(result)
        return result
