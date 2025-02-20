import allure
from jsonschema import validate
from schemas import switch_on_kids_mode_schema
from qa_guru_python17_diploma_work.utils.api_helper import api_request


@allure.title("Checking switch on kids mode")
def test_switch_on_kids_mode_api(base_api_url):
    endpoint = "/profile/select"
    params = {"apikey": "a20b12b279f744f2b3c7b5c5400c4eb5"}
    payload = {
        "profile_id": "eddf9ed1-4bee-4e00-ab3e-d4850179b9b1"
    }

    headers = {
        'content-type': 'application/json',
        'Cookie': 'auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
                  '.eyJ1aWQiOiI2N2FjZmVhNjdmMTkyYjUyMTBhNWIyNjYiLCJwaWQiOiJlZGRmOWVkMS00YmVlLTRlMDAtYWIzZS1kNDg1MDE3OWI5YjEiLCJkaWQiOiI1MDNmNzhiYi03MTU3LTRlNmItOTk5Zi1kODQwOTI4OTQ2YjEiLCJhbm9ueW1vdXMiOmZhbHNlLCJmb3Jfa2lkcyI6dHJ1ZSwiYWNjb3VudF90eXBlIjoidmlydHVhbCIsImFjbF9leHBpcmUiOm51bGwsInVwZGF0ZWRfYXQiOjE3Mzk5OTU1ODUsInYiOjN9'
                  '.XBW0kSgoPTwW5hmJ6ba1qarrKtK3fSXXddYbw930c90'
    }
    response = api_request(base_api_url, endpoint, "POST", params=params, json=payload, headers=headers)

    with allure.step('Status code=200'):
        assert response.status_code == 200
    with allure.step('Validate schema'):
        validate(response.json(), switch_on_kids_mode_schema)
    with allure.step('Validate headers'):
        assert response.json()['profile_id'] == 'eddf9ed1-4bee-4e00-ab3e-d4850179b9b1'
