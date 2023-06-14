import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pageObject.LoginPage import Login
import time


class Test_Url:

      def test_url01(self,setup):
          self.driver=setup
          time.sleep(4)
          if self.driver.title=="OrangeHRM":
              self.driver.save_screenshot("C:\\Users\\Suraj V. Chaudhari\\Desktop\\Orange\\Screenshot\\test_url01_pass.png")
              assert True
          else:
              self.driver.save_screenshot("C:\\Users\\Suraj V. Chaudhari\\Desktop\\Orange\\Screenshot\\test_urlo1.fail.png")
              assert False

      def test_login02(self,setup):
          self.driver=setup
          self.L=Login(self.driver)
          time.sleep(3)
          self.L.get_username("Admin")
          self.L.get_password("admin123")
          self.L.click_Login()

          try:
              time.sleep(2)
              self.driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']")
              login=True
          except NoSuchElementException:
              login=False

          if login==True:
              self.driver.save_screenshot("C:\\Users\\Suraj V. Chaudhari\\Desktop\\Orange\\Screenshot\\test_logino2.pass.png")
              self.L.click_Menu()
              self.L.click_login()
              assert True
          else:
              self.driver.save_screenshot(
                  "C:\\Users\\Suraj V. Chaudhari\\Desktop\\Orange\\Screenshot\\test_logino2.fail.png")
              assert False





