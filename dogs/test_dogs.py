import pytest
import requests
import json
from jsonschema import validate


def test_res_200(default_url):
    """Проверка кода ответа и схемы json"""
    response = requests.get(f"{default_url}/breeds/list/all", verify=False)
    # verify=False иначе падает с ошибкой проверки сертов
    assert response
    json_schema = {
        "type": "object",
        "properties": {
            "message": {"type": "object"},
            "status": {"type": "string"},
        },
        "required": ["message", "status"]
    }
    validate(instance=response.json(), schema=json_schema)  # Способ проверки схемы json через validate "jsonchema"


@pytest.mark.parametrize("url_num", [1, 4, 11, 26, 42, 50, ])
def test_list_of_dogs(url_num, default_url, pic_url):
    """ Проверка количества фото собак в json с тем, что указано в url"""
    response = requests.get(f"{default_url}/{pic_url}/{url_num}", verify=False)  # f-строка для формирования url
    assert len(response.json().get("message")) == url_num
# Сравниваем количество файлов в json, в "message" с указанным в url, на 51 падает, так как лимит 50


@pytest.mark.parametrize('sub_breeds', ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker', ])
def test_pod(default_url, sub_breeds):
    """Проверка породы переданной в url и полученной в json"""
    response = requests.get(f"{default_url}/breed/hound/{sub_breeds}/images/random", verify=False)
    parsing_value = response.json()
    assert sub_breeds in json.dumps(parsing_value)


def test_breed_json(default_url, list_of_hound):
    """Проверяем что все переданные изображения в json относятся к хаундам"""
    response = requests.get(f"{default_url}/breed/hound/images", verify=False)
    parsed_list = json.dumps(response.json())
    count_hound = parsed_list.count(list_of_hound)
    assert len(response.json().get("message")) == count_hound


def test_image_list(default_url, pic_url):
    """ Проверяем что на 404 ошибку будет корректный ответ"""
    response = requests.get(f"{default_url}//{pic_url}", verify=False)
    assert response.status_code == 404
