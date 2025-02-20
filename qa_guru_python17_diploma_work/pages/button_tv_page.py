from selene import browser
from selene_in_action_py13.conditions import match


class TvPage:
    def __init__(self):
        self.button_tv = browser.element('[data-testid="tv_button"]')

    def open(self):
        browser.open("")

        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def click_button_tv(self):
        self.button_tv.click()

    def check_tv_page_title(self):
        browser.element('.TvSchedule_container__VQpHm').should(match.text('ТВ Каналы Онлайн и Программа Передач'))
