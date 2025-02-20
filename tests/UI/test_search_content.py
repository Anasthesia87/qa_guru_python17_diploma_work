from qa_guru_python17_diploma_work.forms.search_content_form import SearchContentForm
import allure


@allure.title("Checking search content movie")
def test_search_content_film():
    with allure.step('Open main page'):
        search_content_form = SearchContentForm()
    search_content_form.open()

    with allure.step('Type search movie'):
        search_content_form.type_search_text('Жить жизнь')

    with allure.step('Verify search movie results'):
        search_content_form.verify_search_movie_results()


@allure.title("Checking search content person")
def test_search_content_person():
    with allure.step('Open main page'):
        search_content_form = SearchContentForm()
    search_content_form.open()

    with allure.step('Type search person'):
        search_content_form.type_search_text('Любовь Аксенова')

    with allure.step('Verify search person results'):
        search_content_form.verify_search_person_results()


@allure.title("Checking search content tv_channel")
def test_search_content_tv_channel():
    with allure.step('Open main page'):
        search_content_form = SearchContentForm()
    search_content_form.open()

    with allure.step('Type search tv channel'):
        search_content_form.type_search_text('нтв')

    with allure.step('Verify search tv channel results'):
        search_content_form.verify_search_tv_channel_results()
