from selene_in_action_py13.conditions import match
from selene import browser
from qa_guru_python17_diploma_work.forms.registration_form import RegistrationForm
import allure


@allure.title("Checking registration by telephone number")
def test_registration_by_telephone_number():
    with allure.step('Open main page'):
        registration_form = RegistrationForm()
    registration_form.open()

    with allure.step('Click free period button'):
        registration_form.click_free_period_button()

    with allure.step('Select registration with telephone number'):
        registration_form.select_telephone_number_for_registration()

    with allure.step('Type telephone number'):
        registration_form.type_telephone_number('89119119195')

    with allure.step('Click continue button'):
        registration_form.continue_button.click()

    with allure.step('Type password'):
        registration_form.type_password('123456')

    with allure.step('Click continue button'):
        registration_form.continue_button.click()

    with allure.step('Check text message'):
        browser.element('.AuthSteps_container__UAEzf').should(match.text('Введите код из СМС,'))
