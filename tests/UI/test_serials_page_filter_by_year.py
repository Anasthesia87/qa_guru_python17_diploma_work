import allure
from qa_guru_python17_diploma_work.pages.button_serials_page import SerialsPage


@allure.title("Checking filter by year")
def test_serials_page_title_filter_by_year():
    with allure.step('Open main page'):
        serials_page = SerialsPage()
        serials_page.open()

    with allure.step('Click button serials'):
        serials_page.click_button_serials()

    with allure.step('Click button year'):
        serials_page.click_button_year()

    with allure.step('Select year'):
        serials_page.select_year()

    with allure.step('Verify result search with filter by year'):
        serials_page.check_serials_page_title_with_filter_by_year()
