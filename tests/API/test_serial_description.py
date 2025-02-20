import allure
from qa_guru_python17_diploma_work.utils.api_helper import api_request
from jsonschema import validate
from qa_guru_python17_diploma_work.schemas.schemas import serial_description_schema


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
    with allure.step('title = Жить жизнь'):
        assert response.json()["title"] == "Жить жизнь"
    with allure.step('Validate description'):
        assert response.json()[
                   "description"] == "Анна Богинская не понаслышке знает, как манипуляции ломают жизнь. После мучительных отношений, переполненных жестокостью и виртуозной ложью, героиня понимает, что оказалась пешкой в масштабной игре. А правила задают в стенах закрытого клуба, где парней обучают искусству обольщения. Узнает ли девушка больше из откровений загадочной Софии, так удивительно напоминающей ее саму в молодости? В отчаянной попытке уберечь других от своих роковых ошибок Богинская вынуждена столкнуться с призраками прошлого и разобраться, являются ли чувства к Матвею настоящей любовью или их связь — всего лишь болезненная зависимость."
    with allure.step('Validate response schema'):
        validate(response.json(), serial_description_schema)
