import time

from selenium.webdriver import ActionChains, Keys
# from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddEmployeesPage:
    button_employeesModule_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]"
    button_Active_xpath = "//button[normalize-space()='Active']"
    text_activeSearchField_xpath = "//input[@placeholder='Search Active Employee']"
    button_New_xpath = "//button[normalize-space()='New']"
    text_fullname_xpath = "//input[@name='fullname']"
    text_email_xpath = "//input[@id='email']"
    text_personalEmail_xpath = "//input[@id='personalEmail']"
    text_phoneNumber_xpath = "//input[@type='tel']"
    text_empId_xpath = "//input[@name='series']"
    DD_Dept_xpath = "//div[@id='demo-simple-select']"
    button_AddDept_xpath = "//button[text()='Add department']"
    button_DoneAddDept_xpath = "//button[contains(text(),'Done')]"
    DD_Division_xpath = "(//div[@id='demo-simple-select'])[2]"
    button_AddDivision_xpath = "//button[text()='Add division']"
    text_Division_xpath = "(//input[@id='outlined-basic'])[2]"
    DD_Designation_xpath = "(//div[@id='demo-simple-select'])[3]"
    button_AddDesignation_xpath = "//button[text()='Add designation']"
    DD_CountryDD_xpath = "(//button[@aria-haspopup='listbox'])[2]"
    DD_state_xpath = "//div[@id='state']"
    DD_city_xpath = "//div[@id='city']"
    button_Add_xpath = "//button[normalize-space()='Add']"
    button_Cancel_xpath = "//button[contains(text(),'Cancel')]"
    Verify_EmployeeCreatedText_xpath = "//div[contains(text(),'Employee created successfully')]"
    EmployeeStatus_xpath = "(//span[@id='status'])[2]"
    AdminStatus_xpath = "//span[text()='Admin']"
    EmployeesStatus_xpath = "(//span[text()='Employees'])[2]"
    GrantAdmin_xpath = "//button[normalize-space()='Grant team admin']"
    RemoveAdmin_xpath = "//button[normalize-space()='Remove from Admin']"
    buttonActive_xpath = "//span[text()='Active']"
    buttonDeactivate_xpath = "//span[text()='Deactivate']"
    text_reason_xpath = "//input[@type='text']"
    confDeactivate_xpath = "//button[text()='Deactivate']"
    # Invitee feature
    button_invite_xpath = "//button[text()='Invite']"
    DD_Company_xpath = "//div[text()='Company']"
    select_company_xpath = "//li[@data-value='company']"
    select_employee_xpath = "//li[@data-value='employee']"
    button_Copy_xpath = "//button[text()='Copy']"
    button_email_xpath = "//input[@type='email']"
    button_submit_xpath = "//button[@type='submit']"
    button_Send_xpath = "//button[text()='Send']"




    def __init__(self, driver):
        self.driver = driver

    def clickEmployeesModule(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_employeesModule_xpath)))
        element.click()

    def Text_EmployeeCreatedSuccessful(self):
        DeptUpdatedSuccessful = self.driver.find_element(By.XPATH, self.Verify_EmployeeCreatedText_xpath)
        text = DeptUpdatedSuccessful.text  # Access 'text' as an attribute, not as a function
        return text
    def clickAddButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_Add_xpath)))
        element.click()

    def clickCountryDD(self):
        time.sleep(2)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.DD_CountryDD_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        # Click the Company Sign Up button
        element.click()
        time.sleep(1)
        # self.driver.find_element(By.XPATH, self.DD_CountryDD_xpath).click()

    def clickActive(self):
        time.sleep(3)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_Active_xpath))
        )
        element.click()
        # self.driver.find_element(By.XPATH, self.button_Active_xpath).click()

    def clickNewButton(self):
        self.driver.find_element(By.XPATH, self.button_New_xpath).click()


    def setDivisionName(self, searchField):
        self.driver.find_element(By.XPATH, self.text_Division_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_Division_xpath).send_keys(searchField)
    def clickAddDeptButton(self):
        # time.sleep(2)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.button_AddDept_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        # Click the Company Sign Up button
        element.click()
        time.sleep(1)

    def clickDoneAddDept(self):
        self.driver.find_element(By.XPATH, self.button_DoneAddDept_xpath).click()

    def clickAddDivisionButton(self):
        # self.driver.find_element(By.XPATH, self.button_AddDivision_xpath).click()
        # time.sleep(1.5)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_AddDivision_xpath))
        )
        element.click()

    def clickAddDesignation(self):
        # self.driver.find_element(By.XPATH, self.button_AddDesignation_xpath).click()
        # time.sleep(1.5)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_AddDesignation_xpath))
        )
        element.click()

    def setActiveSearchField(self, activeSearchField):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.text_activeSearchField_xpath))
        )
        element.clear()
        element.send_keys(activeSearchField)
        time.sleep(2)
        # self.driver.find_element(By.XPATH, self.text_activeSearchField_xpath).clear()
        # self.driver.find_element(By.XPATH, self.text_activeSearchField_xpath).send_keys(activeSearchField)

    def setFullname(self, activeSearchField):
        self.driver.find_element(By.XPATH, self.text_fullname_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_fullname_xpath).send_keys(activeSearchField)

    def setEmail(self, activeSearchField):
        self.driver.find_element(By.XPATH, self.text_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_email_xpath).send_keys(activeSearchField)

    def setPersonalEmail(self, activeSearchField):
        self.driver.find_element(By.XPATH, self.text_personalEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_personalEmail_xpath).send_keys(activeSearchField)

    def setPhoneNumber(self, activeSearchField):
        self.driver.find_element(By.XPATH, self.text_phoneNumber_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_phoneNumber_xpath).send_keys(activeSearchField)

    def setEmpId(self, activeSearchField):
        self.driver.find_element(By.XPATH, self.text_empId_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_empId_xpath).send_keys(activeSearchField)

    def ClickEmployeeStatus(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.EmployeeStatus_xpath)))
        element.click()
    def ClickAdminStatus(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.AdminStatus_xpath)))
        element.click()
    def ClickEmployeesStatus(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.EmployeesStatus_xpath)))
        element.click()
    def ClickRemoveStatus(self):
        # time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.RemoveAdmin_xpath)))
        element.click()
    def ClickGrantAdmin(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.GrantAdmin_xpath)))
        element.click()
    def ClickDD_Dept(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.DD_Dept_xpath)))
        element.click()
    def ClickDD_Division(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.DD_Division_xpath)))
        element.click()
    def ClickDD_Designation(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.DD_Designation_xpath)))
        element.click()
    def ClickbuttonActive(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.buttonActive_xpath)))
        element.click()
    def ClickbuttonDeactivate(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.buttonDeactivate_xpath)))
        element.click()
    def setreasonText(self, text):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.text_reason_xpath)))
        element.send_keys(text)
    def ClickconfDeactivate(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.confDeactivate_xpath)))
        element.click()

    def perform_keyboard_actions(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    # Invite

    def ClickcInviteButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_invite_xpath)))
        element.click()

    def ClickDDcompany(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.DD_Company_xpath)))
        element.click()

    def selctCompany(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.select_company_xpath)))
        element.click()

    def selctEmployee(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.select_employee_xpath)))
        element.click()

    def ClickcCopyButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_Copy_xpath)))
        element.click()

    def setInviteEmail(self, name):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_email_xpath)))
        element.send_keys(name)

    def ClickcSubmitButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_submit_xpath)))
        element.click()

    def ClickcSendButton(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_Send_xpath)))
        element.click()
