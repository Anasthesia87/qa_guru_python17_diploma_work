from selene_in_action_py13.conditions import match
from selene import browser
from qa_guru_python17_diploma_work.forms.authorization_form import AuthorizationForm
import allure


@allure.title("Checking authorization form")
def test_authorization_by_telephone_number_forgot_password():
    with allure.step('Open main page'):
        authorization_form = AuthorizationForm()
        authorization_form.open()

    with allure.step('Click free period button'):
        authorization_form.click_free_period_button()

    with allure.step('Select authorization by telephone number'):
        authorization_form.select_telephone_number_for_authorization()

    with allure.step('Type telephone number'):
        authorization_form.type_telephone_number('89215574647')

    with allure.step('Click continue button'):
        authorization_form.continue_button.click()

    with allure.step('Click forgot password button'):
        authorization_form.get_password()

    with allure.step('Click continue button'):
        authorization_form.continue_button.click()

    with allure.step('Check text message'):
        browser.element('.AuthSteps_container__UAEzf').should(match.text('Вход в аккаунт через телефон'))
