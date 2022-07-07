import requests


def test_ping():
    headers = {'User-Agent':'openmedia'}
    with requests.head('https://yookassa.ru/', headers=headers, timeout=5) as response:
        assert response.status_code == 200


# TODO
class TestYookassa:
    pass
