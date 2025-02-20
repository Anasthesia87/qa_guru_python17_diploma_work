from selene import browser
from selene_in_action_py13.conditions import match

class NewContentPage:
    def __init__(self):
        self.button_new_content = browser.element('[data-testid="new_button"]')

    def open(self):
        browser.open("")

    def click_button_new_content(self):
        self.button_new_content.click()

    def check_new_content_page_title(self):
        browser.element('.Genres_new_wrapper__lzxBE').should(match.text('Новинки фильмов, мультфильмов и сериалов смотреть онлайн'))




