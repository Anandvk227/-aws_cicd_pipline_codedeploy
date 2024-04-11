# testCases/test_login.py

import pytest
from openpyxl.reader.excel import load_workbook
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from GenericLib.BaseClass import BaseClass

class TestLogin:
    baseURL = ReadConfig.getApplicationURL()

    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active
    username = worksheet["A2"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger=LogGen.loggen()

    # @pytest.mark.order(4)
    @pytest.mark.run(order=4)
    @pytest.mark.regression
    def test_homePageTitle(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started Home page title test****")
        act_title = driver.title

        if act_title == "InLynk - Business Digital Eco System":
            self.logger.info("****Home page title test passed****")
            assert True
        else:
            self.logger.error("****Home page title test failed****")
            driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            assert False

    # @pytest.mark.order(5)
    @pytest.mark.run(order=5)
    @pytest.mark.regression
    def test_login_inValid_Password(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started invalid Password Login Test****")
        self.logger.info("**** TS_01  TC_03 Started invalid Password Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword("InLINK@!@#$")
        lp.clickLogin()

        act_Text = lp.IncorrectLoginText()

        if act_Text == "Incorrect username or password.":
            assert True
            self.logger.info("********* invalid Login password Test is Passed ***********")

        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_login_inValid_Password.png")
            self.logger.error("********* invalid Login password Test is Failed ***********")
            assert False

    # @pytest.mark.order(6)
    @pytest.mark.run(order=6)
    @pytest.mark.regression
    def test_login_inValid_Username(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started invalid Username Login Test****")
        self.logger.info("***** TS_1  TC_04	 verify the login page with invalid user name*****")
        lp = LoginPage(driver)
        lp.setUserName("sohel@gmailxyz.com")
        lp.setPassword(self.password)
        lp.clickLogin()

        act_Text = lp.IncorrectLoginText()

        if act_Text == "Incorrect username or password.":
            assert True
            self.logger.info("********* invalid Login Username Test is Passed ***********")

        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_login_inValid_Username.png")
            self.logger.error("********* invalid Login Username Test is Failed ***********")
            assert False

    # @pytest.mark.order(3)
    @pytest.mark.run(order=3)
    @pytest.mark.regression
    @pytest.mark.test
    def test_login_Valid_UsernamePassword(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started Login Test****")
        self.logger.info("****TS_1 TC_01 Verify that a registered user can successfully log in with valid credentials.****")
        lp = LoginPage(driver)
        self.logger.info("Entering SuperAdmin Credentials for login Username:" + self.username + " and Password:" + self.password)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        # lp.clickcreatePost()
        # act_Text = lp.newsFeedText()

        # if act_Text == "Create News Feed":
        #     assert True
        #     self.logger.info("********* Login Test is Passed ***********")

        # else:
        #     driver.save_screenshot(".\\Screenshots\\" + "test_login_Valid_UsernamePassword.png")
        #     self.logger.error("********* Login Test is Failed ***********")
        #     assert False

        # element = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[@class='flexAutoRow alignCntr pdngHXS']"))
        # )
        # element.click()
