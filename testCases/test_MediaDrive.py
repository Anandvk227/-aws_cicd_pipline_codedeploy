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



class TestMediaDrive(BaseClass):
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
    def test_MediaDrive(self):
        self.logger.info("****Started Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickNewsFeed()
        self.md = mediaDrivePage(self.driver)
        self.md.clickMediaDrive()

    @pytest.mark.regression
    # @pytest.mark.skip("created a common method")
    @pytest.mark.run(order=97)
    def test_MediaDriveVerify(self):
        self.test_MediaDrive()

        xpath = "//span[text()='There are no items']"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveVerify.png")
            assert False

    @pytest.mark.regression
    # @pytest.mark.skip
    @pytest.mark.run(order=98)
    def test_MediaDriveCreationAndUpload(self):
        self.test_MediaDrive()
        self.logger.info("****TC_02  verify New Button****")
        self.md.clickButtonNew()
        self.md.clickCreateFolder()
        self.md.setinputFolderName(self.first_name)
        self.md.clickbuttonCreate()
        xpath = "//div[contains(text(),'Folder created successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveCreationAndUpload.png")
            assert False

        self.md.clickClosetoaster()
            # File Upload
        self.md.clickButtonNew()
        self.logger.info("****TC_03  verify upload File ***")
        self.md.setUploadFiles(self.file_path)


        xpath_success_message = "//div[contains(text(),'File uploaded successfully')]"
        xpath_popup = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/p[@class='MuiTypography-root MuiDialogContentText-root MuiTypography-body1 MuiDialogContentText-root css-o3d33y']/div[@class='MuiFormControl-root css-13sljp9']/div[@role='radiogroup']/label[1]/span[1]"
        xpath_upload = "//button[normalize-space()='Upload']"

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_success_message))
            )
            self.logger.info(f"Text Found: {element.text}")
            assert True

        except TimeoutException:
            self.logger.info("Success Message Not Found")

            try:
                popup_element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_popup))
                )
                popup_element.click()
                popup_element1 = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_upload))
                )
                popup_element1.click()

                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_success_message))
                )
                self.logger.info(f"Text Found: {element.text}")
                assert True

            except TimeoutException:
                self.logger.info("Pop-up or Success Message Not Found")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveCreationAndUpload.png")
                assert False

        # Upload folder
        self.md.clickButtonNew()
        self.logger.info("****TC_03  verify upload folder***")
        self.md.setUploadFiles(self.folder_path)

        xpath_success_message = "//div[contains(text(),'File uploaded successfully')]"
        xpath_popup = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/p[@class='MuiTypography-root MuiDialogContentText-root MuiTypography-body1 MuiDialogContentText-root css-o3d33y']/div[@class='MuiFormControl-root css-13sljp9']/div[@role='radiogroup']/label[1]/span[1]"
        xpath_upload = "//button[normalize-space()='Upload']"

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_success_message))
            )
            self.logger.info(f"Text Found: {element.text}")
            assert True

        except TimeoutException:
            self.logger.info("Success Message Not Found")

            try:
                popup_element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_popup))
                )
                popup_element.click()
                popup_element1 = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_upload))
                )
                popup_element1.click()

                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_success_message))
                )
                self.logger.info(f"Text Found: {element.text}")
                assert True

            except TimeoutException:
                self.logger.info("Pop-up or Success Message Not Found")
                self.driver.save_screenshot(".\\ScreenShots\\" + "test_MediaDriveCreationAndUpload.png")
                assert False

    @pytest.mark.regression
    # @pytest.mark.test
    # @pytest.mark.flaky(rerun=3, rerun_delay=2)
    @pytest.mark.run(order=99)
    def test_MediaDriveSearchViewFilter(self):
        self.test_MediaDrive()
        self.md.clickButtonNew()
        self.md.clickCreateFolder()
        self.md.setinputFolderName(self.first_name1)
        self.md.clickbuttonCreate()
        xpath = "//div[contains(text(),'Folder created successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveSearchViewFilter.png")
            assert False

        self.md.clickClosetoaster()
        # File Upload
        self.md.clickButtonNew()

        self.md.setUploadFiles(self.file_path)

        xpath_success_message = "//div[contains(text(),'File uploaded successfully')]"
        xpath_popup = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/p[@class='MuiTypography-root MuiDialogContentText-root MuiTypography-body1 MuiDialogContentText-root css-o3d33y']/div[@class='MuiFormControl-root css-13sljp9']/div[@role='radiogroup']/label[1]/span[1]"
        xpath_upload = "//button[normalize-space()='Upload']"

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_success_message))
            )
            self.logger.info(f"Text Found: {element.text}")
            assert True

        except TimeoutException:
            self.logger.info("Success Message Not Found")

            try:
                popup_element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_popup))
                )
                popup_element.click()
                popup_element1 = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_upload))
                )
                popup_element1.click()

                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_success_message))
                )
                self.logger.info(f"Text Found: {element.text}")
                assert True

            except TimeoutException:
                self.logger.info("Pop-up or Success Message Not Found")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveSearchViewFilter.png")
                assert False


        self.md.clickClosetoaster()
        self.logger.info("TC_08	Verify the Search bar whith valid data")
        self.md.setSearchField(self.searchFile)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='"+self.searchFile+"']"))
        )
        element.click()
        self.md.ClickcloseFile()
        self.logger.info("TC_09	Verify the View Button To ensure that List view and Grid view is able to select")
        self.md.ClickViewMode()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.searchFile + "']"))
        )
        element.click()
        self.md.ClickcloseFile()
        self.logger.info("TC_10	Verify the Filter buttonTo ensure that Filter's List options able to select")
        self.md.ClickFilter()
        self.md.ClickAllCheckBox()
        self.md.setSearchField(self.first_name1)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.first_name1 + "']"))
        )
        element.click()
        self.driver.back()
        self.md.ClickFilter()
        self.md.ClickImagesCheckBox()
        self.md.setSearchField(self.first_name1)
        # time.sleep(5)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='No search results found']"))
        )

        # Assert the text
        assert element.text == 'No search results found', f"Expected 'No search results found' but found '{element.text}'"
        # time.sleep(4)

    @pytest.mark.regression
    # @pytest.mark.flaky(rerun=3, rerun_delay=2)
    @pytest.mark.test
    @pytest.mark.run(order=100)
    def test_MediaDriveshare(self):
        self.test_MediaDrive()
        self.md.clickButtonNew()
        self.md.clickCreateFolder()
        self.md.setinputFolderName(self.first_name2)
        self.md.clickbuttonCreate()
        xpath = "//div[contains(text(),'Folder created successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveshare.png")
            assert False
        time.sleep(1)
        self.md.clickClosetoaster()
        # File Upload
        self.md.clickButtonNew()

        self.md.setUploadFiles(self.file_path)

        xpath_success_message = "//div[contains(text(),'File uploaded successfully')]"
        xpath_popup = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/p[@class='MuiTypography-root MuiDialogContentText-root MuiTypography-body1 MuiDialogContentText-root css-o3d33y']/div[@class='MuiFormControl-root css-13sljp9']/div[@role='radiogroup']/label[1]/span[1]"
        xpath_upload = "//button[normalize-space()='Upload']"

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_success_message))
            )
            self.logger.info(f"Text Found: {element.text}")
            assert True

        except TimeoutException:
            self.logger.info("Success Message Not Found")

            try:
                popup_element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_popup))
                )
                popup_element.click()
                popup_element1 = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_upload))
                )
                popup_element1.click()

                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_success_message))
                )
                self.logger.info(f"Text Found: {element.text}")
                assert True

            except TimeoutException:
                self.logger.info("Pop-up or Success Message Not Found")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveshare.png")
                assert False

        self.md.setSearchField(self.first_name2)
        time.sleep(3)
        self.logger.info("***** TC_20 	Verify 'Share' option****")
        self.md.clickthreeDotsMenu()
        self.md.clickthreeDotsShare()
        self.md.clickdownArrow()
        time.sleep(3)
        self.md.clickEdit()
        xpath = "//div[contains(text(),'Access updated successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveshare.png")
            assert False

        self.lp.clickLogout()
        self.logger.info("****Started Login Test****")
        self.lp.setUserName(self.username2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickNewsFeed()
        self.md = mediaDrivePage(self.driver)
        self.md.clickMediaDrive()
        self.md.clickTabSharedWithMe()
        self.md.setTabSearch(self.first_name2)
        time.sleep(2)
        self.md.clickthreeDotsMenu()
        self.logger.info("*****TC_33	Verify 'Rename' option****")
        self.md.clickthreedotsRename()
        self.md.clickCancelRename()
        self.lp.clickLogout()
        self.logger.info("****Started Login Test****")
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickNewsFeed()
        self.md = mediaDrivePage(self.driver)
        self.md.clickMediaDrive()
        self.md.clickthreeDotsMenu()
        self.md.clickthreeDotsShare()
        self.logger.info("***TC_22	Verify the access dropdown for each individual network company****")
        self.md.clickdownArrow()
        self.logger.info("***TC_23	Verify the None, View and Edit options***")
        self.md.clickNone()
        self.md.clickDone()
        xpath = "//div[contains(text(),'Access updated successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveshare.png")
            assert False
        self.lp.clickLogout()
        self.logger.info("****Started Login Test****")
        self.lp.setUserName(self.username2)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickNewsFeed()
        self.md = mediaDrivePage(self.driver)
        self.md.clickMediaDrive()
        self.logger.info("****TC_50	Verify the Shared with me Tab****")
        self.md.clickTabSharedWithMe()
        # self.md.setTabSearch(self.first_name2)
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'There are no shared items')]"))
        )

        # Assert the text
        assert element.text == 'There are no shared items', f"Expected 'There are no shared items' but found '{element.text}'"

    @pytest.mark.regression
    # @pytest.mark.flaky(rerun=3, rerun_delay=2)
    # @pytest.mark.skip
    @pytest.mark.run(order=101)
    def test_MediaDriveMoveTo(self):
        self.test_MediaDrive()
        self.md.clickButtonNew()
        self.md.clickCreateFolder()
        self.md.setinputFolderName(self.first_name3)
        self.md.clickbuttonCreate()
        xpath = "//div[contains(text(),'Folder created successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveMoveTo.png")
            assert False

        self.md.clickClosetoaster()
        # File Upload
        self.md.clickButtonNew()

        self.md.setUploadFiles(self.file_path)

        xpath_success_message = "//div[contains(text(),'File uploaded successfully')]"
        xpath_popup = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/p[@class='MuiTypography-root MuiDialogContentText-root MuiTypography-body1 MuiDialogContentText-root css-o3d33y']/div[@class='MuiFormControl-root css-13sljp9']/div[@role='radiogroup']/label[1]/span[1]"
        xpath_upload = "//button[normalize-space()='Upload']"

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_success_message))
            )
            self.logger.info(f"Text Found: {element.text}")
            assert True

        except TimeoutException:
            self.logger.info("Success Message Not Found")

            try:
                popup_element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_popup))
                )
                popup_element.click()
                popup_element1 = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_upload))
                )
                popup_element1.click()

                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_success_message))
                )
                self.logger.info(f"Text Found: {element.text}")
                assert True

            except TimeoutException:
                self.logger.info("Pop-up or Success Message Not Found")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveMoveTo.png")
                assert False

        self.md.setSearchField(self.searchFile)
        time.sleep(2)
        self.md.clickthreeDotsMenu()
        self.logger.info("***TC_15	Verify the 'Move To' option***")
        self.md.clickMoveTothreeDots()
        self.md.setMoveToSearchInput(self.first_name3)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.first_name3 + "']"))
        )
        element.click()
        self.md.clickButtonMove()
        xpath = "//div[contains(text(),'Folder moved successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveMoveTo.png")
            assert False
        # self.md.clickClosetoaster()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.first_name3 + "']"))
        )
        element.click()
        self.md.setSearchField(self.searchFile)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.searchFile + "']"))
        )
        element.click()
        self.md.clickClosetoaster()
        self.md.ClickcloseFile()

    @pytest.mark.regression
    # @pytest.mark.test
    # @pytest.mark.flaky(rerun=3, rerun_delay=2)
    @pytest.mark.run(order=102)
    def test_MediaDriveEditZipDownloadTrash(self):
        self.test_MediaDrive()
        self.md.setSearchField(self.searchFile)
        time.sleep(2)
        self.md.clickthreeDotsMenu()
        self.md.clickthreeDotsEdit()
        self.md.clickContinueButton()
        self.md.clickUploadLogo()
        # when there are no other folders present
        # self.md.clickFileMediakit()
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//div[@class='flexCol fullHeight pdngXS'])[3]"))
        # )
        # element.click()
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.searchFile + "']"))
        # )
        # element.click()
        #
        # self.md.clicksubmitButton()

        # running with choosing file from system
        self.md.setchooseFromSystem(self.file_path)
        self.md.clickCropSaveButton()

        self.md.clickUploadLogo2()
        self.md.setchooseFromSystem(self.file_path)
        self.md.clickCropSaveButton()
        self.md.clickPreviewButton()
        self.md.clickDownloadButton()
        self.md.clickSaveButton()
        self.md.setEnterFileName(self.first_name4)
        self.md.clickFileSaveButton()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.first_name4 + "']"))
        )
        element.click()
        self.md.clickButtonPreviewZip()
        xpath = "//div[contains(text(),'File/Folder converted to zip')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveEditZipDownloadTrash.png")
            assert False
        self.md.clickClosetoaster()
        self.md.ClickcloseFile()
        self.md.setSearchField(self.first_name4+".zip")
        time.sleep(2)
        self.md.clickthreeDotsMenu()
        self.md.ClickMoveToTrash()
        self.md.ClickconfTrash()
        xpath = "//div[contains(text(),'File/Folder moved to trash')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveEditZipDownloadTrash.png")
            assert False

    @pytest.mark.regression
    # @pytest.mark.skip
    # @pytest.mark.flaky(rerun=3, rerun_delay=2)
    # @pytest.mark.test
    @pytest.mark.run(order=103)
    def test_MediaDriveTrashRestoreAndDelete(self):
        self.test_MediaDrive()
        self.md.clickButtonNew()
        self.md.clickCreateFolder()
        self.md.setinputFolderName(self.first_name5)
        self.md.clickbuttonCreate()
        xpath = "//div[contains(text(),'Folder created successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashRestoreAndDelete.png")
            assert False

        self.md.setSearchField(self.first_name5)
        time.sleep(2)
        self.md.clickthreeDotsMenu()
        self.md.ClickMoveToTrash()
        self.md.ClickconfTrash()
        xpath = "//div[contains(text(),'File/Folder moved to trash')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashRestoreAndDelete.png")
            assert False
        self.md.clickClosetoaster()
        self.md.clickTabTrash()
        self.md.setSearchField(self.first_name5)
        time.sleep(2)
        self.md.clickthreeDotsMenu()
        self.md.clickTrashRestore()
        self.md.clickTrashConfRestore()
        xpath = "//div[contains(text(),'File/Folder Restored Successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashRestoreAndDelete.png")
            assert False

        self.md.clickTabMyFiles()

        self.md.setSearchField(self.first_name5)
        time.sleep(2)
        self.md.clickthreeDotsMenu()
        self.md.ClickMoveToTrash()
        self.md.ClickconfTrash()
        xpath = "//div[contains(text(),'File/Folder moved to trash')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashRestoreAndDelete.png")
            assert False
        self.md.clickClosetoaster()
        self.md.clickTabTrash()
        self.md.setSearchField(self.first_name5)
        time.sleep(2)
        self.md.clickthreeDotsMenu()
        self.md.clickTrash3dotsDelete()
        self.md.clickTrashConfDelete()

        xpath = "//div[contains(text(),'Folder/File Permanently Deleted. Cannot be recover')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashRestoreAndDelete.png")
            assert False


    @pytest.mark.regression
    # @pytest.mark.skip
    # @pytest.mark.flaky(rerun=3, rerun_delay=2)
    # @pytest.mark.test
    @pytest.mark.run(order=104)
    def test_MediaDriveTrashAll(self):
        self.test_MediaDrive()
        self.md.clickSelectAllCheckBox()
        self.md.clickTrashAll()
        self.md.ClickconfTrash()
        xpath = "//div[contains(text(),'File/Folder moved to trash')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashAll.png")
            assert False
        self.md.clickTabTrash()
        self.md.clickSelectAllCheckBox()

        self.md.clickDeleteAll()
        self.md.clickAllConfDelete()

        xpath = "//div[contains(text(),'Folder/File Permanently Deleted. Cannot be recover')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveTrashAll.png")
            assert False

    # @pytest.mark.test
    @pytest.mark.run(order=105)
    def test_MediaDriveEmployeeCreateMedia(self):
        self.logger.info("****Started Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.EmpEmail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.md = mediaDrivePage(self.driver)
        self.md.clickMediaDrive()
        self.md.clickButtonNew()
        self.md.clickCreateFolder()
        self.md.setinputFolderName(self.first_name1)
        self.md.clickbuttonCreate()
        xpath = "//div[contains(text(),'Folder created successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveEmployeeCreateMedia.png")
            assert False

        self.md.clickClosetoaster()

        self.md.setSearchField(self.first_name1)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.first_name1 + "']"))
        )
        element.click()

        # File Upload
        self.md.clickButtonNew()

        self.md.setUploadFiles(self.file_path)

        xpath_success_message = "//div[contains(text(),'File uploaded successfully')]"
        xpath_popup = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-1ty026z']/p[@class='MuiTypography-root MuiDialogContentText-root MuiTypography-body1 MuiDialogContentText-root css-o3d33y']/div[@class='MuiFormControl-root css-13sljp9']/div[@role='radiogroup']/label[1]/span[1]"
        xpath_upload = "//button[normalize-space()='Upload']"

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath_success_message))
            )
            self.logger.info(f"Text Found: {element.text}")
            assert True

        except TimeoutException:
            self.logger.info("Success Message Not Found")

            try:
                popup_element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_popup))
                )
                popup_element.click()
                popup_element1 = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, xpath_upload))
                )
                popup_element1.click()

                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath_success_message))
                )
                self.logger.info(f"Text Found: {element.text}")
                assert True

            except TimeoutException:
                self.logger.info("Pop-up or Success Message Not Found")
                self.driver.save_screenshot(".\\Screenshots\\" + "test_MediaDriveEmployeeCreateMedia.png")
                assert False


    @pytest.mark.tests
    @pytest.mark.run(order=106)
    def test_TrashEmployeeMedia(self):
        self.test_MediaDrive()
        self.md.clickTabEmployee()
        self.md.setSearchField(self.EmpName2)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.EmpName2 + "']"))
        )
        element.click()
        self.md.setSearchField(self.first_name1)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.first_name1 + "']"))
        )
        element.click()
        self.md.setSearchField(self.searchFile)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='" + self.searchFile + "']"))
        )
        element.click()
        self.md.ClickcloseFile()
        self.md.clickonMainFile()
        self.md.clickDeleteEmpFolder()
        self.md.ClickconfTrash()
        xpath = "//div[contains(text(),'File/Folder moved to trash')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TrashEmployeeMedia.png")
            assert False

        self.lp.clickLogout()
        self.logger.info("****Started Login Test****")
        self.lp.setUserName(self.EmpEmail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.md = mediaDrivePage(self.driver)
        self.md.clickMediaDrive()
        xpath = "//span[text()='There are no items']"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_TrashEmployeeMedia.png")
            assert False


if __name__ == "__main__":
    unittest.main()
