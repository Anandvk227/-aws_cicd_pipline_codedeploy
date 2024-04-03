import os
import unittest
import pytest

import time
from openpyxl.reader.excel import load_workbook
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from krishnapageObjects.NewsfeedPage import NewsFeed
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from GenericLib.BaseClass import BaseClass

class TestNewsFeed():
    baseURL = ReadConfig.getApplicationURL()
    # username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    whats = ReadConfig.getwhats()
    whatso = ReadConfig.getwhatso()
    # usernames = ReadConfig.getuseremails()
    # usernames1 = ReadConfig.getuseremails1()
    # usernames2 = ReadConfig.getuseremails2()
    # usernames3 = ReadConfig.getuseremails3()
    whatson = ReadConfig.getwhatson()
    oneimage = ReadConfig.getoneimage()
    fiveimages = ReadConfig.getfiveimages()

    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active

    username = worksheet["A2"].value
    usernames = worksheet["B6"].value
    usernames1 = worksheet["I2"].value
    usernames2 = worksheet["I3"].value
    usernames3 = worksheet["D6"].value

    workbook.close()


    relative_one = "Files/one.png"
    absolute_path1 = os.path.abspath(relative_one)
    relative_two = "Files/two.png"
    absolute_path2 = os.path.abspath(relative_two)
    relative_three = "Files/three.png"
    absolute_path3 = os.path.abspath(relative_three)
    relative_four = "Files/four.png"
    absolute_path4 = os.path.abspath(relative_four)
    relative_five = "Files/five.png"
    absolute_path5 = os.path.abspath(relative_five)
    relative_six = "Files/six.jpg"
    absolute_path6 = os.path.abspath(relative_six)
    relative_video1 = "Files/video1.mp4"
    absolute_pathvideo1 = os.path.abspath(relative_video1)
    whatvideo = ReadConfig.getwhatvideo()
    relative_video2 = "Files/video2.mp4"
    absolute_pathvideo2 = os.path.abspath(relative_video2)
    whatvideos = ReadConfig.getwhatvideos()
    whatyoutube = ReadConfig.getwhatyoutube()
    youtubeurl = ReadConfig.getyoutubeurl()
    whatedit = ReadConfig.getwhatedit()
    commenttext = "hiii gud mrng"
    replytext = "gudmorning all"
    commentedittext = "all "
    search = "hii,all employees and relation companies"

    logger = LogGen.loggen()  # Logger


    @pytest.mark.tests
    @pytest.mark.regression
    @pytest.mark.run(order=43)
    # @pytest.mark.flaky(reruns=3,reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforemployees(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_001_NewsFeed **********")
        self.logger.info("************** TC_01 Create a feed with text content.  **************")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhats(self.whats)
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf.clickonlogout()
        self.logger.info("************* Logout successful **********")
        lp.setUserName(self.usernames)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* EmpLogin successful **********")
        if "Hi,gud mrng employees" in driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedverification.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=44)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforempndrel(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_002_NewsFeed **********")
        self.logger.info("********** TC_20 Create a feed with Public enabled. *******")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhatso(self.whatso)
        nf.clickonpublic()
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf.clickonlogout()
        self.logger.info("************* Logout successful **********")
        lp.setUserName(self.usernames1)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relation company Login successful **********")
        if "hii,all employees and relation companies" in driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedforempndrel.png")
            assert False

    @pytest.mark.test
    @pytest.mark.regression
    @pytest.mark.run(order=45)
    # @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforpartners(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_003_NewsFeed **********")
        self.logger.info(
            "************* TC_21 Create a feed with Public disabled (default) and Partners checkbox selected.*************")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhatson(self.whatson)
        nf.clickonemp()
        nf.clickonpartner()
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf.clickonlogout()
        self.logger.info("************* Logout successful **********")
        lp.setUserName(self.usernames2)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* partnerLogin successful **********")
        if "hii,all partners schedule the meeting" in driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedforpartners.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=46)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforarchived(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_004_NewsFeed **********")
        self.logger.info("************ TC_22 Create a feed with Status disabled **********")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")
        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhats(self.whats)
        nf.clickonstatus()
        nf.clickonpost()
        time.sleep(3)
        if "Post created and saved in archived list" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf.clickonthreedots()
        nf.clickonarchive()
        time.sleep(3)
        if "Hi,gud mrng employees" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedforarchived.png")
            assert False

    @pytest.mark.image
    @pytest.mark.regression
    @pytest.mark.run(order=47)
    # @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedwithimage(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_005_NewsFeed **********")
        self.logger.info("*************** Test_06 Create a feed with text and upload 1 image.   **********")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setoneimage(self.oneimage)
        # nf.setgallery(self.absolute_path1)
        nf.imageicon()
        nf.uploadimage(self.absolute_path1)
        # nf.uploadimage(self.relative_one)
        # nf.clickuploadimage()
        nf.AddClick()
        # nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        # nf.clickonlogout()
        # self.logger.info("************* Logout successful **********")
        # lp.setUserName(self.usernames)
        # lp.setPassword(self.password)
        # lp.clickLogin()
        # self.logger.info("************* EmpLogin successful **********")
        # time.sleep(3)
        # if "one image upload" in driver.page_source:
        #     self.logger.info("***************Newsfeed test is passed **********")
        #     # driver.close()
        #
        # else:
        #     self.logger.error("************* NewsFeed test is failed **********")
        #     driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedwithimage.png")
        #     assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=48)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedwith5images(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_006_NewsFeed **********")
        self.logger.info("*********** TC_05 Create a feed with text and image uploads (up to 5 images). **************")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setfiveimages(self.fiveimages)
        nf.setgallery(self.absolute_path1)
        nf.setgallery(self.absolute_path2)
        nf.setgallery(self.absolute_path3)
        nf.setgallery(self.absolute_path4)
        nf.setgallery(self.absolute_path5)
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        nf.clickonlogout()
        self.logger.info("************* Logout successful **********")
        lp.setUserName(self.usernames)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* EmpLogin successful **********")
        nf.clickonimage()
        time.sleep(3)
        if "five images upload" in driver.page_source:
            self.logger.info("*************** Newsfeed test is passed **********")
            # self.driver.close()

        else:
            self.logger.error("************* NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedwith5images.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=49)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedwith6images(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_007_NewsFeed **********")
        self.logger.info("************* Tc_07 Attempt to create a feed with text and upload 6 images.************")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setgallery(self.absolute_path1)
        nf.setgallery(self.absolute_path2)
        nf.setgallery(self.absolute_path3)
        nf.setgallery(self.absolute_path4)
        nf.setgallery(self.absolute_path5)
        nf.setgallery(self.absolute_path6)
        # nf.clickonpost()
        time.sleep(3)
        if "Cannot upload more than 5 images" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
            # driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedwith6images.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=50)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedwithimages(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_008_NewsFeed **********")
        self.logger.info("************* TC_08 Create a feed with only image uploads (no text).")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")
        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setfiveimages(self.fiveimages)
        nf.setgallery(self.absolute_path1)
        nf.setgallery(self.absolute_path2)
        nf.setgallery(self.absolute_path3)
        nf.setgallery(self.absolute_path4)
        nf.setgallery(self.absolute_path5)
        nf.clickonpublic()
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        nf.clickonlogout()
        self.logger.info("************* Logout successful **********")
        lp.setUserName(self.usernames1)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* EmpLogin successful **********")
        nf.clickonimage()
        time.sleep(3)
        if "five images upload" in driver.page_source:
            self.logger.info("*************** Newsfeed test is passed **********")
            # driver.close()

        else:
            self.logger.error("************* NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedwithimages.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=51)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforemployeesvideo(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_009_NewsFeed **********")
        self.logger.info("************* TC_09 Create a feed with text and upload video. ************")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhats(self.whatvideo)
        nf.setvideo(self.absolute_pathvideo1)
        time.sleep(3)
        # nf.clickonpost()
        if "Cannot upload greater than 20MB" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
            # driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedforemployeesvideo.png")
            assert False

    @pytest.mark.test
    @pytest.mark.regression
    @pytest.mark.run(order=52)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforemployeesvideos(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_010_NewsFeed **********")
        self.logger.info(
            "*************** TC_10 Attempt to create a feed with text and upload more than 20mb video. ************")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhats(self.whatvideos)
        nf.setvideo(self.absolute_pathvideo2)
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf.clickonlogout()
        self.logger.info("************* Logout successful **********")
        lp.setUserName(self.usernames)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* EmpLogin successful **********")
        if "uploading videos" in driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedforemployeesvideos.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=53)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_newsfeedforempndrelvideo(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_011_NewsFeed **********")
        self.logger.info("*********** TC_13 Create a feed with text and upload one YouTube URL. ***********")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhatyoutube(self.whatyoutube)
        nf.clickonpublic()
        nf.clickonyoutube()
        nf.setyoutubeurl(self.youtubeurl)
        nf.clickondone()
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf.clickonlogout()
        self.logger.info("************* Logout succesful **********")
        lp.setUserName(self.usernames1)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin succesful **********")
        if "uploading youtube videos" in driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedforempndrelvideo.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=54)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_editnewsfeedforemployees(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_012_NewsFeed **********")
        self.logger.info("************ TC_23 Edit a feed by changing the text content ************")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhats(self.whats)
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf.clickonthreedot()
        nf.clickonedit()
        nf.setwhatedit(self.whatedit)
        nf.clickonpublic()
        nf.clickonupdate()
        time.sleep(3)
        if "News feed updated successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedupdate.png")
            assert False
        time.sleep(3)
        nf.clickonlogout()
        self.logger.info("************* Logout successful **********")
        lp.setUserName(self.usernames1)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin successful **********")
        if "Hi,gud mrng employeesEditing the feed" in driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_editnewsfeedforemployees.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=55)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_deletenewsfeedforempndrelvideo(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_013_NewsFeed **********")
        self.logger.info(
            "*********** TC_29 Delete a feed and select the checkbox for permanent deletion. **************")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhatyoutube(self.whatyoutube)
        nf.clickonpublic()
        nf.clickonyoutube()
        nf.setyoutubeurl(self.youtubeurl)
        nf.clickondone()
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False

        time.sleep(3)
        nf.clickonthreedot()
        nf.clickondelete()
        nf.clickondeletecheckbox()
        nf.clickondeletebutton()
        time.sleep(3)
        if "News Feed deleted successfully!" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
            # driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_deletenewsfeedforempndrelvideo.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=56)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_archivenewsfeedwith5images(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_014_NewsFeed **********")
        self.logger.info("************ TC_28 Delete a feed without selecting the checkbox. ***********")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setfiveimages(self.fiveimages)
        nf.setgallery(self.absolute_path1)
        nf.setgallery(self.absolute_path2)
        nf.setgallery(self.absolute_path3)
        nf.setgallery(self.absolute_path4)
        nf.setgallery(self.absolute_path5)
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf.clickonthreedot()
        nf.clickondelete()
        nf.clickondeletebutton()
        time.sleep(3)
        if "Feed deleted successfully, saved in archived feed" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedarchieve.png")
            assert False
        time.sleep(3)
        nf.clickonthreedots()
        nf.clickonarchive()
        time.sleep(3)
        if "five images upload" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
            # driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_archivenewsfeedwith5images.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=57)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_bookmarknewsfeed(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_015_NewsFeed **********")
        self.logger.info("************* TC_32 Add a feed to bookmarks. ***********")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* companyLogin succesful **********")
        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhatso(self.whatso)
        nf.clickonpublic()
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf = NewsFeed(driver)
        nf.clickonthreedot()
        nf.clickonbookmark()
        nf.clickonexplore()
        time.sleep(3)
        if "hii,all employees and relation companies" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedverification.png")
            assert False
        time.sleep(3)
        nf.clickonremove()
        self.logger.info("************* TC_33 Remove a feed from bookmarks. **********")
        time.sleep(3)
        if "hii,all employees and relation companies" in driver.page_source:
            self.logger.error("********** NewsFeed test is failed *********")
            # Log and take a screenshot
            driver.save_screenshot(".\\Screenshots\\" + "test_bookmarknewsfeed.png")
            assert False
        else:
            self.logger.info("************** NewsFeed test is passed **********")
        time.sleep(3)

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=58)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_selfposts(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_016_NewsFeed **********")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* companyLogin successful **********")
        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhatso(self.whatso)
        nf.clickonpublic()
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf.clickonthreedots()
        nf.clickonfilter()
        nf.clickonall()
        nf.clickonself()
        nf.clickonapply()
        time.sleep(3)
        if "hii,all employees and relation companies" in driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_selfposts.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=59)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_sharenewsfeed(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_017_NewsFeed **********")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* companyLogin succesful **********")
        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhatso(self.whatso)
        nf.clickonpublic()
        nf.clickonpost()
        time.sleep(1)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(1)
        nf.clickonshare()
        nf.clickonwhatsapp()
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[1])
        time.sleep(3)

        if "https://web.whatsapp.com/" in driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedwhatsapp.png")
            assert False
        time.sleep(3)
        window_handles = driver.window_handles
        # Switch to the last opened window
        driver.switch_to.window(window_handles[0])
        nf.clickonshare()
        driver.implicitly_wait(5)
        nf.clickonfacebook()
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[2])
        time.sleep(3)

        if "https://www.facebook.com/" in driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedfacebook.png")
            assert False
        time.sleep(3)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[0])
        nf.clickonshare()
        nf.clickontwitter()
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[3])
        time.sleep(3)

        if "https://twitter.com/" in driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedtwitter.png")
            assert False
        time.sleep(3)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[0])
        nf.clickonshare()
        nf.clickonlinkedin()
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[4])
        time.sleep(3)

        if "https://www.linkedin.com/" in driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedlinkedin.png")
            assert False
        time.sleep(3)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[0])
        nf.clickonshare()
        nf.clickontelegram()
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[5])
        time.sleep(3)

        if "https://telegram.me/" in driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedtelegram.png")
            assert False
        time.sleep(3)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[0])
        nf.clickonshare()
        nf.clickongmail()
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[6])
        time.sleep(3)

        if "https://accounts.google.com/" in driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")
        elif "https://www.google.com/" in driver.current_url:
            # Handle the other condition
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedgoogle.png")
            assert False
        time.sleep(3)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[0])
        nf.clickoninstagram()
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[7])
        time.sleep(3)

        if "https://www.instagram.com/" in driver.current_url:
            self.logger.info("********** NewsFeed test is passed *********")
            # driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_sharenewsfeedinstagram.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.tests
    @pytest.mark.regression
    @pytest.mark.run(order=60)
    # @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_adminfeed(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_018_NewsFeed **********")
        lp = LoginPage(driver)
        lp.setUserName(self.usernames3)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhatso(self.whatso)
        nf.clickonpublic()
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf.clickonlogout()
        self.logger.info("************* Logout successful **********")
        lp.setUserName(self.usernames1)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* relationcompanyLogin successful **********")
        if "hii,all employees and relation companies" in driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # driver.close()
        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_adminfeed.png")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @pytest.mark.run(order=61)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_feedcomment(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_019_NewsFeed **********")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhats(self.whats)
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf.clickoncomment()
        nf.setcommenttext(self.commenttext)
        nf.clickonsend()
        nf.clickoncancelcmnt()
        nf.clickonlogout()
        self.logger.info("************* Logout successful **********")
        driver.execute_script("window.open('', '_blank');")
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[1])
        driver.get(self.baseURL)
        lp.setUserName(self.usernames)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(3)
        self.logger.info("************* EmpLogin successful **********")
        if "Hi,gud mrng employees" in driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedverification.png")
            assert False
        time.sleep(3)
        nf.clickoncomments()
        nf.clickonreplycmnt()
        nf.setreplytext(self.replytext)
        nf.clickonreplysend()
        nf.clickonviewreply()
        time.sleep(3)
        if "gudmorning all" in driver.page_source:
            self.logger.info("********** NewsFeed display is passed *********")
            # self.driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed display is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_feedcomment.png")
            assert False

    @pytest.mark.kri
    @pytest.mark.regression
    @pytest.mark.run(order=62)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_editfeedcomment(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_020_NewsFeed **********")
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login successful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.setwhats(self.whats)
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf.clickoncomment()
        nf.setcommenttext(self.commenttext)
        nf.clickonsend()
        nf.clickoncommentthreedot()
        nf.clickoncommentedit()
        nf.setcommentedittext(self.commentedittext)
        nf.clickoncommenteditsend()
        nf.clickoncommentthreedot()
        nf.clickoncommentdelete()
        nf.clickoncommentconfirmdelete()
        time.sleep(3)
        if "all hiii gud mrng" in driver.page_source:
            self.logger.error("********** NewsFeed test is failed *********")
            # Log and take a screenshot
            driver.save_screenshot(".\\Screenshots\\" + "test_editfeedcomment.png")
            assert False


        else:
            self.logger.info("************** NewsFeed test is passed **********")
            # driver.close()

    # @pytest.mark.babi
    @pytest.mark.regression
    @pytest.mark.run(order=63)
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="Skipping this test")
    def test_adminasemployeefeed(self, driver):
        driver.maximize_window()
        self.logger.info("****Opening URL****")
        driver.get(self.baseURL)
        self.logger.info("************* Test_018_NewsFeed **********")
        lp = LoginPage(driver)
        lp.setUserName(self.usernames3)
        lp.setPassword(self.password)
        lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting NewsFeed Test **********")
        nf = NewsFeed(driver)
        nf.clickOnwhat()
        nf.clickonrolechange()
        nf.clickonemployeeselect()
        nf.setwhatso(self.whatso)
        nf.clickonpost()
        time.sleep(3)
        if "News feed created successfully" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
            # driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedcreation.png")
            assert False
        time.sleep(3)
        nf.setsearch(self.search)
        nf.clickonlike()
        self.logger.info("************ TC_37 Like a feed. **********")
        time.sleep(3)
        if "1 Like" in driver.page_source:
            self.logger.info("********** NewsFeed test is passed *********")
            # driver.close()

        else:
            # Log and take a screenshot
            self.logger.error("************** NewsFeed test is failed **********")
            driver.save_screenshot(".\\Screenshots\\" + "test_newsfeedlike.png")
            assert False
        time.sleep(3)
        nf.clickondislike()
        self.logger.info("************* TC_38 Unlike a feed. ************")

    if __name__ == '__main__':
        unittest.main(verbosity=2)
