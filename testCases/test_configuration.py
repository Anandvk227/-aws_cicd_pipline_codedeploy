import time
import unittest
import pytest
from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.randomGen import randomGen
from pageObjects.ConfigurationPage import ConfigurationPage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from GenericLib.BaseClass import BaseClass

class TestConfiguration():
    baseURL = ReadConfig.getApplicationURL()
    DeptName = "QA"
    first_name = randomGen.random_first_name()
    first_name2 = randomGen.random_first_name()
    DeptDescription = "Software Testing"
    EditDeptDescription = "Software Testing test data"
    DivisionName = "Manual Testing"
    DivisionDescription = "Functional and Non Functional"
    EditDivisionDescription = "Functional and Non Functional test data"
    DesignationName = "Associate Test Engineer"
    DesignationDescription = "All testing activities"
    EditDesignationDescription = "All testing activities test data"

    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

    username = worksheet["A2"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.test9
    # @pytest.mark.flaky(reruns=3, reruns_delay=2)
    @pytest.mark.run(order=7)
    def test_createDept(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        cp = ConfigurationPage(driver)
        cp.clickModuleConfiguration()
        # cp.clickDepartments()
        self.logger.info(" Started TC_01 : Verify create NEW Department ")
        cp.clickNewBtn()
        cp.setDepartmentName(self.DeptName + " " + self.first_name)
        cp.setEnterDescription(self.DeptDescription)
        cp.clickCreateBtn()

        act_Text = WebDriverWait(driver, 10).until(
            lambda driver: cp.Text_DeptCreatedSuccessful()
        )

        if act_Text == "Department created successfully":
            assert True
            self.logger.info("********* TC_01 : Verify create NEW Department Test is Passed ***********")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_createDept.png")
            self.logger.error("********* TC_01 : Verify create NEW Department Test is Failed ***********")
            assert False
        time.sleep(3)
        self.logger.info(" Started TC_04 : Verify Search Department ")
        cp.setsearchField(self.DeptName + " " + self.first_name)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'" + self.DeptName + " " + self.first_name + "')]"))
        )
        element.click()
        # cp.clickopenDept()
        self.logger.info(" Started TC_06 : Verify create NEW Division ")
        cp.clickDivisionsTab()
        cp.clickNewBtn()
        cp.setDepartmentName(self.DivisionName)
        cp.setEnterDescription(self.DivisionDescription)
        cp.clickCreateBtn()
        act_Text = WebDriverWait(driver, 10).until(
            lambda driver: cp.Text_DivisionCreatedSuccessful()
        )

        if act_Text == "Division created successfully":
            assert True
            self.logger.info("********* TC_06 : Verify create NEW Division Test is Passed ***********")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_createDivision.png")
            self.logger.error("********* Create Division Test is Failed ***********")
            assert False

        cp.clickDesignationsTab()
        self.logger.info(" Started TC_10 : Verify Create NEW Designation ")
        cp.clickNewBtn()
        cp.setDepartmentName(self.DesignationName)
        cp.setEnterDescription(self.DesignationDescription)
        cp.clickCreateBtn()
        act_Text = WebDriverWait(driver, 10).until(
            lambda driver: cp.Text_DesignationCreatedSuccessful()
        )

        if act_Text == "Designation created successfully":
            assert True
            self.logger.info("********* Create Designation Test is Passed ***********")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "TC_10_test_createDesignation.png")
            self.logger.error("********* TC_10 : Verify Create NEW Designation Test is Failed ***********")
            assert False

    @pytest.mark.regression
    # @pytest.mark.test
    @pytest.mark.run(order=8)
    def test_EditDept(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****TC_02	Verify Edit Department****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        cp = ConfigurationPage(driver)
        cp.clickModuleConfiguration()
        # cp.clickDepartments()
        # cp.clickDepartments()
        cp.setsearchField(self.DeptName + " " + self.first_name)
        time.sleep(2)
        cp.clickEditDepartment()
        cp.setEnterDescription(self.EditDeptDescription)
        time.sleep(1)
        cp.clickUpdateBtn()
        act_Text = WebDriverWait(driver, 10).until(
            lambda driver: cp.Text_DeptUpdatedSuccessful()
        )

        if act_Text == "Department updated successfully":
            assert True
            self.logger.info("********* updated Department Test is Passed ***********")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_updateDept.png")
            self.logger.error("********* updated Department Test is Failed ***********")
            assert False
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'" + self.DeptName + " " + self.first_name + "')]"))
        )
        element.click()
        # cp.clickopenDept()
        cp.clickDivisionsTab()
        cp.setsearchField(self.DivisionName)
        self.logger.info("********* TC_07	Verify Edit the Division ***********")
        time.sleep(2)
        cp.clickEditDivision()
        cp.setEnterDescription(self.EditDivisionDescription)
        cp.clickUpdateBtn()
        act_Text = WebDriverWait(driver, 10).until(
            lambda driver: cp.Text_DivisionUpdatedSuccessful()
        )

        if act_Text == "Division updated successfully":
            assert True
            self.logger.info("********* updated Division Test is Passed ***********")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_UpdateDivision.png")
            self.logger.error("********* updated Division Test is Failed ***********")
            assert False

        cp.clickDesignationsTab()
        self.logger.info(" Started TC_01 : Verify create NEW Department ")
        cp.setsearchField(self.DesignationName)
        cp.clickEditDivision()
        time.sleep(2)
        self.logger.info("********* TC_13	Verify Search Designation***********")
        cp.setEnterDescription(self.EditDesignationDescription)
        cp.clickUpdateBtn()
        act_Text = WebDriverWait(driver, 10).until(
            lambda driver: cp.Text_DesignationUpdatedSuccessful()
        )

        if act_Text == "Designation updated successfully":
            assert True
            self.logger.info("********* updated Designation Test is Passed ***********")

        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_UpdateDesignation.png")
            self.logger.error("********* updated Designation Test is Failed ***********")
            assert False

    @pytest.mark.regression
    @pytest.mark.test9
    @pytest.mark.run(order=9)
    def test_DeleteDept(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        cp = ConfigurationPage(driver)
        cp.clickModuleConfiguration()
        # cp.clickDepartments()
        time.sleep(3)
        # cp.setsearchField(self.DeptName + " " + self.first_name)
        time.sleep(2)
        self.logger.info("****TC_03	Verify Delete Department****")
        cp.clickDeleteDepartment()
        cp.clickDeleteDepartmentDelete()
        act_Text = WebDriverWait(driver, 10).until(
            lambda driver: cp.Text_DeleteError()
        )

        if act_Text == "Some Division Under This Department":
            assert True
            self.logger.info("********* Delete Error Designation Test is Passed ***********")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_DevisionError.png")
            self.logger.error("********* Delete Error Designation Test is Failed ***********")
            assert False

        cp.clickDeleteDepartmentCancel()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'" + self.DeptName + " " + self.first_name + "')]"))
        )
        element.click()
        # cp.clickopenDept()
        self.logger.info("****TC_05	Verify by clicking on created Department****")
        cp.clickDivisionsTab()
        self.logger.info("****TC_09	Verify Search Division****")
        cp.setsearchField(self.DivisionName)
        time.sleep(2)
        self.logger.info("****TC_08	Verify Delete the Division****")
        cp.clickDeleteDivision()
        cp.clickDeleteDepartmentDelete()
        act_Text = WebDriverWait(driver, 10).until(
            lambda driver: cp.Text_DivisionDeletedSuccessfully()
        )

        if act_Text == "Division deleted successfully":
            assert True
            self.logger.info("********* Delete Division Test is Passed ***********")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_DeleteDivision.png")
            self.logger.error("********* Delete Division Test is Failed ***********")
            assert False

        cp.clickDesignationsTab()
        cp.setsearchField(self.DesignationName)
        self.logger.info("*********TC_12	Verify Delete the Designation***********")
        cp.clickDeleteDivision()
        cp.clickDeleteDepartmentDelete()
        act_Text = WebDriverWait(driver, 10).until(
            lambda driver: cp.Text_DesignationDeletedSuccessfully()
        )

        if act_Text == "Designation deleted successfully":
            assert True
            self.logger.info("********* Delete Designation Test is Passed ***********")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_DeleteDesignation.png")
            self.logger.error("********* Delete Designation Test is Failed ***********")
            assert False

        # Use the browser's back button to navigate back
        cp.clickConfigurationtextLink()

        # Wait for a few seconds (for demonstration purposes)
        # time.sleep(3)

        cp.setsearchField(self.DeptName + " " + self.first_name)
        time.sleep(2)
        self.logger.info("*********TC_03	Verify Delete Department***********")
        cp.clickDeleteDepartment()
        cp.clickDeleteDepartmentDelete()
        act_Text = WebDriverWait(driver, 10).until(
            lambda driver: cp.Text_DepartmentDeletedSuccessfully()
        )

        if act_Text == "Department deleted successfully":
            assert True
            self.logger.info("********* Delete Department Test is Passed ***********")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_DeleteDept.png")
            self.logger.error("********* Delete Department Test is Failed ***********")
            assert False

    @pytest.mark.regression
    @pytest.mark.flaky(rerun=3, reun_delay=2)
    @pytest.mark.run(order=10)
    def test_CreateConfDept(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        cp = ConfigurationPage(driver)
        cp.clickModuleConfiguration()
        # cp.clickDepartments()
        self.logger.info(" Started TC_01 : Verify create NEW Department ")
        cp.clickNewBtn()
        cp.setDepartmentName(self.DeptName + " " + self.first_name2)
        cp.setEnterDescription(self.DeptDescription)
        cp.clickCreateBtn()

        act_Text = WebDriverWait(driver, 10).until(
            lambda driver: cp.Text_DeptCreatedSuccessful()
        )

        if act_Text == "Department created successfully":
            assert True
            self.logger.info("********* TC_01 : Verify create NEW Department Test is Passed ***********")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_createDept.png")
            self.logger.error("********* TC_01 : Verify create NEW Department Test is Failed ***********")
            assert False

        self.logger.info(" Started TC_04 : Verify Search Department ")
        cp.setsearchField(self.DeptName + " " + self.first_name2)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[contains(text(),'" + self.DeptName + " " + self.first_name2 + "')]"))
        )
        element.click()
        # cp.clickopenDept()
        self.logger.info(" Started TC_06 : Verify create NEW Division ")
        cp.clickDivisionsTab()
        cp.clickNewBtn()
        cp.setDepartmentName(self.DivisionName)
        cp.setEnterDescription(self.DivisionDescription)
        cp.clickCreateBtn()
        act_Text = WebDriverWait(driver, 10).until(
            lambda driver: cp.Text_DivisionCreatedSuccessful()
        )

        if act_Text == "Division created successfully":
            assert True
            self.logger.info("********* TC_06 : Verify create NEW Division Test is Passed ***********")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "test_createDivision.png")
            self.logger.error("********* Create Division Test is Failed ***********")
            assert False

        cp.clickDesignationsTab()
        self.logger.info(" Started TC_10 : Verify Create NEW Designation ")
        cp.clickNewBtn()
        cp.setDepartmentName(self.DesignationName)
        cp.setEnterDescription(self.DesignationDescription)
        cp.clickCreateBtn()
        act_Text = WebDriverWait(driver, 10).until(
            lambda driver: cp.Text_DesignationCreatedSuccessful()
        )

        if act_Text == "Designation created successfully":
            assert True
            self.logger.info("********* Create Designation Test is Passed ***********")
        else:
            driver.save_screenshot(".\\Screenshots\\" + "TC_10_test_createDesignation.png")
            self.logger.error("********* TC_10 : Verify Create NEW Designation Test is Failed ***********")
            assert False

    if __name__ == '__main__':
        unittest.main(verbosity=2)
