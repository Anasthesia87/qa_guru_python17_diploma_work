import allure
from qa_guru_python17_diploma_work.pages.button_new_content_page import NewContentPage


@allure.title("Checking button new content")
def test_new_content_button():
    with allure.step('Open main page'):
        new_content_page = NewContentPage()
        new_content_page.open()

    with allure.step('Click button new content'):
        new_content_page.click_button_new_content()

    with allure.step('Check new content page title'):
        new_content_page.check_new_content_page_title()
