import time
# from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # Login Page
    textbox_username_id = "outlined-basic1"
    textbox_password_id = "outlined-adornment-password undefined"
    button_login_xpath = "//button[@type='submit']"
    link_logout_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[4]/div[1]"
    LoginText_Xpath = "//h1[contains(text(),'Login')]"
    createPost_xpath = "//span[@class='pdngXS brdrBlackSM postWidth brdrRadiusXSM pointer lightTxt feedHover']"
    NewsFeedText_xpath = "//span[contains(text(),'Create News Feed')]"
    button_newsfeed_xpath = "//body/div[@id='root']/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]"
    IncorrectLoginText_xpath = "//span[contains(text(),'Incorrect username or password.')]"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setUserName1(self, username1):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username1)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_login_xpath)))
        element.click()
        time.sleep(4)

    def clickNewsFeed(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_newsfeed_xpath)))
        element.click()

    def clickcreatePost(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.createPost_xpath)))
        element.click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

    def loginText(self):
        LoginText = self.driver.find_element((By.XPATH, self.LoginText_Xpath))
        text = LoginText.text  # Access 'text' as an attribute, not as a function
        return text  # Return the text for further use

    def newsFeedText(self):
        NewsfeedText = self.driver.find_element(By.XPATH, self.NewsFeedText_xpath)
        text = NewsfeedText.text  # Access 'text' as an attribute, not as a function
        return text

    def IncorrectLoginText(self):
        NewsfeedText = self.driver.find_element(By.XPATH, self.IncorrectLoginText_xpath)
        text = NewsfeedText.text  # Access 'text' as an attribute, not as a function
        return text
