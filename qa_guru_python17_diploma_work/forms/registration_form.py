from selene import browser


class RegistrationForm:
    def __init__(self):
        self.free_period_button = browser.element('.Button_text__CEKtw')
        self.telephone_number = browser.element('#login')
        self.continue_button = browser.element('.Button_text__CEKtw')
        self.password = browser.element('#password')

    def open(self):
        browser.open("")

        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    def click_free_period_button(self):
        self.free_period_button.click()

    def select_telephone_number_for_registration(self):
        browser.element('.LoginTypeToggle_toggleContainer__eCQyp > button:nth-child(3)').click()

    def type_telephone_number(self, value):
        self.telephone_number.type(value)

    def type_password(self, value):
        self.password.type(value)
