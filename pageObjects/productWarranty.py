import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class productWarranty():
    button_PW = "(//div[@class='resNavLink  brdrBSM'])[2]"
    button_PW_Individual = "//span[text()='Product Warranty']"
    text_NoPW_registered = "//span[text()='No Warranty is registered']"
    button_register = "//button[text()='register']"
    txt_setSearchCompany = "//input[@placeholder = 'Search Company*']"
    txt_searchField = "//input[@type= 'search']"
    txt_prdId = "//input[@id='prodId']"
    txt_serialNumber = "//input[@id='serialNumber']"
    txt_prodName = "//input[@id='prodName']"
    txt_purchaseDate = "//input[@placeholder='dd/mm/yyyy']"
    txt_ExpiryDate = "//input[@placeholder='dd/mm/yyyy']"
    file_invoice = "//input[@id='invoice']"
    text_customerName = "//input[@id='customerName']"
    text_customerEmail = "//input[@id='customerEmail']"
    text_customerPhone = "//input[@name='customerPhone']"
    button_submit = "//button[contains(text(),'SUBMIT')]"
    button_Cancel = "//button[contains(text(),'Cancel')]"
    button_Update = "//button[contains(text(),'Update')]"
    button_ConfUpdate = "(//button[contains(text(),'Update')])[2]"
    button_Delete = "//button[contains(text(),'Delete')]"
    button_ConfDelete = "(//button[contains(text(),'Delete')])[2]"
    button_Edit = "//button[contains(text(),'Edit')]"
    button_Reject = "//button[contains(text(),'Reject')]"
    button_ConfReject = "(//button[contains(text(),'Reject')])[2]"
    button_Approve = "//button[contains(text(),'Approve')]"
    button_ConfApprove = "(//button[contains(text(),'Approve')])[2]"
    text_verifyCreate = "//div[contains(text(),'Warranty registration successfully submitted')]"
    text_verifyUpdate = "//div[contains(text(),'Warranty details updated successfully')]"
    text_verifyApprove = "//div[contains(text(),'The registration request has been successfully app')]"
    text_verifyReject = "//div[contains(text(),'The registration request has been rejected.')]"
    text_verifyDelete = "//div[contains(text(),'Warranty details deleted successfully')]"
    open_invoice = "//span[@class='capitalTxt primaryTxt pdngLXS pointer ellipsisTxt firstLetter ']"
    status_Pending = "//span[contains(text(),'Pending')]"
    iconStatus_Approve = "//tbody/tr[1]/td[8]/div[1]/span[1]/*[1]"
    iconStatus_Reject = "//span[@aria-label='Reject']"
    iconStatus_ConfReject = "//button[text()='Reject']"
    button_Continue = "//button[text()='Continue']"
    iconStatusConf_Approve = "//button[contains(text(),'Approve')]"
    close_Toast = "//button[@class='Toastify__close-button Toastify__close-button--light']"
    icon_profile = "//div[@class='flexAutoRow pointer']"
    button_logout = "//span[contains(text(),'Log Out')]"
    button_Conflogout = "//button[contains(text(),'Logout')]"
    Text_Purchase = "//span[text()='Purchase Date']"
    Close_filePreview = "//button[@class='flexInline slideBtns slideDownBtn alignCntr justifyCntr']"
    Download_filePreview = "//button[@class='flexInline slideBtns slideCloseBtn alignCntr justifyCntr']"
    ################################ Status Filter ################################################
    IconFilter = "(//*[name()='path'])[10]"
    filterAll = "//span[text()='All']"
    filterPending = "//body/div[@id='basic-menu']/div[3]/ul[1]/li[2]"
    filterActive = "//body/div[@id='basic-menu']/div[3]/ul[1]/li[3]"
    filterRejected = "//body/div[@id='basic-menu']/div[3]/ul[1]/li[4]"
    filterExpired = "//body/div[@id='basic-menu']/div[3]/ul[1]/li[5]"
    filterClear = "//span[contains(text(),'Clear')]"


    def __init__(self, driver):
        self.logger = None
        self.driver = driver

    def clickPWfeature(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_PW))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
    def clickPWfeature_Individual(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_PW_Individual))
        )
        element.click()
    def clickClose_filePreview(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Close_filePreview))
        )
        element.click()
    def clickDownload_filePreview(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.Download_filePreview))
        )
        element.click()

    def clickPurchaseDate(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.Text_Purchase))
        )
        element.is_displayed()

    def clicklogoutButton(self):
        time.sleep(0.5)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_logout))
        )
        element.click()
    def clickConflogoutButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_Conflogout))
        )
        element.click()
    def clickProfileIcon(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.icon_profile))
        )
        element.click()

    def clickRegisterButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_register))
        )
        element.click()
    def clickclose_Toast(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.close_Toast))
        )
        element.click()

    def setProductId(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_prdId))
        )
        element.send_keys(name)
    def setserialNumber(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_serialNumber))
        )
        element.send_keys(name)
    def setprodName(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_prodName))
        )
        element.send_keys(name)
    def setpurchaseDate(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_purchaseDate))
        )
        element.send_keys(name)
    def setExpiryDate(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_ExpiryDate))
        )
        element.send_keys(name)

    def setfile_invoice(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.file_invoice))
        )
        element.send_keys(name)
    def setcustomerName(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.text_customerName))
        )
        element.send_keys(Keys.CONTROL + "a")  # Select all text
        element.send_keys(Keys.BACKSPACE)  # Delete selected text
        element.send_keys(name)  # Input the new text

    def setcustomerEmail(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.text_customerEmail))
        )
        element.send_keys(name)
    def setcustomerPhone(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.text_customerPhone))
        )
        element.send_keys(Keys.CONTROL + "a")  # Select all text
        element.send_keys(Keys.BACKSPACE)  # Delete selected text
        element.send_keys(name)  # Input the new text


    def setSearchCompany(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.txt_setSearchCompany))
        )
        element.send_keys(name)
    def setsearchField(self, name):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.txt_searchField))
        )
        element.send_keys(name)

    def clickSubmitButton(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_submit))
        )
        element.click()
    def clickCancelButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_Cancel))
        )
        element.click()
    def clickUpdateButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_Update))
        )
        element.click()
    def clickConfUpdateButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_ConfUpdate))
        )
        element.click()

    def clickDeleteButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_Delete))
        )
        element.send_keys(Keys.HOME)
        element.click()
    def clickConfDeleteButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_ConfDelete))
        )
        element.click()

    def clickEditButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_Edit))
        )
        element.click()

    def clickRejectButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_Reject))
        )
        element.click()

    def clickConfRejectButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_ConfReject))
        )
        element.click()
    def clickApproveButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_Approve))
        )
        element.click()
    def clickConfApproveButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_ConfApprove))
        )
        element.click()

    def clickOpen_invoice(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.open_invoice))
        )
        element.click()
    def clickstatus_Pending(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.status_Pending))
        )
        element.click()
    def clickiconStatus_Approve(self):
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.iconStatus_Approve))
        )
        element.click()
    def clickiconStatus_Reject(self):
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.iconStatus_Reject))
        )
        element.click()
    def clickiconStatus_ConfReject(self):
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.iconStatus_ConfReject))
        )
        element.click()

    def clickContinueButton(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_Continue))
        )
        element.click()
    def clickiconStatusConf_Approve(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.iconStatusConf_Approve))
        )
        element.click()

    def clickIconFilter(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.IconFilter))
        )
        element.click()
    def clickfilterAll(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.filterAll))
        )
        element.click()
    def clickfilterPending(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.filterPending))
        )
        element.click()
    def clickfilterActive(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.filterActive))
        )
        element.click()
    def clickfilterClear(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.filterClear))
        )
        element.click()
    def clickfilterRejected(self):
        time.sleep(0.5)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.filterRejected))
        )
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element.click()
    def clickfilterExpired(self):
        time.sleep(0.5)
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.filterExpired))
        )
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element.click()




