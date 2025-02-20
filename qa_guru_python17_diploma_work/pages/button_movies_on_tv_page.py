from time import sleep

from selene import browser
from selene_in_action_py13.conditions import match

class MoviesOnTvPage:
    def __init__(self):
        self.button_movies_on_tv = browser.element('[data-testid="archive_button"]')

    def open(self):
        browser.open("")

    def click_button_movies_on_tv(self):
        sleep(10)
        self.button_movies_on_tv.click()

    def check_movies_on_tv_page_title(self):
        browser.element('.TvArchive_container___H8vS').should(match.text('Кино на ТВ в записи'))