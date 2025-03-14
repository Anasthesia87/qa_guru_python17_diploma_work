import allure
from qa_guru_python17_diploma_work.utils.api_helper import api_request
from jsonschema import validate
from qa_guru_python17_diploma_work.schemas.schemas import tv_channels_schema


@allure.title("Checking tv channels")
def test_tv_channels_api(base_api_url):
    endpoint = "/multiplex/tv"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5",
              "tz": "3",
              }

    response = api_request(base_api_url, endpoint, "GET", params=params)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('title = Телеканалы'):
        assert response.json()["title"] == "Телеканалы"
    with allure.step('Validate response schema'):
        validate(response.json(), tv_channels_schema)
