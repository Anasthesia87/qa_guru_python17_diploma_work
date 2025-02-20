import allure
from qa_guru_python17_diploma_work.utils.api_helper import api_request
from jsonschema import validate
from schemas import serial_description_schema


@allure.title("Checking serial_description")
def test_serial_description_api(base_api_url):
    endpoint = "/web/watch/zhitzhizn"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5",
              "locale": "ru",
              "content_lang": "ru"
              }

    response = api_request(base_api_url, endpoint, "GET", params=params)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('title = Трейлер 1 сезона'):
        assert response.json()["title"] == "Трейлер 1 сезона"
    with allure.step('Validate description'):
        assert response.json()[
                   "description"] == "Аня знает, как нужно жить. Но отношения с манипулятором лишают уверенности и свободы. Как не дать абьюзеру затушить внутренний огонь?"
    with allure.step('Validate response schema'):
        validate(response.json(), serial_description_schema)
