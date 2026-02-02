import requests


def test_echo_get_status_code():
    response = requests.get("https://postman-echo.com/get")
    assert response.status_code == 200


def test_echo_get_args():
    response = requests.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2").json()
    assert response['args']['foo1'] == 'bar1'
    assert response['args']['foo2'] == 'bar2'


def test_echo_post_status_code():
    response = requests.post("https://postman-echo.com/post")
    assert response.status_code == 200


def test_echo_post_text():
    response = requests.post("https://postman-echo.com/post", json={'test': 'example'}).json()
    assert response['data']['test'] == 'example'


def test_echo_put():
    text = 'This is expected to be sent back as part of response body'
    response = requests.put("https://postman-echo.com/put", json=text).json()
    assert response['data'] == f'"{text}"'


def test_echo_put_empty_status_code():
    response = requests.post("https://postman-echo.com/put")
    assert response.status_code != 404
