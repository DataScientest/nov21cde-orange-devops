import requests

API_URL = "http://127.0.0.1:8000"


def test_get_index():
    response = requests.get(
        url=f"{API_URL}/"
        # url="{}/".format(API_URL)
    )

    assert response.status_code == 200, response.content


def test_get_mon_endpoint():
    response = requests.get(
        url=f"{API_URL}/mon_endpoint",
        params={"nombre_entier": 24}
        # url="{}/".format(API_URL)
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert data["un_nombre"] == 24


def test_post_mon_premier_post():
    response = requests.post(
        url=f"{API_URL}/mon_premier_post",

        # url="{}/".format(API_URL)
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert "hello" in data
    assert data["hello"] == "world"


def test_get_health():
    response = requests.get(
        url=f"{API_URL}/health",

        # url="{}/".format(API_URL)
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert "status" in data
    assert data["status"] == 1


def test_post_index():
    response = requests.post(
        url=f"{API_URL}/",

        # url="{}/".format(API_URL)
    )

    assert response.status_code == 200, response.content
    data = response.json()

    assert "status" in data
    assert data["status"] == 1
