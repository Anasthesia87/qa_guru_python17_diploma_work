from qa_guru_python17_diploma_work.pages.button_movies_page import MoviesPage
import allure


@allure.title("Checking button movies")
def test_movies_button():
    with allure.step('Open main page'):
        movies_page = MoviesPage()
        movies_page.open()

    with allure.step('Click button movies'):
        movies_page.click_button_movies()

    with allure.step('Check movies page title'):
        movies_page.check_button_movies_page_title()
