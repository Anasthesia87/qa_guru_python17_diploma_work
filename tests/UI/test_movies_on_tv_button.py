import allure
from qa_guru_python17_diploma_work.pages.button_movies_on_tv_page import MoviesOnTvPage


@allure.title("Checking button movies on tv")
def test_movies_on_tv_button():
    with allure.step('Open main page'):
        movies_on_tv_page = MoviesOnTvPage()
        movies_on_tv_page.open()

    with allure.step('Click button movies on tv'):
        movies_on_tv_page.click_button_movies_on_tv()

    with allure.step('Check movies on tv page title'):
        movies_on_tv_page.check_movies_on_tv_page_title()
