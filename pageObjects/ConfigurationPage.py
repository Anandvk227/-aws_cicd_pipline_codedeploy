import time
# from telnetlib import EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class ConfigurationPage:

    Module_configuration_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/ul[1]/li[8]/div[1]"
    searchField_xpath = "//input[@type='search']"
    tab_Departments_xpath = "//button[normalize-space()='Departments']"
    tab_Relations_xpath = "//button[normalize-space()='Relations']"
    NewBtn_xpath = "//button[normalize-space()='New']"
    text_Department_name_xpath = "//input[@id='outlined-basic']"
    text_EnterDescription_xpath = "//textarea[@placeholder='Write a summary about (120 characters)']"
    button_Create_xpath = "//button[normalize-space()='Create']"
    button_Cancel_xpath = "//button[normalize-space()='Cancel']"
    button_Update_xpath = "//button[normalize-space()='Update']"
    area_openDept_xpath = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[4]/div[2]/div[1]/div[1]"
    tab_Divisions_xpath = "//button[normalize-space()='Divisions']"
    tab_Designations_xpath = "//button[normalize-space()='Designations']"
    linkText_EditDepartment_xpath = "//span[normalize-space()='Edit']"
    linkText_DeleteDepartment_xpath = "//span[text()='Delete']"
    linkText_DeleteDepartmentCancel_xpath = "//button[normalize-space()='Cancel']"
    linkText_DeleteDepartmentDelete_xpath = "//button[normalize-space()='Delete']"
    icon_DeleteDivision_xpath = "(//*[name()='svg'][@aria-label='Delete'])[1]"
    icon_EditDivision_xpath = "(//*[name()='svg'][contains(@aria-label,'Edit')])[1]"
    verify_DeptCreatedSuccessful_xpath = "//div[contains(text(),'Department created successfully')]"
    verify_DivisionCreatedSuccessful_xpath = "//div[contains(text(),'Division created successfully')]"
    verify_DesignationCreatedSuccessful_xpath = "//div[contains(text(),'Designation created successfully')]"
    verify_DivisionDeletedSuccessfully_xpath = "//div[contains(text(),'Division deleted successfully')]"
    verify_DesignationDeletedSuccessfully_xpath = "//div[contains(text(),'Designation deleted successfully')]"
    verify_DepartmentDeletedSuccessfully_xpath = "//div[contains(text(),'Department deleted successfully')]"
    verify_DeleteError_xpath = "//div[contains(text(),'Some Division Under This Department')]"
    linkText_Configuration_xpath = "//span[@class='breadCrumbTxt pointer headingSM']"
    verify_DeptUpdatedSuccessful_xpath = "//div[contains(text(),'Department updated successfully')]"
    verify_DivisionUpdatedSuccessful_xpath = "//div[contains(text(),'Division updated successfully')]"
    verify_DesignationUpdatedSuccessful_xpath = "//div[contains(text(),'Designation updated successfully')]"
    verify_RelationCreatedSuccessfully_xpath = "//div[contains(text(),'Relation created successfully')]"
    verify_RelationUpdatedSuccessfully_xpath = "//div[contains(text(),'Relation updated successfully')]"
    verify_RelationDeletedSuccessfully_xpath = "//div[contains(text(),'Relation deleted successfully')]"


    def __init__(self, driver):
        self.driver = driver

    def Text_DeptUpdatedSuccessful(self):
        time.sleep(2)
        DeptUpdatedSuccessful = self.driver.find_element(By.XPATH, self.verify_DeptUpdatedSuccessful_xpath)
        text = DeptUpdatedSuccessful.text  # Access 'text' as an attribute, not as a function
        return text
    def Text_RelationDeletedSuccessfully(self):
        time.sleep(2)
        DeptUpdatedSuccessful = self.driver.find_element(By.XPATH, self.verify_RelationDeletedSuccessfully_xpath)
        text = DeptUpdatedSuccessful.text  # Access 'text' as an attribute, not as a function
        return text
    def Text_RelationUpdatedSuccessfully(self):
        time.sleep(2)
        DeptUpdatedSuccessful = self.driver.find_element(By.XPATH, self.verify_RelationUpdatedSuccessfully_xpath)
        text = DeptUpdatedSuccessful.text  # Access 'text' as an attribute, not as a function
        return text
    def Text_RelationCreatedSuccessfully(self):
        time.sleep(2)
        DeptUpdatedSuccessful = self.driver.find_element(By.XPATH, self.verify_RelationCreatedSuccessfully_xpath)
        text = DeptUpdatedSuccessful.text  # Access 'text' as an attribute, not as a function
        return text
    def Text_DivisionUpdatedSuccessful(self):
        time.sleep(2)
        DivisionUpdatedSuccessful = self.driver.find_element(By.XPATH, self.verify_DivisionUpdatedSuccessful_xpath)
        text = DivisionUpdatedSuccessful.text  # Access 'text' as an attribute, not as a function
        return text
    def Text_DesignationUpdatedSuccessful(self):
        DesignationUpdatedSuccessful = self.driver.find_element(By.XPATH, self.verify_DesignationUpdatedSuccessful_xpath)
        text = DesignationUpdatedSuccessful.text  # Access 'text' as an attribute, not as a function
        return text

    def Text_DepartmentDeletedSuccessfully(self):
        time.sleep(2)
        DepartmentDeletedSuccessfully = self.driver.find_element(By.XPATH, self.verify_DepartmentDeletedSuccessfully_xpath)
        text = DepartmentDeletedSuccessfully.text  # Access 'text' as an attribute, not as a function
        return text
    def Text_DesignationDeletedSuccessfully(self):
        time.sleep(2)
        DesignationDeletedSuccessfully = self.driver.find_element(By.XPATH, self.verify_DesignationDeletedSuccessfully_xpath)
        text = DesignationDeletedSuccessfully.text  # Access 'text' as an attribute, not as a function
        return text
    def Text_DivisionDeletedSuccessfully(self):
        DivisionDeletedSuccessfully = self.driver.find_element(By.XPATH, self.verify_DivisionDeletedSuccessfully_xpath)
        text = DivisionDeletedSuccessfully.text  # Access 'text' as an attribute, not as a function
        return text

    def Text_DeptCreatedSuccessful(self):
        DeptCreatedSuccessful = self.driver.find_element(By.XPATH, self.verify_DeptCreatedSuccessful_xpath)
        text = DeptCreatedSuccessful.text  # Access 'text' as an attribute, not as a function
        return text
    def Text_DeleteError(self):
        DeleteError = self.driver.find_element(By.XPATH, self.verify_DeleteError_xpath)
        text = DeleteError.text  # Access 'text' as an attribute, not as a function
        return text
    def Text_DivisionCreatedSuccessful(self):
        time.sleep(2)
        DivisionCreatedSuccessful = self.driver.find_element(By.XPATH, self.verify_DivisionCreatedSuccessful_xpath)
        text = DivisionCreatedSuccessful.text  # Access 'text' as an attribute, not as a function
        return text
    def Text_DesignationCreatedSuccessful(self):
        time.sleep(2)
        DesignationCreatedSuccessful = self.driver.find_element(By.XPATH, self.verify_DesignationCreatedSuccessful_xpath)
        text = DesignationCreatedSuccessful.text  # Access 'text' as an attribute, not as a function
        return text
    def clickModuleConfiguration(self):
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Module_configuration_xpath)))
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        #
        # # Wait for a short while to ensure the element is clickable
        # time.sleep(1)
        #
        # element.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Business Settings']")))
        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        element.click()
        wait = WebDriverWait(self.driver, 10)
        element1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Department']")))

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        element1.click()

    def setsearchField(self, searchField):
        # time.sleep(2)
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.searchField_xpath)))
        element.clear()
        # element.send_keys(Keys.CONTROL + "a", searchField)
        element.send_keys(searchField)
        time.sleep(3)

    def setRelationsearchField(self, searchRelation):
        self.driver.find_element(By.XPATH, self.searchField_xpath).clear()
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.searchField_xpath).send_keys(searchRelation)
        time.sleep(1)

    def clickDepartments(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_Departments_xpath)))
        element.click()
    def clickConfigurationtextLink(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.linkText_Configuration_xpath)))
        element.click()

    def clickRelations(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.tab_Relations_xpath)))
        element.click()

    def clickNewBtn(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.NewBtn_xpath)))
        element.click()

    def setDepartmentName(self, searchField):
        department_name_element = self.driver.find_element(By.XPATH, self.text_Department_name_xpath)
        department_name_element.clear()
        department_name_element.send_keys(searchField)

    def setEnterDescription(self, searchField):
        self.driver.find_element(By.XPATH, self.text_EnterDescription_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_EnterDescription_xpath).send_keys(searchField)

    def clickCreateBtn(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_Create_xpath)))
        element.click()

    def clickCancelBtn(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_Cancel_xpath)))
        element.click()

    def clickUpdateBtn(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_Update_xpath)))
        element.click()

    def clickopenDept(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.area_openDept_xpath)))
        element.click()

    def clickDivisionsTab(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.tab_Divisions_xpath)))
        element.click()

    def clickDesignationsTab(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.tab_Designations_xpath)))
        element.click()

    def clickEditDepartment(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.linkText_EditDepartment_xpath)))
        element.click()

    def clickDeleteDepartment(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.linkText_DeleteDepartment_xpath)))
        element.click()

    def clickDeleteDepartmentCancel(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.linkText_DeleteDepartmentCancel_xpath)))
        element.click()

    def clickDeleteDepartmentDelete(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.linkText_DeleteDepartmentDelete_xpath)))
        element.click()

    def clickDeleteDivision(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.icon_DeleteDivision_xpath)))
        element.click()

    def clickEditDivision(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.icon_EditDivision_xpath)))
        element.click()
