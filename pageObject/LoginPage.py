from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    Username=(By.NAME,'username')
    Password=(By.NAME,'password')
    login=(By.XPATH,"//button[normalize-space()='Login']")
    menu=(By.XPATH,"//span[@class='oxd-userdropdown-tab']")
    clogin=(By.XPATH,"//a[normalize-space()='Logout']")


    def __init__(self,driver):
        self.driver = driver
        self.wait=WebDriverWait(driver,10)

    def get_username(self,Username):
        self.wait.until(expected_conditions.presence_of_element_located(self.Username))
        self.driver.find_element(*Login.Username).send_keys(Username)

    def get_password(self,Password):
        self.wait.until(expected_conditions.presence_of_element_located(self.Password))
        self.driver.find_element(*Login.Password).send_keys(Password)

    def click_Login(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.login))
        self.driver.find_element(*Login.login).click()

    def click_Menu(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.menu))
        self.driver.find_element(*Login.menu).click()

    def click_login(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.clogin))
        self.driver.find_element(*Login.clogin).click()

    def login_status(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.menu))
        try:

            self.driver.find_element(*Login.menu)
            return True
        except (NoSuchElementException,TimeoutException) :
            return False
            pass

