import pytest


@pytest.fixture()
def default_url():
    return "https://dog.ceo/api"


@pytest.fixture()
def pic_url():
    return "breeds/image/random"


@pytest.fixture()
def list_of_hound():
    return "https://images.dog.ceo/breeds/hound"
