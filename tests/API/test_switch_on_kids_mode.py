import allure
from jsonschema import validate
from qa_guru_python17_diploma_work.schemas.schemas import switch_on_kids_mode_schema
from qa_guru_python17_diploma_work.utils.api_helper import api_request


@allure.title("Checking switch on kids mode")
def test_switch_on_kids_mode_api(base_api_url):
    endpoint = "/profile/select"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5"}
    payload = {
        "profile_id": "66eb0a9d-3afa-4607-acf0-b608597fd6a4"
    }

    headers = {
        'content-type': 'application/json',
        'Cookie': 'auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                  '.eyJ1aWQiOiI2NjE0NGEzY2JiOTliZDNlZjNkMjYwZjUiLCJwaWQiOiI1OTM4Njc2My1hN2FiLTQ4YzUtOWIzYy03YjhmOTI3M'
                  'jA2NTAiLCJkaWQiOiIwZjcyMGVhNC03NDQwLTQxOGMtOTg2Mi1hYWY0MDIzNTY4YWUiLCJhbm9ueW1vdXMiOmZhbHNlLCJmb3J'
                  'fa2lkcyI6ZmFsc2UsImFjY291bnRfdHlwZSI6InJlZ2lzdGVyZWQiLCJhY2xfZXhwaXJlIjpudWxsLCJ1cGRhdGVkX2F0IjoxN'
                  'zEyOTk1MTcwLCJ2IjozfQ.sIZfIJhvyQmVRvpT_xTievBH9VUIBJT5RY6ezVGr6uU'
    }
    response = api_request(base_api_url, endpoint, "POST", params=params, json=payload, headers=headers)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('Validate schema'):
        validate(response.json(), switch_on_kids_mode_schema)
    with allure.step('Validate headers'):
        assert response.json()['profile_id'] == '59386763-a7ab-48c5-9b3c-7b8f92720650'
