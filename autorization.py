from selenium.webdriver.common.by import By

class Autorization:

    def __init__(self, driver):
        self.driver = driver

    def input_username(self, value_username):
        username = self.driver.find_element(By.CSS_SELECTOR, "#username")
        username.clear()
        username.send_keys(value_username)

    def input_password(self, value_password):
        password = self.driver.find_element(By.CSS_SELECTOR, "#password")
        password.clear()
        password.send_keys(value_password)

    def send_form(self):
        send_button = self.driver.find_element(By.CSS_SELECTOR, "button")
        send_button.click()

    def check_authorization(self):
        result = self.driver.find_element(By.CSS_SELECTOR, "#flash").get_attribute("class")
        return result == "flash success"


