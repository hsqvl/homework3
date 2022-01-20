import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request ya url"
    )


@pytest.fixture()
def default_yandex_url(request):
    return request.config.getoption("--url")
