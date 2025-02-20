from qa_guru_python17_diploma_work.pages.button_serials_page import SerialsPage
import allure


@allure.title("Checking filter by country")
def test_serials_page_title_filter_by_country():
    with allure.step('Open main page'):
        serials_page = SerialsPage()
        serials_page.open()

    with allure.step('Click button serials'):
        serials_page.click_button_serials()

    with allure.step('Click button country'):
        serials_page.click_button_country()

    with allure.step('Select country'):
        serials_page.select_country()

    with allure.step('Verify result search with filter by country'):
        serials_page.check_serials_page_title_with_filter_by_country()
