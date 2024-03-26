import time
import pytest
from openpyxl.reader.excel import load_workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sunithaPageObjects.CompanyProfile import LoginPage
from selenium import webdriver
from pageObjects.randomGen import randomGen
from sunithaPageObjects.WebinarPage import WebinarPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from GenericLib.BaseClass import BaseClass


class Test_Webinar():
    workbook = load_workbook("TestData/LoginData.xlsx")

    # Access the active worksheet
    worksheet = workbook.active
    baseURL = ReadConfig.getApplicationURL()
    username = worksheet["A2"].value
    password = "Inlink@123"
    description = "About Media Drive Module of Inlink"
    LimitSeats = "10"
    coHost = worksheet["A6"].value
    panelist = worksheet["C6"].value
    Email = "ksunik7k3@gmail.com"
    PastTabSearch = "QA"
    EditTitle = "Automation team meeting"
    web = "Webinar "
    PTS = "Training Meeting"
    Training = "Training Meeting"
    logger = LogGen.loggen()

    title = "Webinar Meeting"
    description = "Webinar Meeting for Dev Meeting"
    email = "sunitha@instavc.com"

    # title = randomGen.random_first_name()
    # description = randomGen.random_Description()
    # email = randomGen.random_email()


    Trainingtitle = "Training meeting"
    TriningDiscription = "All modules of inlynk, code review with automation team  "

    EmpMail = worksheet["B6"].value
    EmpPassword = "Inlink@123"

    username1 = worksheet["A25"].value

    PartnerMail = worksheet["I3"].value

    PartnerPassword = "Inlink@123"

    ShareHolderMail = worksheet["I2"].value
    shareholderPassword = "Inlink@123"
    workbook.close()

    @pytest.mark.run(order=86)
    @pytest.mark.regression
    # @pytest.mark.skip(reason="skipping this test")
    def test_webinar(self, driver):
        driver.maximize_window()
        self.logger.info("****** Login verification *****")
        driver.get(self.baseURL)
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setpassword(self.password)
        lp.clickLogin()
        wp = WebinarPage(driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()

        # Webinar Creation----------------------------------Webinar Creation
        self.logger.info("****** TC_01 '+' New button webinar meeting creation*****")
        wp.NewButton()
        self.logger.info("****** TC_02	Verify 'Webinar meeting' radio button *****")
        wp.WebinarRadioButton()
        self.logger.info("****** TC_03	Verify the Enter Title input field *****")
        wp.setTitle(self.title)
        self.logger.info("****** TC_04	Verify the Enter Description input field *****")
        wp.setDescription(self.description)
        self.logger.info("****** TC_05	Verify Date and Time Selection *****")
        wp.DateTime()
        # Need to Update the Date#
        wp.CalendarforwardArrow()
        wp.selectDate()
        wp.calendarHours()
        wp.Hrs()
        wp.SelectHours()
        wp.minutes()
        wp.SelectMinutes()
        self.logger.info("****** TC_06	Verify the RSVP toggle button *****")
        wp.ToggleButton()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.logger.info("****** TC_07 limit seats input *****")
        wp.LimitSeats(self.LimitSeats)
        self.logger.info("****** TC_08	Verify Add 'co- host' search bar *****")
        wp.coHostSearch(self.coHost)
        self.logger.info("****** TC_09	Verify the Add Participants Check box *****")
        wp.AddPanelist(self.panelist)
        wp.SelectPanelist()
        wp.selectCoHost()
        self.logger.info(
            "****** TC_11	Verify Network relation searching by name, of already selected relation(check box) *****")
        wp.manufacturer()
        wp.shareHolder()
        wp.vendor()
        wp.partner()
        wp.distributor()
        wp.memberEMail(self.email)
        self.logger.info("****** TC_10	Verify 'Invite Members' Search bar *****")
        wp.setAddEmail()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.logger.info("****** TC_02	Verify 'Training' radio button *****")
        wp.PublicEnable()
        self.logger.info("****** TC_12	Verify 'Schedule webinar button and button *****")
        wp.Schedule()

        xpath = "//div[contains(text(),'Created webinar successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_webinar.png")
            assert False

    @pytest.mark.run(order=87)
    # @pytest.mark.suni
    @pytest.mark.skip(reason="skipping this test")
    def test_EmployeeBookSeat(self, driver):
        driver.maximize_window()
        self.logger.info("****** Login verification *****")
        driver.get(self.baseURL)
        lp = LoginPage(driver)
        lp.setUserName(self.EmpMail)
        lp.setpassword(self.EmpPassword)
        lp.clickLogin()

        wp = WebinarPage(driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        wp.CalendarFeb()
        self.logger.info("****** TC_25	Verify Book Seat button for both Training and Webinar*****")
        wp.BookSeat()

        xpath = "//div[contains(text(),'Your seat has been successfully booked.')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_EmployeeBookSeat.png")
            assert False

        time.sleep(1)
        wp.CloseToaster()
        wp.Logout()

        lp.setUserName(self.PartnerMail)  # as Partner booking the seat
        lp.setpassword(self.PartnerPassword)
        lp.clickLogin()

        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        wp.CalendarFeb()
        self.logger.info("****** TC_25	Verify Book Seat button for both Training and Webinar*****")
        wp.BookSeat()
        xpath = "//div[contains(text(),'Your seat has been successfully booked.')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_EmployeeBookSeat.png")
            assert False

        time.sleep(1)
        wp.CloseToaster()
        wp.Logout()

        lp.setUserName(self.ShareHolderMail)  # as a share holder booking the seat
        lp.setpassword(self.shareholderPassword)
        lp.clickLogin()

        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        wp.CalendarFeb()
        self.logger.info("****** TC_25	Verify Book Seat button for both Training and Webinar*****")
        wp.BookSeat()
        xpath = "//div[contains(text(),'Your seat has been successfully booked.')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_EmployeeBookSeat.png")
            assert False

        time.sleep(1)

    # Webinar Past tab -------------------------------------------Webinar Past tab
    @pytest.mark.run(order=88)
    # @pytest.mark.skip(reason="skipping this test")
    def test_PastTabsSessionVerification(self, driver):
        driver.maximize_window()
        self.logger.info("****** Login verification *****")
        driver.get(self.baseURL)
        lp = LoginPage(driver)
        lp.setUserName(self.username1)
        lp.setpassword(self.password)
        lp.clickLogin()

        wp = WebinarPage(driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()
        self.logger.info("****** TC_14	Verify when User selects the Past tab *****")
        wp.PastTab()
        self.logger.info("****** TC_15	Verify the Custom calendar filter *****")
        wp.FebDate()
        wp.PastViewButton()
        self.logger.info("****** TC_32	Verify the User Accessibility of Chat History *****")
        wp.ChatHistory()
        time.sleep(2)
        wp.CloseChatHistrory()
        self.logger.info("****** TC_33	Verify the User Accessibility of Poll History *****")
        wp.ViewPollHistory()

        if "Results" in driver.page_source:
            self.logger.info("********* test_PastTabsSessionVerification is Passed ***********")

        else:
            self.logger.info("********* test_PastTabsSessionVerification is failed ***********")
            driver.save_screenshot(".\\Screenshots\\" + "test_PastTabsSessionVerification.png")
            assert False

        wp.ClosePollHistory()
        wp.PastSessionBreadcrumb()

    # webinar past session search bar----------------------------webinar past session search bar
    @pytest.mark.run(order=89)
    @pytest.mark.sunitha
    # @pytest.mark.skip(reason="skipping this test")
    def test_PastSessionCardSearch(self, driver):
        driver.maximize_window()
        self.logger.info("****** Login verification *****")
        driver.get(self.baseURL)
        lp = LoginPage(driver)
        lp.setUserName(self.username1)
        lp.setpassword(self.password)
        lp.clickLogin()

        wp = WebinarPage(driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()
        wp.PastTab()
        wp.FebDate()
        self.logger.info("****** TC_32	Verify the User Accessibility of Chat History *****")
        wp.PastSearch(self.PastTabSearch)
        time.sleep(2)
        if "QA   Meeting " in driver.page_source:
            self.logger.info("********* test_PastSessionCardSearch Test is Passed ***********")
        else:
            self.logger.error("********* test_PastSessionCardSearch Test is failed ***********")
            driver.save_screenshot(".\\Screenshots\\" + "test_PastSessionCardSearch.png")
            self.logger.error("Page source:\n%s" % driver.page_source)
            assert False

        wp.SessionCard()
        wp.SessionCardClose()

    @pytest.mark.run(order=90)
    # @pytest.mark.skip(reason="skipping this test")
    def test_PastTabFilter(self, driver):
        driver.maximize_window()
        self.logger.info("****** Login verification *****")
        driver.get(self.baseURL)
        lp = LoginPage(driver)
        lp.setUserName(self.username1)
        lp.setpassword(self.password)
        lp.clickLogin()

        wp = WebinarPage(driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()
        wp.PastTab()
        time.sleep(2)
        self.logger.info("****** TC_30	Verify Custom Calendar Filter *****")
        wp.FebDate()
        self.logger.info("****** TC_23	Verify the Filter in the Past Tab page *****")
        wp.PastTabFilter()
        wp.TrainingCheckBox()
        wp.ApplyButton()
        self.logger.info("****** TC_29	Verify the filter functionalityF *****")
        wp.PastTabFilter()
        wp.TrainingCheckBox()
        wp.WebinarCheckbox()
        wp.ApplyButton()

    @pytest.mark.run(order=91)
    # @pytest.mark.skip(reason="skipping this test")
    def test_WebinarUpcomingTab(self, driver):
        driver.maximize_window()
        self.logger.info("****** Login verification *****")
        driver.get(self.baseURL)
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setpassword(self.password)
        lp.clickLogin()

        wp = WebinarPage(driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()

        self.logger.info("****** TC_14	Verify when User selects the Upcoming tab *****")
        wp.UpcomingTab()

        self.logger.info("******  TC_15	Verify the Custom calendar filter *****")
        wp.MarchMonth()

        self.logger.info(
            "****** TC_16	Verify the visibility of all the Trainings and Webinars for the selected date from calendar*****")
        wp.UpcomingMar25()
        wp.SessionEdit()

        self.logger.info("****** TC_18	Verify Copy link option *****")
        wp.copyLink()
        wp.SessionEdit()

        self.logger.info("****** TC_19	Verify Copy invitation option *****")
        wp.copyInvitation()
        wp.CopyButton()
        wp.CancelCard()

        self.logger.info("****** TC_20	Verify View Registrants option for Training/Webinar *****")
        wp.ViewRegistrants()
        wp.BreadCrumb()

        self.logger.info("****** TC_30	Verify Custom Calendar Filter *****")
        wp.MarchMonth()
        wp.UpcomingMar25()

        self.logger.info("****** TC_17	Verify the 3 dot more button (for host) *****")
        wp.SessionEdit()

        self.logger.info("****** TC_22	Verify Delete Training/Webinar option in 3dot button *****")
        wp.DeleteSession()
        wp.DeleteWebinar()
        time.sleep(2)

        if "Webinar deleted successfully" in driver.page_source:
            self.logger.info("********* test_WebinarUpcomingTab is passed ***********")
        else:
            self.logger.info("********* test_WebinarUpcomingTab is failed ***********")
            driver.save_screenshot(".\\Screenshots\\" + "test_WebinarUpcoming.png")
            self.logger.error("Page source:\n%s" % driver.page_source)
            assert False

    @pytest.mark.run(order=92)
    # @pytest.mark.skip(reason="skipping this test")
    def test_TrainingCreation(self, driver):
        driver.maximize_window()
        self.logger.info("****** Login verification *****")
        driver.get(self.baseURL)
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setpassword(self.password)
        lp.clickLogin()

        wp = WebinarPage(driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()
        self.logger.info("****** TC_01 '+' New button webinar meeting creation*****")
        wp.NewButton()
        self.logger.info("****** TC_03	Verify the Enter Title input field *****")
        wp.EditTitle(self.Trainingtitle)
        self.logger.info("****** TC_03	Verify the Enter description input field *****")
        wp.setDescription(self.TriningDiscription)
        self.logger.info("****** TC_05	Verify Date and Time Selection *****")
        wp.DateTime()
        # Need to Update the Date#
        wp.CalendarforwardArrow()
        wp.selectDate()
        wp.calendarHours()
        # wp.NormalPath()#
        wp.Hrs()
        wp.SelectHours()
        wp.minutes()
        wp.SelectMinutes()
        self.logger.info("****** TC_06	Verify the RSVP toggle button *****")
        wp.ToggleButton()
        self.logger.info(
            "****** TC_07	Verify Limit seats toggle button and'Select number of seats' input field *****")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wp.LimitSeats(self.LimitSeats)
        self.logger.info("****** TC_08	Verify Add 'co- host' search bar *****")
        wp.coHostSearch(self.coHost)
        self.logger.info(
            "****** TC_11	Verify Network relation searching by name, of already selected relation(check box) *****")
        wp.manufacturer()
        wp.shareHolder()
        wp.vendor()
        wp.partner()
        wp.distributor()
        self.logger.info("****** TC_10	Verify 'Invite Members' Search bar*****")
        wp.memberEMail(self.Email)
        self.logger.info("****** TC_12	Verify 'Schedule training button and 'Cancel' button *****")
        wp.Schedule()

        xpath = "//div[contains(text(),'Created training successfully')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_TrainingCreation.png")
            assert False

    @pytest.mark.run(order=93)
    # @pytest.mark.skip(reason="skipping this test")
    def test_EmployeeBookSeat(self, driver):
        driver.maximize_window()
        self.logger.info("****** Login verification *****")
        driver.get(self.baseURL)
        lp = LoginPage(driver)
        lp.setUserName(self.EmpMail)
        lp.setpassword(self.EmpPassword)
        lp.clickLogin()

        wp = WebinarPage(driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        wp.MarchMonth()
        wp.UpcomingMar25()
        self.logger.info("****** TC_25	Verify Book Seat button for both Training and Webinar*****")
        wp.BookSeat()
        xpath = "//div[contains(text(),'Your seat has been successfully booked.')]"
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_EmployeeBookSeat.png")
            assert False

        time.sleep(1)
        wp.CloseToaster()
        wp.Logout()

        lp.setUserName(self.PartnerMail)  # as Partner booking the seat
        lp.setpassword(self.PartnerPassword)
        lp.clickLogin()

        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        wp.MarchMonth()
        wp.UpcomingMar25()
        self.logger.info("****** TC_25	Verify Book Seat button for both Training and Webinar*****")
        wp.BookSeat()
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_EmployeeBookSeat.png")
            assert False

        time.sleep(1)
        wp.CloseToaster()
        wp.Logout()

        lp.setUserName(self.ShareHolderMail)  # as a share holder booking the seat
        lp.setpassword(self.shareholderPassword)
        lp.clickLogin()

        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        wp.MarchMonth()
        wp.UpcomingMar25()
        self.logger.info("****** TC_25	Verify Book Seat button for both Training and Webinar*****")
        wp.BookSeat()
        try:
            # Use WebDriverWait to wait for the element to be present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Text Found : {element.text}")
            assert True
        except:
            self.logger.info(f"Text Not Found")
            driver.save_screenshot(".\\Screenshots\\" + "test_EmployeeBookSeat.png")
            assert False

        time.sleep(1)

    @pytest.mark.run(order=94)
    @pytest.mark.krishna
    # @pytest.mark.flaky(reruns=3, reruns_delay=2)
    # @pytest.mark.skip(reason="skipping this test")
    def test_TrainingUpcoming(self, driver):
        driver.maximize_window()
        self.logger.info("****** Login verification *****")
        driver.get(self.baseURL)
        lp = LoginPage(driver)
        lp.setUserName(self.username)
        lp.setpassword(self.password)
        lp.clickLogin()
        wp = WebinarPage(driver)
        self.logger.info("****** TC_13 Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()
        self.logger.info("****** TC_23 Verify the Filter in the Upcoming Tab page*****")
        self.logger.info("****** TC_30 Verify Custom Calendar Filter*****")
        wp.MarchMonth()
        wp.UpcomingMar25()
        self.logger.info("****** TC_22 Verify Delete Training/Webinar option in 3dot button*****")
        wp.SessionEdit()
        wp.editListbox()
        self.logger.info("****** TC_03 Verify the Enter Title input field*****")
        wp.EditTitle(self.EditTitle)
        wp.UpdateMeeting()
        wp.UpdateConfirm()
        wp.SessionEdit()
        self.logger.info("****** TC_20 Verify View Registrants option for Training/Webinar*****")
        wp.ViewRegistrants()
        wp.BreadCrumb()
        wp.UpcomingTab()
        wp.MarchMonth()
        wp.UpcomingMar25()
        wp.SessionEdit()
        self.logger.info("****** TC_22 Verify Delete Training/Webinar option in 3dot button*****")
        wp.DeleteSession()
        wp.DeleteWebinar()
        time.sleep(2)

        if "Training deleted successfully" in driver.page_source:
            self.logger.info("********* test_TrainingPastTab is passed ***********")
        else:
            self.logger.info("********* test_TrainingPastTab is failed ***********")
            driver.save_screenshot(".\\Screenshots\\" + "test_TrainingUpcoming.png")
            self.logger.error("Page source:\n%s" % driver.page_source)
            assert False

    # Training Past tab_______________________________________Training Past tab
    @pytest.mark.run(order=95)
    @pytest.mark.babi
    # @pytest.mark.skip(reason="skipping this test")
    def test_TrainingPastTab(self, driver):
        driver.maximize_window()
        self.logger.info("****** Login verification *****")
        driver.get(self.baseURL)
        lp = LoginPage(driver)
        lp.setUserName(self.username1)
        lp.setpassword(self.password)
        lp.clickLogin()

        wp = WebinarPage(driver)
        self.logger.info("****** TC_13	Verify the accessibility and of Training & Webinar from Menu module*****")
        wp.clickTAndWModule()
        self.logger.info("****** TC_31	Verify the Training and Webinar Details in the past tab*****")
        wp.PastTab()
        self.logger.info("****** TC_30	Verify Custom Calendar Filter*****")
        # wp.FebMonth()  # Uncomment this line if you need to test the February month filter
        self.logger.info("****** TC_27	Verify User Accessibility of Past sessions for (HOST)*****")
        wp.FebDate()
        time.sleep(2)

        if "Training Meeting" in driver.page_source:
            self.logger.info("********* test_TrainingPastTab is passed ***********")
        else:
            self.logger.info("********* test_TrainingPastTab is failed ***********")
            driver.save_screenshot(".\\Screenshots\\" + "test_TrainingPastTab.png")
            self.logger.error("Page source:\n%s" % driver.page_source)
            assert False
        time.sleep(2)
        self.logger.info("****** TC_31(After click on the Training or Webinar past session card)*****")
        wp.PastViewButton()
        wp.ChatHistory()
        wp.CloseChatHistrory()
        wp.PastSessionBreadcrumb()
        time.sleep(2)


    if __name__ == '__main__':
        unittest.main(verbosity=2)













