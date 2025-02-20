import allure
from qa_guru_python17_diploma_work.utils.api_helper import api_request


@allure.title("Checking switch language in English")
def test_switch_language_api(base_api_url):
    endpoint = "/document/terms_of_use/en"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5"}

    response = api_request(base_api_url, endpoint, "GET", params=params)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('Validate headers'):
        assert response.headers['Content-Type'] == 'text/html; charset=UTF-8'
    with allure.step('Validate language'):
        assert 'START user agreement' in response.text
