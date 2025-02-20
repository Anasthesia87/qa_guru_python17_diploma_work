from selene import browser
from selene_in_action_py13.conditions import match

class CartoonsPage:
    def __init__(self):
        self.button_cartoons = browser.element('[data-testid="animation_button"]')

    def open(self):
        browser.open("")

    def click_button_cartoons(self):
        self.button_cartoons.click()

    def check_cartoons_page_title(self):
        browser.element('.CatalogRedesigned_page_wrapper__uuM_W').should(match.text('Мультфильмы - смотреть онлайн'))