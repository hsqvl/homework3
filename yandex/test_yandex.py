import pytest
import requests



def test_yandex_200(default_yandex_url):
    """По умолчанию проверяется яндекс, но можно подставить любой url"""
    response = requests.get(default_yandex_url, verify=False)
    assert response
