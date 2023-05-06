from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import unittest


class TestFacebookLogin(unittest.TestCase):
    def setUp(self):
        driver_service = Service(r'C:\Users\Iwerson\Desktop\geckodriver')
        self.driver = Firefox(service=driver_service)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.facebook.com/")
        email_field = driver.find_element(By.NAME, "email")
        email_field.send_keys("myemail@gmail.com")
        password_field = driver.find_element(By.NAME, "pass")
        password_field.send_keys("mypassword")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        assert "Facebook" in driver.title


if __name__ == "__main__":
    unittest.main()

