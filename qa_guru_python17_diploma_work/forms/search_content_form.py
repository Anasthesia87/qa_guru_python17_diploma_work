from selene import browser
from selene_in_action_py13.conditions import match


class SearchContentForm:
    def __init__(self):
        self.search_form = browser.element('.HeaderSearchV2_header-search__input-text__bKUFA')

    def open(self):
        browser.open("")

        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def type_search_text(self, value):
        self.search_form.type(value).press_enter()

    def verify_search_movie_results(self):
        browser.element('.VideoUnit_title__J_lZy').should(match.text('Жить жизнь'))

    def verify_search_person_results(self):
        browser.element('.Search_search_global_wrapper__xpyTs').should(match.text('Любовь Аксёнова'))

    def verify_search_tv_channel_results(self):
        browser.element('.Search_search_global_wrapper__xpyTs').should(match.text('Телекомпания НТВ'))
