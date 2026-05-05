import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from autorization import Autorization


class TestAuthorization:

    @pytest.fixture
    def driver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        driver.get("https://the-internet.herokuapp.com/login")
        yield driver
        driver.quit()

    def __send_form(self, driver, value_username, value_password):
        auto = Autorization(driver)
        auto.input_username(value_username)
        auto.input_password(value_password)
        auto.send_form()
        return auto.check_authorization()

    def test_successful_login(self, driver):
        result = self.__send_form(driver, "tomsmith", "SuperSecretPassword!")

        assert result == True

    def test_unsuccessful_login(self, driver):
        result = self.__send_form(driver,"Kate", "123!")

        assert result == False

