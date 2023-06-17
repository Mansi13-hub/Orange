#import pytest
#from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Logs.Logger import LogGen
from pageObject.LoginPage import Login
import time
from utilitis.Readconfig import ReadFile

class Test_Url:

      username=ReadFile.getusername()
      password=ReadFile.getpassword()
      log=LogGen.loggen()

      def test_url01(self,setup):
         self.driver=setup
         self.log.info('Opening of browser')
         time.sleep(4)
         if self.driver.title=="OrangeHRM":
             self.log.info('test_url01 is passed')
             self.driver.save_screenshot("C:\\Users\\Suraj V. Chaudhari\\Desktop\\Orange\\Screenshot\\test_url01_pass.png")
             assert True
         else:
             self.driver.save_screenshot("C:\\Users\\Suraj V. Chaudhari\\Desktop\\Orange\\Screenshot\\test_urlo1.fail.png")
             assert False
             self.driver.close()

      def test_login02(self,setup):
          self.driver=setup
          self.log.info('opening browser')
          self.L=Login(self.driver)
          self.log.info('go to url')
          time.sleep(4)
          self.L.get_username(self.username)
          self.log.info('enter username')
          self.L.get_password(self.password)
          self.log.info('enter password')
          self.L.click_Login()
          self.log.info('click on login')

          #try:
          #    time.sleep(2)
          #    self.driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']")
          #    login=True
          #except NoSuchElementException:
          #    login=False

          if self.L.login_status()==True:

              self.log.info('test_login02 is passed')
              self.driver.save_screenshot("C:\\Users\\Suraj V. Chaudhari\\Desktop\\Orange\\Screenshot\\test_logino2.pass.png")
              self.L.click_Menu()
              self.log.info('click on menu')
              self.L.click_login()
              self.log.info('click login')
              assert True

          else:
              self.log.info('test_logino2 is failed')
              self.driver.save_screenshot("C:\\Users\\Suraj V. Chaudhari\\Desktop\\Orange\\Screenshot\\test_logino2.fail.png")
              assert False
              self.driver.close()





