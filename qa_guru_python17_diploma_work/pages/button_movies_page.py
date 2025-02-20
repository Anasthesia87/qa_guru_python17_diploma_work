from selene import browser
from selene_in_action_py13.conditions import match


class MoviesPage:
    def __init__(self):
        self.button_movies = browser.element('[data-testid="movies_button"]')

    def open(self):
        browser.open("")

    def click_button_movies(self):
        self.button_movies.click()

    def check_button_movies_page_title(self):
        browser.element('.CatalogRedesigned_page_wrapper__uuM_W').should(match.text('Фильмы - смотреть онлайн'))
