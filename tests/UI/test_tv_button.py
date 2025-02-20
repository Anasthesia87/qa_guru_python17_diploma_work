from qa_guru_python17_diploma_work.pages.button_tv_page import TvPage
import allure


@allure.title("Checking button tv")
def test_tv_button():
    with allure.step('Open main page'):
        tv_page = TvPage()
        tv_page.open()

    with allure.step('Click button tv'):
        tv_page.click_button_tv()

    with allure.step('Check tv page title'):
        tv_page.check_tv_page_title()
