from selene import browser
from selene_in_action_py13.conditions import match


class WhereToWatch:

    def open(self):
        browser.open("ways-to-watch")

    def check_where_to_watch_page_title(self):
        browser.all('.WaysToWatch_ways-to-watch__device-title__HdDMl').should(
            match.texts('Телевизоры', 'Приставки', 'Телефоны и планшеты'))
