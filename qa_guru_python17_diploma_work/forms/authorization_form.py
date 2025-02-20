from selene import browser

class AuthorizationForm:
    def __init__(self):
        self.free_period_button = browser.element('.Button_text__CEKtw')
        self.telephone_number = browser.element('#login')
        self.continue_button = browser.element('.Button_text__CEKtw')
        self.forgot_password_button = browser.element('.GhostButton_text__BsqQ6')

    def open(self):
        browser.open("")

    def click_free_period_button(self):
        self.free_period_button.click()

    def select_telephone_number_for_authorization(self):
        browser.element('.LoginTypeToggle_toggleContainer__eCQyp > button:nth-child(3)').click()

    def type_telephone_number(self, value):
        self.telephone_number.type(value)

    def get_password(self):
        self.forgot_password_button.click()
