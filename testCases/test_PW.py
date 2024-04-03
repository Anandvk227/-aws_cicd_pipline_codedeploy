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
class Test_PW ():
    baseURL = ReadConfig.getApplicationURL()
    first_name = randomGen.random_first_name()
    file_name = "Files/Free_Test_Data_1MB_PDF.pdf"
    file_path = os.path.abspath(os.path.join(os.getcwd(), file_name))
    purchaseDate = "03-04-2024"
    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active
    username = worksheet["A2"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger = LogGen.loggen()

    @pytest.mark.run(order=1)
    def test_RegisterPW(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
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
        pw.clickRegisterButton()
        pw.setProductId(prod_id)
        pw.setprodName(first_name2)
        pw.setserialNumber(prod_id2)
        pw.setpurchaseDate(self.purchaseDate)
        pw.setfile_invoice("file_path")
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
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_RegisterPW.png")
            assert False