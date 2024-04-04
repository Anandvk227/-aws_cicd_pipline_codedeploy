import os

import pytest
from openpyxl.reader.excel import load_workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from pageObjects.productWarranty import productWarranty
from pageObjects.randomGen import randomGen
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_PW():
    baseURL = ReadConfig.getApplicationURL()
    first_name = randomGen.random_first_name()
    file_name = "Files/Free_Test_Data_1MB_PDF.pdf"
    verify_file = "Free_Test_Data_1MB_PDF.pdf"
    file_path = os.path.abspath(os.path.join(os.getcwd(), file_name))
    purchaseDate = "03-04-2024"
    ExpiryDate = "03-04-2026"
    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active
    username = worksheet["A2"].value
    adminUsername = worksheet["D6"].value
    CustomerUsername = worksheet["A4"].value
    companyName = worksheet["C2"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger = LogGen.loggen()

    @pytest.mark.run(order=1)
    # @pytest.mark.test
    def test_RegisterPW_SuperAdmin(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.logger.info("Started Super admin - can able to raise the warranty on behalf of customer.")
        driver.get(self.baseURL)
        prod_id = randomGen.random_Emp_Id()
        prod_id2 = randomGen.random_Emp_Id()
        first_name2 = randomGen.random_first_name()
        first_name3 = randomGen.random_first_name()
        custEmail = randomGen.random_email()
        phoneNumber = randomGen.random_phone_number()
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        pw = productWarranty(driver)
        pw.clickPWfeature()
        pw.clickRegisterButton()
        pw.setProductId(prod_id)
        pw.setprodName(first_name2)
        pw.setserialNumber(prod_id2)
        pw.setpurchaseDate(self.purchaseDate)
        pw.setfile_invoice(self.file_path)
        xpath = "//span[text()='" + self.verify_file + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.is_displayed()
        pw.setcustomerName(first_name3)
        pw.setcustomerEmail(custEmail)
        pw.setcustomerPhone(phoneNumber)
        pw.clickSubmitButton()
        xpath = pw.text_verifyCreate
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Super admin - can able to raise the warranty on behalf of customer == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False
        pw.clickclose_Toast()
        self.logger.info("Started Edit warranty - that is raised by Super admin on behalf of customer")
        self.logger.info("Searching Product ID to edit")
        pw.setsearchField(prod_id)
        xpath = "//span[text()='" + prod_id + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.click()
        pw.clickEditButton()
        self.logger.info("Updating phone Number")
        pw.setcustomerPhone(phoneNumber)
        pw.clickUpdateButton()
        pw.clickConfUpdateButton()
        xpath = pw.text_verifyUpdate
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Edit warranty - that is raised by Super admin on behalf of customer == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False
        pw.clickclose_Toast()
        self.logger.info("Started Delete warranty - that is raised by Super admin on behalf of customer")
        pw.clickDeleteButton()
        pw.clickConfDeleteButton()
        xpath = pw.text_verifyDelete
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Delete warranty - that is raised by Super admin on behalf of customer == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False

    @pytest.mark.run(order=2)
    # @pytest.mark.test
    def test_RegisterPW_SuperAdmin_Reject(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.logger.info(" Started Super admin - can able to raise the warranty on behalf of customer.")
        driver.get(self.baseURL)
        prod_id = randomGen.random_Emp_Id()
        prod_id2 = randomGen.random_Emp_Id()
        first_name2 = randomGen.random_first_name()
        first_name3 = randomGen.random_first_name()
        custEmail = randomGen.random_email()
        phoneNumber = randomGen.random_phone_number()
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        pw = productWarranty(driver)
        pw.clickPWfeature()
        pw.clickRegisterButton()
        pw.setProductId(prod_id)
        pw.setprodName(first_name2)
        pw.setserialNumber(prod_id2)
        pw.setpurchaseDate(self.purchaseDate)
        pw.setfile_invoice(self.file_path)
        xpath = "//span[text()='" + self.verify_file + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.is_displayed()
        pw.setcustomerName(first_name3)
        pw.setcustomerEmail(custEmail)
        pw.setcustomerPhone(phoneNumber)
        pw.clickSubmitButton()
        xpath = pw.text_verifyCreate
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Super admin - can able to raise the warranty on behalf of customer == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False
        pw.clickclose_Toast()
        self.logger.info("Started Reject the warranty Request - the warranty which are raised by super admin")
        self.logger.info("Searching Product ID to Reject")
        pw.setsearchField(prod_id)
        xpath = "//span[text()='" + prod_id + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.click()
        pw.clickRejectButton()
        pw.clickConfRejectButton()
        xpath = pw.text_verifyReject
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Reject the warranty Request - the warranty which are raised by super admin ")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False

    @pytest.mark.run(order=3)
    # @pytest.mark.test
    def test_RegisterPW_SuperAdmin_Approve(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.logger.info(" Started Super admin - can able to raise the warranty on behalf of customer.")
        driver.get(self.baseURL)
        prod_id = randomGen.random_Emp_Id()
        prod_id2 = randomGen.random_Emp_Id()
        first_name2 = randomGen.random_first_name()
        first_name3 = randomGen.random_first_name()
        custEmail = randomGen.random_email()
        phoneNumber = randomGen.random_phone_number()
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        pw = productWarranty(driver)
        pw.clickPWfeature()
        pw.clickRegisterButton()
        pw.setProductId(prod_id)
        pw.setprodName(first_name2)
        pw.setserialNumber(prod_id2)
        pw.setpurchaseDate(self.purchaseDate)
        pw.setfile_invoice(self.file_path)
        xpath = "//span[text()='" + self.verify_file + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.is_displayed()
        pw.setcustomerName(first_name3)
        pw.setcustomerEmail(custEmail)
        pw.setcustomerPhone(phoneNumber)
        pw.clickSubmitButton()
        xpath = pw.text_verifyCreate
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Super admin - can able to raise the warranty on behalf of customer == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False
        pw.clickclose_Toast()
        self.logger.info("Started Approve the warranty Request - the warranty which are raised by super admin")
        self.logger.info("Searching Product ID to Approve")
        pw.setsearchField(prod_id)
        xpath = "//span[text()='" + prod_id + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.click()
        pw.setExpiryDate(self.ExpiryDate)
        pw.clickApproveButton()
        pw.clickConfApproveButton()
        xpath = pw.text_verifyApprove
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Approve the warranty Request - the warranty which are raised by super admin ")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False

    @pytest.mark.run(order=4)
    # @pytest.mark.test
    def test_RegisterPW_RjectCustomerbySuperAdmin(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.logger.info("Started Individual account / Customer - can able to raise the warranty on behalf of customer.")
        driver.get(self.baseURL)
        prod_id = randomGen.random_Emp_Id()
        prod_id2 = randomGen.random_Emp_Id()
        first_name2 = randomGen.random_first_name()
        first_name3 = randomGen.random_first_name()
        phoneNumber = randomGen.random_phone_number()
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.CustomerUsername)
        lp.setPassword(self.password)
        lp.clickLogin()
        pw = productWarranty(driver)
        pw.clickPWfeature_Individual()
        pw.clickRegisterButton()
        pw.setSearchCompany(self.companyName)
        xpath = "//span[text()='" + self.companyName + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.click()
        pw.setProductId(prod_id)
        pw.setprodName(first_name2)
        pw.setserialNumber(prod_id2)
        pw.setpurchaseDate(self.purchaseDate)
        pw.setfile_invoice(self.file_path)
        xpath = "//span[text()='" + self.verify_file + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.is_displayed()
        pw.setcustomerName(first_name3)
        pw.setcustomerPhone(phoneNumber)
        pw.clickSubmitButton()
        xpath = pw.text_verifyCreate
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Individual account / Customer - can able to raise the warranty on behalf of customer == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_RegisterPW.png")
            assert False
        pw.clickclose_Toast()
        pw.clickProfileIcon()
        pw.clicklogoutButton()
        pw.clickConflogoutButton()
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        pw.clickPWfeature()
        self.logger.info("Started Super admin Reject the warranty Request - the warranty which are raised by customer")
        self.logger.info("Searching Product ID to Reject")
        pw.setsearchField(prod_id)
        xpath = "//span[text()='" + prod_id + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.click()
        pw.clickRejectButton()
        pw.clickConfRejectButton()
        xpath = pw.text_verifyReject
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Super admin Reject the warranty Request - the warranty which are raised by customer ")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False

    @pytest.mark.run(order=5)
    # @pytest.mark.test
    def test_RegisterPW_ApproveCustomerbySuperAdmin(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.logger.info("Started Individual account / Customer - can able to raise the warranty on behalf of customer.")
        driver.get(self.baseURL)
        prod_id = randomGen.random_Emp_Id()
        prod_id2 = randomGen.random_Emp_Id()
        first_name2 = randomGen.random_first_name()
        first_name3 = randomGen.random_first_name()
        phoneNumber = randomGen.random_phone_number()
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.CustomerUsername)
        lp.setPassword(self.password)
        lp.clickLogin()
        pw = productWarranty(driver)
        pw.clickPWfeature_Individual()
        pw.clickRegisterButton()
        pw.setSearchCompany(self.companyName)
        xpath = "//span[text()='" + self.companyName + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.click()
        pw.setProductId(prod_id)
        pw.setprodName(first_name2)
        pw.setserialNumber(prod_id2)
        pw.setpurchaseDate(self.purchaseDate)
        pw.setfile_invoice(self.file_path)
        xpath = "//span[text()='" + self.verify_file + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.is_displayed()
        pw.setcustomerName(first_name3)
        pw.setcustomerPhone(phoneNumber)
        pw.clickSubmitButton()
        xpath = pw.text_verifyCreate
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Super admin Reject the warranty Request - the warranty which are raised by customer")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_RegisterPW.png")
            assert False
        pw.clickclose_Toast()
        pw.clickProfileIcon()
        pw.clicklogoutButton()
        pw.clickConflogoutButton()
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        pw.clickPWfeature()
        self.logger.info("Started Super admin Approve the warranty Request - the warranty which are raised by customer")
        self.logger.info("Searching Product ID to Reject")
        pw.setsearchField(prod_id)
        xpath = "//span[text()='" + prod_id + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.click()
        pw.setExpiryDate(self.ExpiryDate)
        pw.clickApproveButton()
        pw.clickConfApproveButton()
        xpath = pw.text_verifyApprove
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Super admin Approve the warranty Request - the warranty which are raised by customer ")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False

