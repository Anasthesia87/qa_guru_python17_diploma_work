from qa_guru_python17_diploma_work.pages.button_cartoons_page import CartoonsPage
import allure


@allure.title("Checking button cartoons")
def test_cartoons_button():
    with allure.step('Open main page'):
        cartoons_page = CartoonsPage()
        cartoons_page.open()

    with allure.step('Click button cartoons'):
        cartoons_page.click_button_cartoons()

    with allure.step('Check cartoons page title'):
        cartoons_page.check_cartoons_page_title()
