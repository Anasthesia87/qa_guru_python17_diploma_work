from selene import browser
from selene_in_action_py13.conditions import match

class SerialsPage:
    def __init__(self):
        self.button_serials = browser.element('[data-testid="series_button"]')
        self.button_genre = browser.element('[data-testid=genre_dropdown_default] > div > div')
        self.genre_checkbox = browser.element('#select-genre-bio-0')
        self.button_country = browser.element('[data-testid=country_dropdown_default] > div > div')
        self.country_checkbox = browser.element('#select-country-AU-0')
        self.button_year = browser.element('[data-testid=year_dropdown_default] > div > div')
        self.year_checkbox = browser.element('#select-year-2025-0')

    def open(self):
        browser.open("")

        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def click_button_serials(self):
        self.button_serials.click()

    def check_serials_page_title(self):
        browser.element('.CatalogRedesigned_page_wrapper__uuM_W').should(match.text('Сериалы - смотреть онлайн'))

    def click_button_genre(self):
        self.button_genre.click()

    def select_genre(self):
        self.genre_checkbox.click()

    def check_serials_page_title_with_filter_by_genre(self):
        browser.element('.CatalogRedesigned_page_wrapper__uuM_W').should(match.text('Сериалы: биография - смотреть онлайн'))

    def click_button_country(self):
        self.button_country.click()

    def select_country(self):
        self.country_checkbox.click()

    def check_serials_page_title_with_filter_by_country(self):
        browser.element('.CatalogRedesigned_page_wrapper__uuM_W').should(match.text('Сериалы - Австралия смотреть онлайн'))

    def click_button_year(self):
        self.button_year.click()

    def select_year(self):
        self.year_checkbox.click()

    def check_serials_page_title_with_filter_by_year(self):
        browser.element('.CatalogRedesigned_page_wrapper__uuM_W').should(match.text('Сериалы: 2025 года - смотреть онлайн'))

