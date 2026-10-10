import requests

import pytest

import allure

@pytest.fixture
def base_url():
    return "https://postman-echo.com"

@allure.title("Проверка GET-запроса с query-параметрами")
@allure.description("Тест проверяет возвращение статус-кода 200 и корректность переданного текста")
def test_get_request(base_url):
    with allure.step("Формирование адреса URL и параметров запроса"):
        url = f"{base_url}/get"
        payload = {"text": "hello"}
    with allure.step("Отправка GET-запроса к API и получение ответа"):
        response = requests.get(url, params=payload)
        response_json = response.json()
    with allure.step("Проверка соответствия статус-кода и тела ответа"):
        assert response.status_code == 200
        assert response_json["args"]["text"] == "hello"

@allure.title("Проверка POST-запроса с передачей тела в формате JSON")
@allure.description("Тест проверяет отправку данных в JSON и получение успешного ответа со статус-кодом 200")
def test_post(base_url):
    with allure.step("Формирование адреса URL и параметров запроса"):
        url = f"{base_url}/post"
        payload = {"text": "hello"}
    with allure.step("Отправка POST-запроса к API и получение ответа"):
        response = requests.post(url, json=payload)
        response_json = response.json()
    with allure.step("Проверка соответствия статус-кода и тела ответа"):
        assert response.status_code == 200
        assert response_json["json"]["text"] == "hello"

@allure.title("Проверка POST-запроса с отправкой данных в формате веб-формы")
@allure.description("Тест проверяет отправку текстовой формы и получение успешного ответа со статус-кодом")
def test_post_form(base_url):
    with allure.step("Формирование адреса URL и параметров запроса"):
        url = f"{base_url}/post"
        payload = {"text": "hello"}
    with allure.step("Отправка POST-запроса к API и получение ответа"):
        response = requests.post(url, data=payload)
        response_json = response.json()
    with allure.step("Проверка соответствия статус-кода и тела ответа"):
        assert response.status_code == 200
        assert response_json["form"]["text"] == "hello"


@allure.title("Проверка PUT-запроса для обновления данных в формате веб-формы")
@allure.description("Тест проверяет обновление данных и получение успешного ответа со статусом-кодом")
def test_put_form(base_url):
    with allure.step("Формирование адреса URL и параметров запроса"):
        url = f"{base_url}/put"
        payload = {"text": "hello"}
    with allure.step("Отправка PUT-запроса к API и получение ответа"):
        response = requests.put(url, data=payload)
        response_json = response.json()
    with allure.step("Проверка соответствия статус-кода и тела ответа"):
        assert response.status_code == 200
        assert response_json["form"]["text"] == "hello"

@allure.title("Проверка DELETE-запроса без передачи тела (удаление ресурса)")
@allure.description("Тест проверяет удаление данных и получение успешного ответа со статусом-кодом")
def test_delete_request(base_url):
    with allure.step("Формирование адреса URL"):
        url = f"{base_url}/delete"
    with allure.step("Отправка DELETE-запроса к API и получение ответа"):
        response = requests.delete(url)
        response_json = response.json()
    with allure.step("Проверка соответствия статус-кода и тела ответа"):
        assert response.status_code == 200