import allure
from qa_guru_python17_diploma_work.pages.where_to_watch_page import WhereToWatch


@allure.title("Checking where to watch page")
def test_where_to_watch_page():
    with allure.step('Open page'):
        where_to_watch_page = WhereToWatch()
        where_to_watch_page.open()

    with allure.step('Check where to watch page title'):
        where_to_watch_page.check_where_to_watch_page_title()
