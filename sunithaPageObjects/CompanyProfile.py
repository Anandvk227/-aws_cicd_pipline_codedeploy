import time

from lib2to3.pgen2 import driver
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class LoginPage:
    textbox_username_name = "email"
    textbox_password_name = "password"
    button_login_xpath = "//button[normalize-space()='Login']"
    newsFeed_click_xpath = "//div[@class='resNavLink activeLink']"
    company_profile_xpath = "//span[normalize-space()='Company Profile']"

    # Banner image uploading---------------------------------------------------------------
    BannerImageClick_button_xpath = "//div[@class='flexCol justifyEnd alignCntr pointer editIcon']//input[@id='preview']"
    SaveBannerImage_button_xpath = "//button[normalize-space()='Save']"
    # need to validate the banner image
    EditBanner_click_xpath = "//span[@class='flexInline primaryTxt pointer editIcon pointer']"
    UploadBannerImageAgain_xpath = "//div[@class='flexCol pointer']//input[@id='preview']"
    # again need to save and click on edit
    BannerImageRemove_xpath = "//span[contains(text(),'Remove')]"

    # ProfileImage Uploading________________________________________________________________
    ProfileImageClick_button_xpath = "//div[@class='flexCol justifyEnd alignCntr pointer addProfilePicIcon']//input[@id='preview']"
    SaveProfileImage_button_xpath = "//button[normalize-space()='Save']"
    EditProfile_click_xpath = "//span[contains(@class,'flexInline primaryTxt pointer editIconAvatar')]"
    UploadProfileImageAgain_xpath = "//div[@class='flexCol pointer']//input[@id='preview']"
    ProfileImageRemove_xpath = "//span[contains(text(),'Remove')]"

    # Office Details------------------------------------------------------
    click_office_details_button = "//button[@aria-label='Official details']"
    textbox_company_name = "nameOfCompany"
    inputfield_orgname_id = "typeOfOrg"
    Remove_industry_xpath = "//*[@data-testid='CancelIcon']"

    inputfield_industry_id = "industry"
    button_industry_name_xpath = "(//*[@data-testid='AddIcon'])[3]"
    button_calendar_css = "svg[data-testid='CalendarIcon']"
    buttonpreviousmonth_xpath = "//button[@title='Previous month']"
    button_date_xpath = "//button[normalize-space()='12']"
    input_website_id = "website"
    button_save_xpath = "//button[normalize-space()='Save']"

    # Overview________________________________________________________________
    scrollIntoOverView_xpath = "//span[text()='Followers']"
    button_edit_xpath = "//button[@aria-label='Edit']//*[name()='svg']//*[name()='path' and contains(@d,'M3 17.25V2')]"
    textarea_company_summary_id = "desc"
    textarea_address_id = "address"
    country_dropdown_xpath = "//button[@id='rfs-btn']"
    select_india_xpath = "(//li[@role='option'])[2]"
    textarea_contact_id = "contactPerson"
    listbox_state_id = "state"
    select_sate_ap_xpath = "//li[normalize-space()='Andhra Pradesh']"
    click_city_id = "city"
    listbox_city_xpath = "//li[normalize-space()='Addanki']"
    input_pincode_id = "pincode"
    input_domain_name_id = "domainName"
    input_contact_person_id = "contactPerson"
    button_save_xpath = "//button[normalize-space()='Save']"
    path_certifications_xpath = "//span[contains(@title,'Go to certifications')]"

    # Awards___________________________________________________________________________
    Awards_button_xpath = "//div[@class='flexRow pdngHXS alignCntr']//button[@aria-label='Add']"
    Click_preview_xpath = "//div[@class='flexRow justifyCntr alignCntr editAwardDialog brdrBlackSM']//input[@id='preview']"
    awardTitleField_id = "outlined-basic"
    SaveAward_xpath = "//button[normalize-space()='Save']"

    # social Media Links---------------------------------------------------------------
    button_social_media_links_xpath = "//div[@class='flexCol pdngXS']//div[@class='flexAutoRow pdngLXS']"

    listbox_social_media_dropdown_id = "name"
    select_social_media_xpath = "//li[normalize-space()='Instagram']"
    input_url_id = "url"
    click_save_button_xpath = "//button[normalize-space()='Save']"

    # clicking elements______________________________________________________________________________
    Resource_click_xpath = "//span[@title='Go to resources ']"
    Network_click_xpath = "//span[@title='Go to networks']"
    Certification_xpath = "//span[@title='Go to certifications']"
    Settings_xpath = "//button[normalize-space()='Settings']"
    NewsFeed_xpath = "//button[normalize-space()='News Feed']"

    def __init__(self, driver):
        self.driver = driver

    # ____________________Banner Image

    def BannerImageClick(self, absolute_path3):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.BannerImageClick_button_xpath)))
        element.send_keys(absolute_path3)

    def SaveBannerImage(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 3)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.SaveBannerImage_button_xpath)))
        element.click()
        time.sleep(1)

    def EditBanner(self):
        # time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.EditBanner_click_xpath)))
        # time.sleep(1)
        element.click()

    def UploadBannerImageAgain(self, absolute_path4):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.UploadBannerImageAgain_xpath)))
        element.send_keys(absolute_path4)

    def BannerImageRemove(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 7)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.BannerImageRemove_xpath)))
        element.click()

    # ----------------------------Profile Image Uploading
    def ProfileImageClick(self, absolute_path5):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.ProfileImageClick_button_xpath)))
        element.send_keys(absolute_path5)

    def SaveProfileImage(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.SaveProfileImage_button_xpath)))
        element.click()

    def EditProfile(self):
        time.sleep(3)
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.EditProfile_click_xpath)))
        element.click()

    def UploadProfileImage(self, absolute_path6):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.UploadProfileImageAgain_xpath)))
        element.send_keys(absolute_path6)

    def ProfileImageRemove(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.ProfileImageRemove_xpath)))
        element.click()

    def setUserName(self, username):
        # time.sleep(2)
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((By.NAME, self.textbox_username_name)))
        element.send_keys(username)

    def setpassword(self, password):
        # time.sleep(2)
        self.driver.find_element(By.NAME, self.textbox_password_name).clear()
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((By.NAME, self.textbox_password_name)))
        element.send_keys(password)

    def clickLogin(self):
        # time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_login_xpath)))
        element.click()
        time.sleep(3)

    """def clickNewsfeedModule(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.newsFeed_click_xpath)))
        element.click()"""

    def clickCompanyProfile(self):
        time.sleep(2)

        wait = WebDriverWait(self.driver, 20)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.company_profile_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        # Wait for the element to be clickable
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.company_profile_xpath)))
        # Click the Company Sign Up button
        element.click()

    # _______________________________Official Details
    def ofc_details(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.click_office_details_button)))
        element.click()

    def setCompany(self, companyname):
        time.sleep(1)
        self.driver.find_element(By.NAME, self.textbox_company_name).send_keys(Keys.CONTROL + 'a')
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((By.NAME, self.textbox_company_name)))
        element.send_keys(companyname)

    def setOrganisation(self, orgname):
        time.sleep(1)
        self.driver.find_element(By.ID, self.inputfield_orgname_id).send_keys(Keys.CONTROL + 'a')
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((By.ID, self.inputfield_orgname_id)))
        element.send_keys(orgname)

    def RemoveIndustry(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.Remove_industry_xpath)))
        element.click()

    def setIndustry(self, industry):
        time.sleep(1)
        self.driver.find_element(By.ID, self.inputfield_industry_id).send_keys(Keys.CONTROL + 'a')
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((By.ID, self.inputfield_industry_id)))
        element.send_keys(industry)
        time.sleep(2)

    def clickIndustryName(self):
        time.sleep(2)
        # wait = WebDriverWait(self.driver, 5)
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_industry_name_xpath)))
        # element.click()
        self.driver.find_element(By.XPATH,self.button_industry_name_xpath).click()

    def clickCalendar(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.button_calendar_css)))
        # time.sleep(1)
        element.click()
        time.sleep(1)


    def clickonpreviousmonth(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.buttonpreviousmonth_xpath).click()

    def clickDate(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_date_xpath)))
        element.click()

    def setwebsite(self, website):
        time.sleep(1)
        self.driver.find_element(By.ID, self.input_website_id).send_keys(Keys.CONTROL + 'a')
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((By.ID, self.input_website_id)))
        element.send_keys(website)

    def clickSave(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_save_xpath)))
        element.click()

    # _____________________________________OverView

    def scrollIntoOverView(self):
        time.sleep(1)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.scrollIntoOverView_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        time.sleep(1)
        # element.click()
    def scrollIntoAwards(self):
        time.sleep(1)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, "//span[normalize-space()='Contact number']")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        time.sleep(1)
        # element.click()

    def clickEdit(self):
        wait = WebDriverWait(self.driver, 10)
        # Wait for the element to be clickable and visible
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_edit_xpath)))

        # Optionally, you can wait for the element to be visible as well
        wait.until(EC.visibility_of(element))

        # Scroll the element into view
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        # Click the element
        element.click()

    def setCompanySummary(self, companysummary):
        time.sleep(1)
        # self.driver.find_element(By.ID, self.textarea_company_summary_id).send_keys((Keys.CONTROL + 'a'))
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, self.textarea_company_summary_id)))
        # Clear the existing content of the textarea
        element.clear()
        # Send keys to the textarea
        element.send_keys(companysummary)

    def setAddress(self, address):
        time.sleep(1)
        self.driver.find_element(By.ID, self.textarea_address_id).send_keys(Keys.CONTROL + 'a')
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((By.ID, self.textarea_address_id)))
        element.send_keys(address)


    def countrydropdown(self):
        wait = WebDriverWait(self.driver, 20)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.country_dropdown_xpath)))
        # Click the Company Sign Up button
        element.click()
        time.sleep(1)


    def clickonselectindia(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH,self.select_india_xpath)))
        element.click()

    def clickState(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.textarea_contact_id)))
        element.click()
    def clickstatelistbox(self):
        time.sleep(1)
        self.driver.find_element(By.ID, self.listbox_state_id).click()
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.company_profile_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        time.sleep(2)

    def selectState(self):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.select_sate_ap_xpath)))
        element.click()

    def clickcity(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.ID, self.click_city_id)))
        element.click()

    def selectCity(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.listbox_city_xpath)))
        element.click()

    def setpincode(self, pincode):
        time.sleep(1)
        self.driver.find_element(By.ID, self.input_pincode_id).send_keys(Keys.CONTROL + 'a')
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((By.ID, self.input_pincode_id)))
        element.send_keys(pincode)

    def setdomainName(self, domainname):
        time.sleep(1)
        self.driver.find_element(By.ID, self.input_domain_name_id).send_keys(Keys.CONTROL + 'a')
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((By.ID, self.input_domain_name_id)))
        element.send_keys(domainname)

    def setcontactPerson(self, contactperson):
        time.sleep(1)
        self.driver.find_element(By.ID, self.input_contact_person_id).send_keys(Keys.CONTROL + 'a')
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((By.ID, self.input_contact_person_id)))
        element.send_keys(contactperson)

    def clicksave(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.button_save_xpath)))
        element.click()

    # _______________________________Awards

    def AwardsEdit(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.Awards_button_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)
        element.click()

    def ClickPreview(self, absolute_path7):
        time.sleep(2)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.Click_preview_xpath)))
        element.send_keys(absolute_path7)

    def TitleInput(self, awardTitle):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((By.ID, self.awardTitleField_id)))
        element.send_keys(awardTitle)

    def SaveAward(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.SaveAward_xpath)))
        element.click()

        # ____________________________Social Media Links

    def clicksocialMediaLinks(self):

        # Scroll to bring the element into view
        # wait = WebDriverWait(self.driver, 10)
        #
        # # Wait for the element to be clickable
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_social_media_links_xpath)))
        #
        # # Scroll the element into view
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        #
        # # Wait for a brief moment to ensure the scroll action is completed
        # time.sleep(3)
        #
        # # Click on the element
        # element.click()
        # time.sleep(1)
        socialmedia_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.button_social_media_links_xpath)))

        # Scroll to the element using Actions class
        actions = ActionChains(self.driver)
        actions.move_to_element(socialmedia_links).perform()

        # Wait for the element to be clickable
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.button_social_media_links_xpath)))
        # Click on the element
        socialmedia_links.click()

    def clicksocilmedialist(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.listbox_social_media_dropdown_id)))
        element.click()

    def clickSocialMediaName(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.select_social_media_xpath)))
        element.click()

    def setUrl(self, url):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((By.ID, self.input_url_id)))
        element.send_keys(url)

    def clickUrlsave(self):
        time.sleep(1)
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.click_save_button_xpath)))
        element.click()

    def ResourceClick(self):
        time.sleep(2)

        element = self.driver.find_element(By.XPATH, self.Certification_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        time.sleep(1)

        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Resource_click_xpath)))
        element.click()

    def NetworksClick(self):
        time.sleep(1)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.Network_click_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        # Wait for a short while to ensure the element is clickable
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        time.sleep(1)
        element.click()

    def CertificationsClick(self):
        time.sleep(2)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.Certification_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        # Wait for a short while to ensure the element is clickable
        time.sleep(1)
        element.click()

    def Settings(self):
        # time.sleep(2)
        # self.driver.find_element(By.XPATH, self.Settings_xpath).click()
        time.sleep(2)
        # Scroll to bring the element into view
        element = self.driver.find_element(By.XPATH, self.Settings_xpath)
        element1 = self.driver.find_element(By.XPATH, "//span[normalize-space()='Followers  :']")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element1)
        # Wait for a short while to ensure the element is clickable
        time.sleep(1)
        element.click()

    def NewsFeed(self):
        time.sleep(1)
        # self.driver.find_element(By.XPATH, self.NewsFeed_xpath).click()
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, self.NewsFeed_xpath)))
        element.click()
        time.sleep(1)
