import time
import pytest


from openpyxl.reader.excel import load_workbook

from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from Anand_PageObjects.RecognitionPage import Recognitions
from GenericLib.BaseClass import BaseClass


class Test_Create_Recognition():
    baseURL = ReadConfig.getApplicationURL()

    addemployee="Anand"
    addtitle="Best Employee of the Year"
    adddescription="The Best Employee of the Year is recognized for exceptional performance, innovation, teamwork, leadership, adaptability, initiative, reliability, positivity, customer focus, and continuous learning."


    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

    username = worksheet["B14"].value
    username1=worksheet["E14"].value
    password = ReadConfig.getPassword()

    workbook.close()

    logger=LogGen.loggen()


    @pytest.mark.regression
    @pytest.mark.run(order=81)
    # @pytest.mark.skip(reason="skipping this Test")
    def test_CreateRecognition_Verify_Employee_got_Recognition(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(3)
        if "News Feed" in driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False

        rcp = Recognitions(driver)
        rcp.clickrecognition()
        if "Recognition" in driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False

        rcp.clicknewrecognition()
        time.sleep(2)
        rcp.selecttemplate()
        rcp.selectbadge()
        rcp.clicknext()
        rcp.setaddemployee(self.addemployee)
        rcp.clickemployee()
        rcp.setaddtitle(self.addtitle)
        rcp.setadddescription(self.adddescription)
        rcp.clickonpreview()
        rcp.clickpublish()
        time.sleep(2)
        if "Employee recognition has been successfully published" in driver.page_source:
            self.logger.info("********** Employee recognition published test is passed *********")
            self.logger.info("********** content creation test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition published test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_CreateRecognition_Verify_Employee_got_Recognition.png")
            assert False

        lp.clickLogout()
        lp.setUserName(self.username1)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in driver.page_source:
            self.logger.info("********** Employee recognition verification test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition verification test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_CreateRecognition_Verify_Employee_got_Recognition.png")
            assert False

        rcp.closepopup()
        lp.clickLogout()

    @pytest.mark.regression
    @pytest.mark.run(order=82)
    # @pytest.mark.skip(reason="skipping this Test")
    # @pytest.mark.skip(reason="skipping this Test")
    def test_UnpublishedRecognition_and_Verify_in_Employee_account(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(4)
        if "News Feed" in driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False

        rcp = Recognitions(driver)
        rcp.clickrecognition()
        if "Recognition" in driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False

        rcp.clicknewrecognition()
        time.sleep(2)
        rcp.selecttemplate()
        rcp.selectbadge()
        rcp.clicknext()
        time.sleep(2)
        rcp.setaddemployee(self.addemployee)
        rcp.clickemployee()
        rcp.setaddtitle(self.addtitle)
        rcp.setadddescription(self.adddescription)
        time.sleep(1)
        rcp.clickonpreview()
        time.sleep(1)
        rcp.savetemplate()
        time.sleep(2)
        if "Employee recognition has been saved in unpublished" in driver.page_source:
            self.logger.info("********** Employee recognition unpublished test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition unpublished test is failed **********")
            driver.save_screenshot(
                ".\\Screenshots\\" + "test_UnpublishedRecognition_and_Verify_in_Employee_account.png")
            assert False

        time.sleep(1)
        if "Anand" in driver.page_source:
            self.logger.info("********** Employee verification test is passed *********")
            self.logger.info("********** content creation test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** Employee verification test is failed **********")
            driver.save_screenshot(
                ".\\Screenshots\\" + "test_UnpublishedRecognition_and_Verify_in_Employee_account.png")
            assert False

        lp.clickLogout()
        lp.setUserName(self.username1)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(2)
        if "News Feed" in driver.page_source:
            self.logger.info("********** Employee Login successfully *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** Employee Login failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "Employee_login_fail.png")
            assert False

        lp.clickLogout()

    @pytest.mark.regression
    @pytest.mark.run(order=83)
    # @pytest.mark.skip(reason="skipping this Test")
    # @pytest.mark.anand
    def test_UnpublishedtoPunlishRecognition(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(4)
        if "News Feed" in driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False
        rcp = Recognitions(driver)
        rcp.clickrecognition()
        if "Recognition" in driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False
        rcp.clicknewrecognition()
        time.sleep(2)
        rcp.selecttemplate()
        rcp.selectbadge()
        rcp.clicknext()
        time.sleep(2)
        rcp.setaddemployee(self.addemployee)
        rcp.clickemployee()
        rcp.setaddtitle(self.addtitle)
        rcp.setadddescription(self.adddescription)
        time.sleep(1)
        rcp.clickonpreview()
        time.sleep(1)
        rcp.savetemplate()
        time.sleep(2)
        if "Employee recognition has been saved in unpublished" in driver.page_source:
            self.logger.info("********** Employee recognition unpublished test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition unpublished test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_UnpublishedtoPublishRecognition.png")
            assert False
        time.sleep(1)

        if "Anand" in driver.page_source:
            self.logger.info("********** Employee verification test is passed *********")
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee verification test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_UnpublishedtoPublishRecognition.png")
            assert False
        time.sleep(1)
        lp.clickLogout()
        time.sleep(2)
        lp.setUserName(self.username1)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(3)
        if "News Feed" in driver.page_source:
            self.logger.info("********** Employee Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee Login failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "Employee_login_fail.png")
            assert False

        time.sleep(2)
        lp.clickLogout()
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(4)
        if "News Feed" in driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False
        rcp = Recognitions(driver)
        rcp.clickrecognition()
        time.sleep(2)
        if "Recognition" in driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False
        rcp.unpublishedtab()
        time.sleep(2)
        rcp.clickonthreedots()
        time.sleep(1)
        rcp.clickonpublish()
        rcp.publishconfirm()
        time.sleep(2)
        if "Employee Recognition has been published successfully" in driver.page_source:
            self.logger.info("********** Employee recognition published test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition published test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_UnpublishedtoPublishRecognition.png")
            assert False
        time.sleep(3)
        lp.clickLogout()
        time.sleep(2)
        lp.setUserName(self.username1)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in driver.page_source:
            self.logger.info("********** Employee verification test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee verification test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_UnpublishedtoPublishRecognition.png")
            assert False
        time.sleep(2)
        rcp.closepopup()
        time.sleep(1)
        lp.clickLogout()
        time.sleep(2)

    @pytest.mark.regression
    @pytest.mark.run(order=84)
    # @pytest.mark.skip(reason="skipping this Test")
    # @pytest.mark.skip(reason="skipping this Test")
    # @pytest.mark.pspk
    def test_EditRecognition(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(4)
        if "News Feed" in driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False
        rcp = Recognitions(driver)
        rcp.clickrecognition()
        if "Recognition" in driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False
        rcp.clicknewrecognition()
        time.sleep(2)
        rcp.selecttemplate()
        rcp.selectbadge()
        rcp.clicknext()
        time.sleep(2)
        rcp.setaddemployee(self.addemployee)
        rcp.clickemployee()
        rcp.setaddtitle(self.addtitle)
        rcp.setadddescription(self.adddescription)
        time.sleep(1)
        rcp.clickonpreview()
        time.sleep(1)
        rcp.savetemplate()
        time.sleep(2)
        if "Employee recognition has been saved in unpublished" in driver.page_source:
            self.logger.info("********** Employee recognition unpublished test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition unpublished test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_EditRecognition.png")
            assert False
        time.sleep(2)

        if "Anand" in driver.page_source:
            self.logger.info("********** Employee verification test is passed *********")
            self.logger.info("********** content creation test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee verification test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_EditRecognition.png")
            assert False
        time.sleep(3)
        lp.clickLogout()
        time.sleep(2)
        lp.setUserName(self.username1)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(3)
        if "News Feed" in driver.page_source:
            self.logger.info("********** Employee Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee Login failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "Employee_login_fail.png")
            assert False

        time.sleep(2)
        lp.clickLogout()
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(1)
        if "News Feed" in driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False
        rcp = Recognitions(driver)
        rcp.clickrecognition()
        time.sleep(2)
        if "Recognition" in driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False
        rcp.unpublishedtab()
        time.sleep(2)
        rcp.clickonthreedots()
        time.sleep(1)
        rcp.clickonedit()
        time.sleep(1)
        rcp.clcikonback()
        time.sleep(1)
        rcp.selecttemplatetwo()
        rcp.selectbannertwo()
        time.sleep(1)
        rcp.clicknext()
        time.sleep(1)
        rcp.clickonpreview()
        time.sleep(1)
        rcp.clickpublish()
        time.sleep(2)
        if "Employee recognition has been successfully published" in driver.page_source:
            self.logger.info("********** Employee recognition published test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition published test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_EditRecognition.png")
            assert False
        time.sleep(3)
        lp.clickLogout()
        time.sleep(2)
        lp.setUserName(self.username1)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in driver.page_source:
            self.logger.info("********** Employee verification test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** Employee verification test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_EditRecognition.png")
            assert False
        time.sleep(3)
        rcp.closepopup()
        time.sleep(3)
        lp.clickLogout()

    @pytest.mark.regression
    @pytest.mark.run(order=85)
    # @pytest.mark.skip(reason="skipping this Test")
    def test_CreateRecognition_Verify_Employee_got_Recognition_download_Recognition(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(4)
        if "News Feed" in driver.page_source:
            self.logger.info("********** OEM Company Login successfully *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** OEM Company Login failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "OEM_login_fail.png")
            assert False

        rcp = Recognitions(driver)
        rcp.clickrecognition()
        if "Recognition" in driver.page_source:
            self.logger.info("********** Recognition tab Open successfully and Published Recognitions open *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** Recognition tab Open failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "recognitiontab_open_fail.png")
            assert False

        rcp.clicknewrecognition()
        rcp.selecttemplate()
        rcp.selectbadge()
        rcp.clicknext()
        rcp.setaddemployee(self.addemployee)
        rcp.clickemployee()
        rcp.setaddtitle(self.addtitle)
        rcp.setadddescription(self.adddescription)
        rcp.clickonpreview()
        rcp.clickpublish()
        time.sleep(2)
        if "Employee recognition has been successfully published" in driver.page_source:
            self.logger.info("********** Employee recognition has been successfully published *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** Employee recognition Created fail **********")
            driver.save_screenshot(".\\Screenshots\\" + "employee_recognition.png")
            assert False

        lp.clickLogout()
        lp.setUserName(self.username1)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(4)
        if "Congratulations" in driver.page_source:
            self.logger.info("********** Employee verification test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** Employee verification test is failed **********")
            driver.save_screenshot(
                ".\\Screenshots\\" + "test_CreateRecognition_Verify_Employee_got_Recognition_download_Recognition.png")
            assert False

        rcp.closepopup()
        rcp.clickmyprofiletab()
        time.sleep(1)
        rcp.clickmyrecognition()
        rcp.clickbackrecog()
        rcp.clickdownloadrecog()
        rcp.selectdownloadtype()
        time.sleep(6)

    if __name__ == '__main__':
        unittest.main(verbosity=2)