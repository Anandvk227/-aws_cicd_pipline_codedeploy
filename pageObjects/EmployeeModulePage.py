import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeeModulePage:
    Tab_Pending_xpath = "//button[normalize-space()='Pending']"
    text_PendingSearchField_xpath = "//input[@placeholder='Search Pending Employee']"
    text_RejectedSearchField_xpath = "//input[@placeholder='Search Rejected Employee']"
    DD_Status_xpath = "//span[@id='status']"
    DD_StatusApprove_xpath = "(//li[@role='menuitem'])[1]"
    Field_EmpId_xpath = "(//input[@type='text'])[3]"
    DD_department_xpath = "//div[@id='demo-simple-select']"
    DD_division_xpath = "(//div[@id='demo-simple-select'])[2]"
    DD_designation_xpath = "(//div[@id='demo-simple-select'])[3]"
    Button_Approve_xpath = "//button[contains(text(),'Approve')]"
    Text_Approved_xpath = "//div[contains(text(),'Employee approved successfully')]"
    DD_statusReject_xpath = "//div[@id='fade-menu']//li[2]"
    DD_ConfReject_xpath = "//button[normalize-space()='Reject']"
    Text_RejectedSuccessful_xpath = "//div[contains(text(),'Employee rejected successfully')]"
    Tab_Reject_xpath = "//button[normalize-space()='Rejected']"




    def __init__(self, driver):
        self.driver = driver

    def ClickPendingTab(self):
        time.sleep(3)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Tab_Pending_xpath))
        )
        element.click()
        # self.driver.find_element(By.XPATH, self.Tab_Pending_xpath).click()

    def ClickRejectTab(self):
        time.sleep(3)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Tab_Reject_xpath))
        )
        element.click()
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, self.Tab_Reject_xpath).click()

    def setPendingSearchField(self, Password):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.text_PendingSearchField_xpath))
        )
        element.clear()
        element.send_keys(Password)
        time.sleep(3)
        # self.driver.find_element(By.XPATH, self.text_PendingSearchField_xpath).clear()
        # self.driver.find_element(By.XPATH, self.text_PendingSearchField_xpath).send_keys(Password)
        # time.sleep(3)

    def setRejectedSearchField(self, Password):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.text_RejectedSearchField_xpath))
        )
        element.clear()
        element.send_keys(Password)
        time.sleep(3)

    def setEmpId(self, Password):
        self.driver.find_element(By.XPATH, self.Field_EmpId_xpath).clear()
        self.driver.find_element(By.XPATH, self.Field_EmpId_xpath).send_keys(Password)

    def ClickStatusDD(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.DD_Status_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.DD_Status_xpath).click()

    def ClickStatusApprove(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.DD_StatusApprove_xpath).click()

    def ClickDepartmentDD(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.DD_department_xpath).click()


    def ClickDivisionDD(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.DD_division_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.DD_division_xpath).click()

    def ClickDesignationDD(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.DD_designation_xpath).click()

    def ClickApproveButton(self):
        self.driver.find_element(By.XPATH, self.Button_Approve_xpath).click()
        time.sleep(2)

    def ClickSelectDD(self):
        time.sleep(1)
        # Simulate pressing the down arrow key
        # ActionChains(self.driver).key_down(Keys.DOWN).perform()
        # # Add a delay if necessary:
        # time.sleep(0.1)

        # Simulate pressing the Enter key
        ActionChains(self.driver).key_down(Keys.ENTER).perform()
        # Add a delay if necessary:
        time.sleep(0.1)

    def ClickStatusReject(self):
        self.driver.find_element(By.XPATH, self.DD_statusReject_xpath).click()

    def ClickConfReject(self):
        self.driver.find_element(By.XPATH, self.DD_ConfReject_xpath).click()


