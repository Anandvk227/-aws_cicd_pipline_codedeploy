import time
import unittest
import pytest
from openpyxl.reader.excel import load_workbook
from openpyxl.workbook import Workbook
from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.companyListingPage import companyListingPage
from pageObjects.LoginPage import LoginPage
# from testCases.conftest import setup
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.companySignUpPage import companySignUpPage
from pageObjects.randomGen import randomGen
from selenium import webdriver
from GenericLib.BaseClass import BaseClass
from openpyxl import workbook
import re


class mailboxCode():

    def mailboxCode(self, driver):
        sp = companySignUpPage(driver)
        # Execute JavaScript to open a new tab
        driver.execute_script("window.open('about:blank', '_blank');")

        # Perform actions in the new tab (if needed)
        # For example:
        driver.switch_to.window(driver.window_handles[1])
        self.logger.info("******** Opening new url in another tab for Email OTP ***********")
        time.sleep(1)
        driver.get("https://maildrop.cc/")
        time.sleep(1)
        yopmail = driver.find_element(By.XPATH, "(//input[@type='text'])[1]")
        yopmail.send_keys(email + Keys.ENTER)
        time.sleep(1)

        # reload_button = driver.find_element(By.XPATH, "//img[@title='Reload']")
        #
        # # Click the Reload button every second until the subject is displayed or a maximum time is reached
        # max_wait_time = 60  # Set your maximum wait time in seconds
        # start_time = time.time()
        #
        # while time.time() - start_time < max_wait_time:
        #     reload_button.click()
        #
        #     try:
        #         # Check if the subject is displayed
        #         subject = WebDriverWait(driver, 10).until(
        #             EC.presence_of_element_located((By.XPATH, "//td[@class='subject']"))
        #         )
        #         subject.click()
        #         break  # Break out of the loop if subject is displayed
        #     except StaleElementReferenceException:
        #         print("StaleElementReferenceException occurred. Retrying...")
        #         continue  # Retry the loop if StaleElementReferenceException occurs
        #     except TimeoutException:
        #         time.sleep(1)

        iframeElement = driver.find_element(By.ID, "emailframe")
        driver.switch_to.frame(iframeElement)

        # Code outside the loop will be executed after the loop or when a TimeoutException occurs
        otp = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//body/div[@id='___gatsby']/div[@id='gatsby-focus-wrapper']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/iframe[1]"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", otp)
        time.sleep(0.5)

        confirmation_code = otp.text
        getOTP = re.search(r'\b\d+\b', confirmation_code).group()
        print(getOTP)

        # This code is for QA ENV
        otp = driver.find_element(By.XPATH,
                                  "//body/div[@id='___gatsby']/div[@id='gatsby-focus-wrapper']/div[1]/main[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/iframe[1]")
        driver.execute_script("arguments[0].scrollIntoView(true);", otp)
        time.sleep(0.5)

        confirmation_code = otp.text
        getOTP = re.search(r'\b\d+\b', confirmation_code).group()
        print(getOTP)

        self.logger.info("******** Switching back and entering the otp ***********")
        driver.switch_to.default_content()

        driver.switch_to.window(driver.window_handles[0])

        sp.setOtp(getOTP)

        time.sleep(2)
