
from selenium.webdriver.common.by import By


class Login:
    Username=(By.NAME,'username')
    Password=(By.NAME,'password')
    Login=(By.XPATH,"//button[normalize-space()='Login']")
    menu=(By.XPATH,"//span[@class='oxd-userdropdown-tab']")
    clogin=(By.XPATH,"//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver = driver

    def get_username(self,Username):
        self.driver.find_element(*Login.Username).send_keys(Username)

    def get_password(self,Password):
        self.driver.find_element(*Login.Password).send_keys(Password)

    def click_Login(self):
        self.driver.find_element(*Login.Login).click()

    def click_Menu(self):
        self.driver.find_element(*Login.menu).click()

    def click_login(self):
        self.driver.find_element(*Login.clogin).click()
