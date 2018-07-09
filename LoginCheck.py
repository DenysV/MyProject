from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/login.html")
        self.assertIn("Login", driver.title)
        username = driver.find_element_by_name("username")
        username.send_keys("Alice")
        password=driver.find_element_by_name("password")
        password.send_keys("Alice12345")
        loginbutton=driver.find_element_by_name("submit")
        loginbutton.click()
        #self.assertTrue(driver.find_element_by_link_text("logout"),"Logout link")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
