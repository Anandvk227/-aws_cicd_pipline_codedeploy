import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class companyListingPage:
    emailField_xpath = "//input[@id='email']"
    passwordField_xpath = "//input[@id='outlined-adornment-password password']"
    License_xpath = "//span[text()='License and Subscriptions']"
    searchFiled_xpath = "//input[@type='search']"
    subscription_path = "//body/div[@id='root']/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/button[2]"
    edit_path = "//button[text()='edit']"
    listed_path = "//body/div[@id='root']/div[1]/div[1]/div[5]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]"
    update_path = "//button[text()='update']"
    ListedToast = "//div[contains(text(), 'Company license updated successfully')]"
    PlanDetails = "//span[contains(text(),'Plan Details')]"
    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.emailField_xpath).clear()
        self.driver.find_element(By.XPATH, self.emailField_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.passwordField_xpath).clear()
        self.driver.find_element(By.XPATH, self.passwordField_xpath).send_keys(password)

    def clickLicense(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.License_xpath))
        )
        element.click()
    def setsearchFiled(self,name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.searchFiled_xpath))
        )
        element.send_keys(name)
        time.sleep(2)

    def clicksubscription(self):
        # time.sleep(3)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.subscription_path))
        )
        element.click()
    def clickedit(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.edit_path))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        element.click()

    def clicklisted(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.listed_path))
        )
        # Instantiate ActionChains
        actions = ActionChains(self.driver)
        # Example: Hover over the element
        actions.move_to_element(element).perform()
        element.click()

    def clickupdate (self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.update_path))
        )
        element.click()
