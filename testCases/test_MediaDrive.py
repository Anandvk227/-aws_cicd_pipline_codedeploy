import os
import time
import unittest
import pytest
from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.randomGen import randomGen
from pageObjects.LoginPage import LoginPage
from pageObjects.mediaDrivePage import mediaDrivePage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from GenericLib.BaseClass import BaseClass



class TestMediaDrive():
    baseURL = ReadConfig.getApplicationURL()
    first_name = randomGen.random_first_name()
    first_name1 = randomGen.random_first_name()
    first_name2 = randomGen.random_first_name()
    first_name3 = randomGen.random_first_name()
    first_name4 = randomGen.random_first_name()
    first_name5 = randomGen.random_first_name()
    file_name = "Files/five.png"
    searchFile = "five.png"
    file_path = os.path.abspath(os.path.join(os.getcwd(), file_name))
    folder_name = "Reports"
    folder_path = os.path.abspath(os.path.join(os.getcwd(), folder_name))

    workbook = load_workbook("TestData/LoginData.xlsx")
    worksheet = workbook.active
    username = worksheet["A2"].value
    username2 = worksheet["I2"].value
    EmpName = worksheet["C6"].value
    EmpEmail = worksheet["B6"].value
    EmpName2 = worksheet["A6"].value

    password = ReadConfig.getPassword()
    workbook.close()

    logger = LogGen.loggen()

    @pytest.mark.regression
    # @pytest.mark.tests
    # @pytest.mark.skip("created a common method")
    @pytest.mark.run(order=96)
    def test_MediaDrive(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        md = mediaDrivePage(driver)
        md.clickMediaDrive()

    @pytest.mark.regression
    # @pytest.mark.skip("created a common method")
    @pytest.mark.run(order=97)
    def test_MediaDriveVerify(self, driver):
        self.test_MediaDrive(driver)

        xpath = "//span[text()='There are no items']"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveVerify.png")
            assert False

    @pytest.mark.regression
    # @pytest.mark.skip
    @pytest.mark.run(order=98)
    def test_MediaDriveCreationAndUpload(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started Media Drive Test****")
        self.test_MediaDrive(driver)
        self.logger.info("****TC_02  verify New Button****")
        md = mediaDrivePage(driver)
        md.clickButtonNew()
        md.clickCreateFolder()
        md.setinputFolderName(self.first_name)
        md.clickbuttonCreate()

        xpath = "//div[contains(text(),'Folder created successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveCreationAndUpload.png")
            assert False

        md.clickClosetoaster()
        # File Upload
        md.clickButtonNew()
        self.logger.info("****TC_03  verify upload File ***")
        md.setUploadFiles(self.file_path)

        xpath_success_message = "//div[contains(text(),'File uploaded successfully')]"
        xpath_popup = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/p[@class='MuiTypography-root MuiDialogContentText-root MuiTypography-body1 MuiDialogContentText-root css-o3d33y']/div[@class='MuiFormControl-root css-13sljp9']/div[@role='radiogroup']/label[1]/span[1]"
        xpath_upload = "//button[normalize-space()='Upload']"

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_success_message))
            )
            self.logger.info(f"Text Found: {element.text}")
            assert True

        except TimeoutException:
            self.logger.info("Success Message Not Found")

            try:
                popup_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_popup))
                )
                popup_element.click()
                popup_element1 = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_upload))
                )
                popup_element1.click()

                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_success_message))
                )
                self.logger.info(f"Text Found: {element.text}")
                assert True

            except TimeoutException:
                self.logger.info("Pop-up or Success Message Not Found")
                driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveCreationAndUpload.png")
                assert False

        # Upload folder
        md.clickButtonNew()
        self.logger.info("****TC_03  verify upload folder***")
        md.setUploadFiles(self.folder_path)

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_success_message))
            )
            self.logger.info(f"Text Found: {element.text}")
            assert True

        except TimeoutException:
            self.logger.info("Success Message Not Found")

            try:
                popup_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_popup))
                )
                popup_element.click()
                popup_element1 = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_upload))
                )
                popup_element1.click()

                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_success_message))
                )
                self.logger.info(f"Text Found: {element.text}")
                assert True

            except TimeoutException:
                self.logger.info("Pop-up or Success Message Not Found")
                driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveCreationAndUpload.png")
                assert False

    @pytest.mark.regression
    # @pytest.mark.test
    # @pytest.mark.flaky(rerun=3, rerun_delay=2)
    @pytest.mark.run(order=99)
    def test_MediaDriveSearchViewFilter(self, driver):
        driver.maximize_window()
        self.logger.info("****Starting MediaDriveSearchViewFilter Test****")
        self.test_MediaDrive(driver)
        md = mediaDrivePage(driver)
        md.clickButtonNew()
        md.clickCreateFolder()
        md.setinputFolderName(self.first_name1)
        md.clickbuttonCreate()
        xpath = "//div[contains(text(),'Folder created successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveSearchViewFilter.png")
            assert False

        md.clickClosetoaster()
        # File Upload
        md.clickButtonNew()
        md.setUploadFiles(self.file_path)

        xpath_success_message = "//div[contains(text(),'File uploaded successfully')]"
        xpath_popup = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/p[@class='MuiTypography-root MuiDialogContentText-root MuiTypography-body1 MuiDialogContentText-root css-o3d33y']/div[@class='MuiFormControl-root css-13sljp9']/div[@role='radiogroup']/label[1]/span[1]"
        xpath_upload = "//button[normalize-space()='Upload']"

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_success_message))
            )
            self.logger.info(f"Text Found: {element.text}")
            assert True
        except TimeoutException:
            self.logger.info("Success Message Not Found")
            try:
                popup_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_popup))
                )
                popup_element.click()
                popup_element1 = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_upload))
                )
                popup_element1.click()
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_success_message))
                )
                self.logger.info(f"Text Found: {element.text}")
                assert True
            except TimeoutException:
                self.logger.info("Pop-up or Success Message Not Found")
                driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveSearchViewFilter.png")
                assert False

        md.clickClosetoaster()
        self.logger.info("TC_08	Verify the Search bar whith valid data")
        md.setSearchField(self.searchFile)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.searchFile + "']"))
        )
        element.click()
        md.ClickcloseFile()
        self.logger.info("TC_09	Verify the View Button To ensure that List view and Grid view is able to select")
        md.ClickViewMode()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.searchFile + "']"))
        )
        element.click()
        md.ClickcloseFile()
        self.logger.info("TC_10	Verify the Filter buttonTo ensure that Filter's List options able to select")
        md.ClickFilter()
        md.ClickAllCheckBox()
        md.setSearchField(self.first_name1)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.first_name1 + "']"))
        )
        element.click()
        driver.back()
        md.ClickFilter()
        md.ClickImagesCheckBox()
        md.setSearchField(self.first_name1)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='No search results found']"))
        )

        # Assert the text
        assert element.text == 'No search results found', f"Expected 'No search results found' but found '{element.text}'"

    @pytest.mark.regression
    # @pytest.mark.flaky(rerun=3, rerun_delay=2)
    @pytest.mark.test
    @pytest.mark.run(order=100)
    def test_MediaDriveshare(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.test_MediaDrive(driver)
        md = mediaDrivePage(driver)
        md.clickButtonNew()
        md.clickCreateFolder()
        md.setinputFolderName(self.first_name2)
        md.clickbuttonCreate()
        xpath = "//div[contains(text(),'Folder created successfully')]"
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveshare.png")
            assert False
        time.sleep(1)
        md.clickClosetoaster()
        # File Upload
        md.clickButtonNew()
        md.setUploadFiles(self.file_path)

        xpath_success_message = "//div[contains(text(),'File uploaded successfully')]"
        xpath_popup = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/p[@class='MuiTypography-root MuiDialogContentText-root MuiTypography-body1 MuiDialogContentText-root css-o3d33y']/div[@class='MuiFormControl-root css-13sljp9']/div[@role='radiogroup']/label[1]/span[1]"
        xpath_upload = "//button[normalize-space()='Upload']"

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_success_message))
            )
            self.logger.info(f"Text Found: {element.text}")
            assert True

        except TimeoutException:
            self.logger.info("Success Message Not Found")

            try:
                popup_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_popup))
                )
                popup_element.click()
                popup_element1 = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_upload))
                )
                popup_element1.click()

                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_success_message))
                )
                self.logger.info(f"Text Found: {element.text}")
                assert True

            except TimeoutException:
                self.logger.info("Pop-up or Success Message Not Found")
                driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveshare.png")
                assert False

        md.setSearchField(self.first_name2)
        time.sleep(3)
        self.logger.info("***** TC_20 	Verify 'Share' option****")
        md.clickthreeDotsMenu()
        md.clickthreeDotsShare()
        md.clickdownArrow()
        time.sleep(3)
        md.clickEdit()
        xpath = "//div[contains(text(),'Access updated successfully')]"
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveshare.png")
            assert False

        lp = LoginPage(driver)
        lp.clickLogout()
        self.logger.info("****Started Login Test****")
        lp.setUserName(self.username2)
        lp.setPassword(self.password)
        lp.clickLogin()
        lp.clickNewsFeed()
        md = mediaDrivePage(driver)
        md.clickMediaDrive()
        md.clickTabSharedWithMe()
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'There are no shared items')]"))
        )

        # Assert the text
        assert element.text == 'There are no shared items', f"Expected 'There are no shared items' but found '{element.text}'"

    @pytest.mark.regression
    # @pytest.mark.flaky(rerun=3, rerun_delay=2)
    # @pytest.mark.skip
    @pytest.mark.run(order=101)
    def test_MediaDriveMoveTo(self, driver):
        self.test_MediaDrive(driver)
        md = mediaDrivePage(driver)
        md.clickButtonNew()
        md.clickCreateFolder()
        md.setinputFolderName(self.first_name3)
        md.clickbuttonCreate()
        xpath = "//div[contains(text(),'Folder created successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveMoveTo.png")
            assert False

        md.clickClosetoaster()
        # File Upload
        md.clickButtonNew()
        md.setUploadFiles(self.file_path)
        xpath_success_message = "//div[contains(text(),'File uploaded successfully')]"
        xpath_popup = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/p[@class='MuiTypography-root MuiDialogContentText-root MuiTypography-body1 MuiDialogContentText-root css-o3d33y']/div[@class='MuiFormControl-root css-13sljp9']/div[@role='radiogroup']/label[1]/span[1]"
        xpath_upload = "//button[normalize-space()='Upload']"

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_success_message))
            )
            self.logger.info(f"Text Found: {element.text}")
            assert True
        except TimeoutException:
            self.logger.info("Success Message Not Found")

            try:
                popup_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_popup))
                )
                popup_element.click()
                popup_element1 = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_upload))
                )
                popup_element1.click()

                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_success_message))
                )
                self.logger.info(f"Text Found: {element.text}")
                assert True
            except TimeoutException:
                self.logger.info("Pop-up or Success Message Not Found")
                driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveMoveTo.png")
                assert False

        md.setSearchField(self.searchFile)
        time.sleep(2)
        md.clickthreeDotsMenu()
        self.logger.info("***TC_15	Verify the 'Move To' option***")
        md.clickMoveTothreeDots()
        md.setMoveToSearchInput(self.first_name3)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.first_name3 + "']"))
        )
        element.click()
        md.clickButtonMove()
        xpath = "//div[contains(text(),'Folder moved successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveMoveTo.png")
            assert False
        # md.clickClosetoaster()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.first_name3 + "']"))
        )
        element.click()
        md.setSearchField(self.searchFile)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.searchFile + "']"))
        )
        element.click()
        md.clickClosetoaster()
        md.ClickcloseFile()

    @pytest.mark.regression
    # @pytest.mark.test
    # @pytest.mark.flaky(rerun=3, rerun_delay=2)
    @pytest.mark.run(order=102)
    def test_MediaDriveEditZipDownloadTrash(self, driver):
        self.test_MediaDrive(driver)
        md = mediaDrivePage(driver)
        md.setSearchField(self.searchFile)
        time.sleep(2)
        md.clickthreeDotsMenu()
        md.clickthreeDotsEdit()
        md.clickContinueButton()
        md.clickUploadLogo()
        # when there are no other folders present
        # md.clickFileMediakit()
        # element = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//div[@class='flexCol fullHeight pdngXS'])[3]"))
        # )
        # element.click()
        # element = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.searchFile + "']"))
        # )
        # element.click()
        #
        # md.clicksubmitButton()

        # running with choosing file from system
        md.setchooseFromSystem(self.file_path)
        md.clickCropSaveButton()

        md.clickUploadLogo2()
        md.setchooseFromSystem(self.file_path)
        md.clickCropSaveButton()
        md.clickPreviewButton()
        md.clickDownloadButton()
        md.clickSaveButton()
        md.setEnterFileName(self.first_name4)
        md.clickFileSaveButton()
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.first_name4 + "']"))
        )
        element.click()
        md.clickButtonPreviewZip()
        xpath = "//div[contains(text(),'File/Folder converted to zip')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveEditZipDownloadTrash.png")
            assert False
        md.clickClosetoaster()
        md.ClickcloseFile()
        md.setSearchField(self.first_name4 + ".zip")
        time.sleep(2)
        md.clickthreeDotsMenu()
        md.ClickMoveToTrash()
        md.ClickconfTrash()
        xpath = "//div[contains(text(),'File/Folder moved to trash')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveEditZipDownloadTrash.png")
            assert False

    @pytest.mark.regression
    # @pytest.mark.skip
    # @pytest.mark.flaky(rerun=3, rerun_delay=2)
    # @pytest.mark.test
    @pytest.mark.run(order=103)
    def test_MediaDriveTrashRestoreAndDelete(self, driver):
        driver.maximize_window()
        self.logger.info("****Started MediaDriveTrashRestoreAndDelete Test****")
        self.test_MediaDrive(driver)
        md = mediaDrivePage(driver)

        # Create a new folder
        md.clickButtonNew()
        md.clickCreateFolder()
        md.setinputFolderName(self.first_name5)
        md.clickbuttonCreate()
        xpath = "//div[contains(text(),'Folder created successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashRestoreAndDelete.png")
            assert False

        # Move folder to trash
        md.setSearchField(self.first_name5)
        time.sleep(2)
        md.clickthreeDotsMenu()
        md.ClickMoveToTrash()
        md.ClickconfTrash()
        xpath = "//div[contains(text(),'File/Folder moved to trash')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashRestoreAndDelete.png")
            assert False

        md.clickClosetoaster()
        md.clickTabTrash()
        md.setSearchField(self.first_name5)
        time.sleep(2)
        md.clickthreeDotsMenu()
        md.clickTrashRestore()
        md.clickTrashConfRestore()
        xpath = "//div[contains(text(),'File/Folder Restored Successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashRestoreAndDelete.png")
            assert False

        md.clickTabMyFiles()

        # Move folder to trash again
        md.setSearchField(self.first_name5)
        time.sleep(2)
        md.clickthreeDotsMenu()
        md.ClickMoveToTrash()
        md.ClickconfTrash()
        xpath = "//div[contains(text(),'File/Folder moved to trash')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashRestoreAndDelete.png")
            assert False

        md.clickClosetoaster()
        md.clickTabTrash()
        md.setSearchField(self.first_name5)
        time.sleep(2)
        md.clickthreeDotsMenu()
        md.clickTrash3dotsDelete()
        md.clickTrashConfDelete()

        xpath = "//div[contains(text(),'Folder/File Permanently Deleted. Cannot be recover')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashRestoreAndDelete.png")
            assert False

    @pytest.mark.regression
    # @pytest.mark.skip
    # @pytest.mark.flaky(rerun=3, rerun_delay=2)
    # @pytest.mark.test
    @pytest.mark.run(order=104)
    def test_MediaDriveTrashAll(self, driver):
        self.test_MediaDrive(driver)
        md = mediaDrivePage(driver)
        md.clickSelectAllCheckBox()
        md.clickTrashAll()
        md.ClickconfTrash()
        xpath = "//div[contains(text(),'File/Folder moved to trash')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashAll.png")
            assert False
        md.clickTabTrash()
        md.clickSelectAllCheckBox()

        md.clickDeleteAll()
        md.clickAllConfDelete()

        xpath = "//div[contains(text(),'Folder/File Permanently Deleted. Cannot be recover')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashAll.png")
            assert False

    # @pytest.mark.test
    @pytest.mark.run(order=105)
    def test_MediaDriveEmployeeCreateMedia(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Started Login Test****")
        lp = LoginPage(driver)
        lp.setUserName(self.EmpEmail)
        lp.setPassword(self.password)
        lp.clickLogin()
        md = mediaDrivePage(driver)
        md.clickMediaDrive()
        md.clickButtonNew()
        md.clickCreateFolder()
        md.setinputFolderName(self.first_name1)
        md.clickbuttonCreate()
        xpath = "//div[contains(text(),'Folder created successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveEmployeeCreateMedia.png")
            assert False

        md.clickClosetoaster()

        md.setSearchField(self.first_name1)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.first_name1 + "']"))
        )
        element.click()

        # File Upload
        md.clickButtonNew()

        md.setUploadFiles(self.file_path)

        xpath_success_message = "//div[contains(text(),'File uploaded successfully')]"
        xpath_popup = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/p[@class='MuiTypography-root MuiDialogContentText-root MuiTypography-body1 MuiDialogContentText-root css-o3d33y']/div[@class='MuiFormControl-root css-13sljp9']/div[@role='radiogroup']/label[1]/span[1]"
        xpath_upload = "//button[normalize-space()='Upload']"

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_success_message))
            )
            self.logger.info(f"Text Found: {element.text}")
            assert True

        except TimeoutException:
            self.logger.info("Success Message Not Found")

            try:
                popup_element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_popup))
                )
                popup_element.click()
                popup_element1 = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_upload))
                )
                popup_element1.click()

                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_success_message))
                )
                self.logger.info(f"Text Found: {element.text}")
                assert True

            except TimeoutException:
                self.logger.info("Pop-up or Success Message Not Found")
                driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveEmployeeCreateMedia.png")
                assert False

    @pytest.mark.tests
    @pytest.mark.run(order=106)
    def test_TrashEmployeeMedia(self, driver):
        self.test_MediaDrive(driver)
        md = mediaDrivePage(driver)
        md.clickTabEmployee()
        md.setSearchField(self.EmpName2)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.EmpName2 + "']"))
        )
        element.click()
        md.setSearchField(self.first_name1)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.first_name1 + "']"))
        )
        element.click()
        md.setSearchField(self.searchFile)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.searchFile + "']"))
        )
        element.click()
        md.ClickcloseFile()
        md.clickonMainFile()
        md.clickDeleteEmpFolder()
        md.ClickconfTrash()
        xpath = "//div[contains(text(),'File/Folder moved to trash')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_TrashEmployeeMedia.png")
            assert False

        lp = LoginPage(driver)
        lp.clickLogout()
        self.logger.info("****Started Login Test****")
        lp.setUserName(self.EmpEmail)
        lp.setPassword(self.password)
        lp.clickLogin()
        md = mediaDrivePage(driver)
        md.clickMediaDrive()
        xpath = "//span[text()='There are no items']"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_TrashEmployeeMedia.png")
            assert False


if __name__ == "__main__":
    unittest.main()
