import pytest
import requests


@pytest.mark.parametrize("url_id", [1, 3, 6, 8, 10, ])
def test_url_200(default_placeholder_url, url_id):
    """Проверка кода ответа и наличия переданного ID в json файле"""
    response = requests.get(f"{default_placeholder_url}/users/{url_id}/albums", verify=False)
    assert response
    assert response.json()[0]["userId"] == url_id


@pytest.mark.parametrize("url_id", [99999, 0, -10, 'something', [123, "something", ]])
def test_url_404(default_placeholder_url, url_id):
    """Проверка наличия корректной реакции на некорректное значение"""
    response = requests.get(f"{default_placeholder_url}/posts{url_id}", verify=False)
    assert response.status_code == 404
    assert response.json() == {}


def test_photos_len(default_placeholder_url):
    """Проверка количества фотографий в альбоме по умолчанию"""
    response = requests.get(f"{default_placeholder_url}/albums/2/photos", verify=False)
    assert response
    assert len(response.json()) == 50


def test_del_smth(default_placeholder_url):
    """Проверка работы команды DELETE, должен вернуться пустой json файл"""
    response = requests.delete(f'{default_placeholder_url}/posts/1')
    assert response
    assert len(response.json()) == 0
