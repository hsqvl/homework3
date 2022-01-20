import pytest
import requests
import json
from jsonschema import validate


def test_schema_breweries(default_ob_url):
    """Проверка кода ответа и схемы json"""
    response = requests.get(f"{default_ob_url}/breweries//madtree-brewing-cincinnati", verify=False)
    assert response
    schema = {
        "items": {
            "type": "object"
        }
    }
    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize('page', [5, 15, 25, 35, 50, ])  # на 51 упадел, так как лимит 50
def test_per_page(default_ob_url, page):
    """Проверка переданного значения "page" в Url с количеством полученным в json"""
    response = requests.get(f"{default_ob_url}/breweries?per_page={page}", verify=False)
    assert len(response.json()) == page


@pytest.mark.parametrize('name', ['Dog', 'Bull', 'Mexico', 'West', 'World', ])
def test_autocomplete(default_ob_url, name):
    """Проверка на то, что поиск по названию действительно возвращает нужные заведения.
    Значение "name" должно встречаться в поле name json файла"""
    response = requests.get(f"{default_ob_url}/breweries/autocomplete?query={name}", verify=False)
    parsing_value = response.json()
    assert response
    assert name in json.dumps(parsing_value)


@pytest.mark.parametrize('value', ["San Diego", "Los Angeles", "Moscow", "Chicago", ])
def test_city(default_ob_url, value):
    """Проверка на то, что город переданный в url действительно указан в json файле.
    Присутсвует проверка кода ответа и валидация json схемы"""

    response = requests.get(f"{default_ob_url}/breweries?by_city={value}", verify=False)
    assert response
    assert response.json()[0]["city"] == value
    schema = {
        "type": "array",
        "items": {
            "type": "object"
        }
    }
    validate(instance=response.json(), schema=schema)
