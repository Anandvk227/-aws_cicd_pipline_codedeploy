import os
import time
from turtle import window_width

import pytest
from openpyxl.reader.excel import load_workbook
from selenium.webdriver import ActionChains
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
    def test_RegisterPW_SuperAdmin_Edit_Delete(self, driver):
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
        self.logger.info("Previewing and downloading uploaded invoice")
        time.sleep(1) #Given 1 sec of time to identify file which is hidden in page, where it require to scrol right and click
        xpath = "//span[text()='" + self.verify_file + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.click()
        pw.clickDownload_filePreview()
        pw.clickClose_filePreview()
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
        self.logger.info("Previewing and downloading uploaded invoice")
        time.sleep(
            1)  # Given 1 sec of time to identify file which is hidden in page, where it require to scrol right and click
        xpath = "//span[text()='" + self.verify_file + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.click()
        pw.clickDownload_filePreview()
        pw.clickClose_filePreview()
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

    @pytest.mark.run(order=6)
    # @pytest.mark.test
    def test_RegisterPW_Admin(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.logger.info("Started admin - can able to raise the warranty on behalf of customer.")
        driver.get(self.baseURL)
        prod_id = randomGen.random_Emp_Id()
        prod_id2 = randomGen.random_Emp_Id()
        first_name2 = randomGen.random_first_name()
        first_name3 = randomGen.random_first_name()
        custEmail = randomGen.random_email()
        phoneNumber = randomGen.random_phone_number()
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.adminUsername)
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
                "Test Passed == admin - can able to raise the warranty on behalf of customer == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False
        pw.clickclose_Toast()
        self.logger.info("Started Edit warranty - that is raised by admin on behalf of customer")
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
                "Test Passed == Edit warranty - that is raised by admin on behalf of customer == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False
        pw.clickclose_Toast()
        self.logger.info("Started Delete warranty - that is raised by admin on behalf of customer")
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
                "Test Passed == Delete warranty - that is raised by admin on behalf of customer == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False

    @pytest.mark.run(order=7)
    # @pytest.mark.test
    def test_RegisterPW_Admin_Reject(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.logger.info(" Started admin - can able to raise the warranty on behalf of customer.")
        driver.get(self.baseURL)
        prod_id = randomGen.random_Emp_Id()
        prod_id2 = randomGen.random_Emp_Id()
        first_name2 = randomGen.random_first_name()
        first_name3 = randomGen.random_first_name()
        custEmail = randomGen.random_email()
        phoneNumber = randomGen.random_phone_number()
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.adminUsername)
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
                "Test Passed == admin - can able to raise the warranty on behalf of customer == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False
        pw.clickclose_Toast()
        self.logger.info("Started Reject the warranty Request - the warranty which are raised by admin")
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
                "Test Passed == Reject the warranty Request - the warranty which are raised by admin ")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False

    @pytest.mark.run(order=8)
    # @pytest.mark.test
    def test_RegisterPW_Admin_Approve(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.logger.info(" Started admin - can able to raise the warranty on behalf of customer.")
        driver.get(self.baseURL)
        prod_id = randomGen.random_Emp_Id()
        prod_id2 = randomGen.random_Emp_Id()
        first_name2 = randomGen.random_first_name()
        first_name3 = randomGen.random_first_name()
        custEmail = randomGen.random_email()
        phoneNumber = randomGen.random_phone_number()
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.adminUsername)
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
                "Test Passed == admin - can able to raise the warranty on behalf of customer == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False
        pw.clickclose_Toast()
        self.logger.info("Started Approve the warranty Request - the warranty which are raised by admin")
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
                "Test Passed == Approve the warranty Request - the warranty which are raised by admin ")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False

    @pytest.mark.run(order=9)
    @pytest.mark.test
    def test_RegisterPW_RjectCustomerbyAdmin_Edit_UpdateCustomer(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.logger.info(
            "Started Individual account / Customer - can able to raise the warranty on behalf of customer.")
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
        lp.setUserName(self.adminUsername)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        pw.clickPWfeature()
        self.logger.info("Started admin Reject the warranty Request - the warranty which are raised by customer")
        self.logger.info("Searching Product ID to Reject")
        pw.setsearchField(prod_id)
        pw.clickiconStatus_Reject()
        pw.clickiconStatus_ConfReject()
        xpath = pw.text_verifyReject
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == admin Reject the warranty Request - the warranty which are raised by customer ")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False
        self.logger.info("Started update the warrenty - if admin reject the warrenty ,user can update the warrenty details. ")
        pw.clickclose_Toast()
        pw.clickProfileIcon()
        pw.clicklogoutButton()
        pw.clickConflogoutButton()
        lp.setUserName(self.CustomerUsername)
        lp.setPassword(self.password)
        lp.clickLogin()
        pw = productWarranty(driver)
        pw.clickPWfeature_Individual()
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


    @pytest.mark.run(order=10)
    # @pytest.mark.test
    def test_RegisterPW_ApproveCustomerbyAdmin(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.logger.info(
            "Started Individual account / Customer - can able to raise the warranty on behalf of customer.")
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
                "Test Passed == admin Reject the warranty Request - the warranty which are raised by customer")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_RegisterPW.png")
            assert False
        pw.clickclose_Toast()
        pw.clickProfileIcon()
        pw.clicklogoutButton()
        pw.clickConflogoutButton()
        lp.setUserName(self.adminUsername)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        pw.clickPWfeature()
        self.logger.info("Started admin Approve the warranty Request - the warranty which are raised by customer")
        self.logger.info("Searching Product ID to Reject")
        pw.setsearchField(prod_id)
        self.logger.info("using icons present on the page to approve")
        pw.clickiconStatus_Approve()
        pw.setExpiryDate(self.ExpiryDate)
        pw.clickContinueButton()
        pw.clickiconStatusConf_Approve()
        xpath = pw.text_verifyApprove
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == admin Approve the warranty Request - the warranty which are raised by customer ")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False

    @pytest.mark.run(order=11)
    # @pytest.mark.test
    def test_RegisterPW_CustomerEditDelete(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.logger.info(
            "Started Individual account / Customer - can able to raise the warranty on behalf of customer.")
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
                "Test Passed == admin Reject the warranty Request - the warranty which are raised by customer")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_RegisterPW.png")
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
        self.logger.info("Previewing and downloading uploaded invoice")
        time.sleep(
            1)  # Given 1 sec of time to identify file which is hidden in page, where it require to scrol right and click
        xpath = "//span[text()='" + self.verify_file + "']"
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        element.click()
        pw.clickDownload_filePreview()
        pw.clickClose_filePreview()
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
    @pytest.mark.run(order=12)
    # @pytest.mark.test
    def test_FilterPW_SuperAdmin(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.logger.info("Started Filter ALL deselect")
        driver.get(self.baseURL)
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        pw = productWarranty(driver)
        pw.clickPWfeature()
        pw.clickIconFilter()
        pw.clickfilterAll()
        xpath = "//span[contains(text(),'No Warranty is registered')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Started Filter ALL deselect == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False
        self.logger.info("Started Filter Pending deselect")
        pw.clickIconFilter()
        pw.clickfilterPending()
        self.logger.info(
            "Started verifying Pending Filter Option that All rows contain 'Pending' and no other statuses.")
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))
        )

        # Iterate over each row
        for row in rows:
            # Check if 'Pending' text is present in the row
            pending_text = row.text.strip()
            assert 'Pending' in pending_text, f"Row text: {pending_text} does not contain 'Pending'"

            # Check if other statuses are not present in the row
            other_statuses = ['Active', 'Rejected', 'Expired']
            for status in other_statuses:
                assert status not in pending_text, f"Row text: {pending_text} contains '{status}'"
        self.logger.info(
            "Test Passed == All rows contain 'Pending' and no other statuses. == Test Passed")
        print("All rows contain 'Pending' and no other statuses.")

        self.logger.info("Started Filter Active deselect")
        pw.clickIconFilter()
        pw.clickfilterPending()
        pw.clickIconFilter()
        pw.clickfilterActive()
        self.logger.info(
            "Started verifying Active Filter Option that All rows contain 'Active' and no other statuses.")
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))
        )

        # Iterate over each row
        for row in rows:
            # Check if 'Pending' text is present in the row
            pending_text = row.text.strip()
            assert 'Active' in pending_text, f"Row text: {pending_text} does not contain 'Active'"

            # Check if other statuses are not present in the row
            other_statuses = ['Pending', 'Rejected', 'Expired']
            for status in other_statuses:
                assert status not in pending_text, f"Row text: {pending_text} contains '{status}'"
        self.logger.info(
            "Test Passed == All rows contain 'Active' and no other statuses. == Test Passed")
        print("All rows contain 'Pending' and no other statuses.")
        pw.clickIconFilter()
        pw.clickfilterActive()
        pw.clickIconFilter()
        pw.clickfilterRejected()
        self.logger.info(
            "Started verifying Rejected Filter Option that All rows contain 'Rejected' and no other statuses.")
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))
        )

        # Iterate over each row
        for row in rows:
            # Check if 'Pending' text is present in the row
            pending_text = row.text.strip()
            assert 'Rejected' in pending_text, f"Row text: {pending_text} does not contain 'Rejected'"

            # Check if other statuses are not present in the row
            other_statuses = ['Pending', 'Active', 'Expired']
            for status in other_statuses:
                assert status not in pending_text, f"Row text: {pending_text} contains '{status}'"
        self.logger.info(
            "Test Passed == All rows contain 'Rejected' and no other statuses. == Test Passed")
        print("All rows contain 'Rejected' and no other statuses.")
        self.logger.info(
            "Started verifying Expired Filter Option that displays No Warranty is registered when there is no expired  ")
        pw.clickIconFilter()
        pw.clickfilterRejected()
        pw.clickIconFilter()
        pw.clickfilterExpired()
        xpath = "//span[contains(text(),'No Warranty is registered')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Started Filter Expired  == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False

        pw.clickIconFilter()
        pw.clickfilterExpired()
        pw.clickIconFilter()
        pw.clickfilterClear()
        # Log the start of the verification process
        self.logger.info("Started verifying that all rows contain 'Rejected', 'Pending', 'Active', or 'Expired'.")

        # Wait for all rows to be present in the table
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))
        )

        # Specify the statuses to check for
        statuses_to_check = ['Rejected', 'Pending', 'Active', 'Expired']

        # Flag to track if any row doesn't contain any of the specified statuses
        all_rows_contain_status = True

        # Iterate over each row
        for row in rows:
            # Get the text of the row
            row_text = row.text.strip()
            # Flag to track if any of the statuses are found in the row
            status_found = False
            # Check if any of the specified statuses are present in the row
            for status in statuses_to_check:
                if status in row_text:
                    status_found = True
                    break
            # If none of the statuses are found in the row, set the flag to False
            if not status_found:
                all_rows_contain_status = False
                break

        # Pass the assertion if all rows contain at least one of the specified statuses
        assert all_rows_contain_status, "Not all rows contain 'Rejected', 'Pending', 'Active', or 'Expired'."

        # Log the verification result
        self.logger.info("Test Passed == All rows contain 'Rejected', 'Pending', 'Active', or 'Expired'.")

        # Print verification message
        print("All rows contain 'Rejected', 'Pending', 'Active', or 'Expired'.")
    @pytest.mark.run(order=13)
    # @pytest.mark.test
    def test_FilterPW_Customer(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        self.logger.info("Started Filter ALL deselect")
        driver.get(self.baseURL)
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        pw = productWarranty(driver)
        pw.clickPWfeature()
        pw.clickIconFilter()
        pw.clickfilterAll()
        xpath = "//span[contains(text(),'No Warranty is registered')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            self.logger.info(
                "Test Passed == Started Filter ALL deselect == Test Passed")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            assert False
        self.logger.info("Started Filter Pending deselect")
        pw.clickIconFilter()
        pw.clickfilterPending()
        self.logger.info(
            "Started verifying Pending Filter Option that All rows contain 'Pending' and no other statuses.")
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))
        )

        # Iterate over each row
        for row in rows:
            # Check if 'Pending' text is present in the row
            pending_text = row.text.strip()
            assert 'Pending' in pending_text, f"Row text: {pending_text} does not contain 'Pending'"

            # Check if other statuses are not present in the row
            other_statuses = ['Active', 'Rejected', 'Expired']
            for status in other_statuses:
                assert status not in pending_text, f"Row text: {pending_text} contains '{status}'"
        self.logger.info(
            "Test Passed == All rows contain 'Pending' and no other statuses. == Test Passed")
        print("All rows contain 'Pending' and no other statuses.")

        self.logger.info("Started Filter Active deselect")
        pw.clickIconFilter()
        pw.clickfilterPending()
        pw.clickIconFilter()
        pw.clickfilterActive()
        self.logger.info(
            "Started verifying Active Filter Option that All rows contain 'Active' and no other statuses.")
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))
        )

        # Iterate over each row
        for row in rows:
            # Check if 'Pending' text is present in the row
            pending_text = row.text.strip()
            assert 'Active' in pending_text, f"Row text: {pending_text} does not contain 'Active'"

            # Check if other statuses are not present in the row
            other_statuses = ['Pending', 'Rejected', 'Expired']
            for status in other_statuses:
                assert status not in pending_text, f"Row text: {pending_text} contains '{status}'"
        self.logger.info(
            "Test Passed == All rows contain 'Active' and no other statuses. == Test Passed")
        print("All rows contain 'Pending' and no other statuses.")
        pw.clickIconFilter()
        pw.clickfilterActive()
        pw.clickIconFilter()
        pw.clickfilterRejected()
        self.logger.info(
            "Started verifying Rejected Filter Option that All rows contain 'Rejected' and no other statuses.")
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))
        )

        # Iterate over each row
        for row in rows:
            # Check if 'Pending' text is present in the row
            pending_text = row.text.strip()
            assert 'Rejected' in pending_text, f"Row text: {pending_text} does not contain 'Rejected'"

            # Check if other statuses are not present in the row
            other_statuses = ['Pending', 'Active', 'Expired']
            for status in other_statuses:
                assert status not in pending_text, f"Row text: {pending_text} contains '{status}'"
        self.logger.info(
            "Test Passed == All rows contain 'Rejected' and no other statuses. == Test Passed")
        print("All rows contain 'Rejected' and no other statuses.")
        self.logger.info(
            "Started verifying Expired Filter Option that displays No Warranty is registered when there is no expired  ")

        pw.clickIconFilter()
        pw.clickfilterExpired()
        pw.clickIconFilter()
        pw.clickfilterClear()
        # Log the start of the verification process
        self.logger.info("Started verifying that all rows contain 'Rejected', 'Pending', 'Active', or 'Expired'.")

        # Wait for all rows to be present in the table
        rows = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr"))
        )

        # Specify the statuses to check for
        statuses_to_check = ['Rejected', 'Pending', 'Active', 'Expired']

        # Flag to track if any row doesn't contain any of the specified statuses
        all_rows_contain_status = True

        # Iterate over each row
        for row in rows:
            # Get the text of the row
            row_text = row.text.strip()
            # Flag to track if any of the statuses are found in the row
            status_found = False
            # Check if any of the specified statuses are present in the row
            for status in statuses_to_check:
                if status in row_text:
                    status_found = True
                    break
            # If none of the statuses are found in the row, set the flag to False
            if not status_found:
                all_rows_contain_status = False
                break

        # Pass the assertion if all rows contain at least one of the specified statuses
        assert all_rows_contain_status, "Not all rows contain 'Rejected', 'Pending', 'Active', or 'Expired'."

        # Log the verification result
        self.logger.info("Test Passed == All rows contain 'Rejected', 'Pending', 'Active', or 'Expired'.")

        # Print verification message
        print("All rows contain 'Rejected', 'Pending', 'Active', or 'Expired'.")
