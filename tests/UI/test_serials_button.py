from qa_guru_python17_diploma_work.pages.button_serials_page import SerialsPage
import allure


@allure.title("Checking button serials")
def test_serials_button():
    with allure.step('Open main page'):
        serials_page = SerialsPage()
    serials_page.open()

    with allure.step('Click button serials'):
        serials_page.click_button_serials()

    with allure.step('Check serials page title'):
        serials_page.check_serials_page_title()
