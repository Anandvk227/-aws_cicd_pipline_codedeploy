import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class Certification:
    certificationprogramme_xpath = "//span[normalize-space()='Certification Programme']"
    markingsystem_xpath = "//span[normalize-space()='Marking System']"
    markingsystem_new_xpath = "//button[normalize-space()='New']"
    acronym1_xpath = "//input[@placeholder='Enter acronym 1']"
    addanotherfield_xpath = "//button[normalize-space()='Another field']"
    acronym2_xpath = "//input[@placeholder='Enter acronym 2']"
    save_xpath  = "//button[normalize-space()='Save']"
    search_xpath = "//input[@placeholder='Search...']"
    acronymedit_xpath = "//div[@class='flexAutoRow pdngHXXS alignCntr']//span[@class='flexInline primaryTxt pointer']"
    acronympublish_xpath = "//button[normalize-space()='Publish']"
    questionbank_xpath = "//span[normalize-space()='Question bank']"
    enterquestion_xpath = "//input[@placeholder='Enter the question here']"
    firstanswer_xpath = "//div[@class='flexMinWidthRow']//input[@id='title']"
    add_xpath = "//button[contains(@class,'MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorPrimary MuiButton-disableElevation MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorPrimary MuiButton-disableElevation css-191um2i')]"
    secondanswer_xpath = "//input[@placeholder='Type the answer 2']"
    categoryselect_xpath = "//body/div[@id='root']/div[@class='baseBlockCntnr']/div[@class='flexCol fullHeight']/div[@class=' innerMainCntnr sideNav']/div[@class='flexCol']/div[@class='flexCol respdngSM']/div[@class='pdngSM']/div[@class='flexCol whiteBg pdngSM']/div[@class='resColRow']/div[@class='QuestionBankRight pdngHXS']/div[@class='flexCol pdngXS ']/div[2]/div[1]/div[1]/div[1]/div[1]/label[1]/span[1]/span[1]"
    selectanswer_xpath = "(//div[@class='flexAutoRow alignCntr'])[2]"
    selectmarkingsystem_xpath = "//div[@class='MuiFormControl-root MuiFormControl-fullWidth css-tzsjye']//div[1]//div[1]"
    selectmarkingsystemoption_xpath = "(//li[@role='option'])[1]"
    selectacronym_xpath = "//div[@class='flexWrap']//div[1]//span[1]"
    unpublished_xpath = "//body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/button[1]"
    publish_xpath = "//span[text()='Publish']"
    questionsearch_xpath = "//input[@placeholder=':Search...:']"
    questionedit_xpath = "svg.MuiSvgIcon-root.MuiSvgIcon-colorPrimary.MuiSvgIcon-fontSizeMedium.pointer.css-19h30gq"
    buttonedit_xpath = "(//span[@class='flexInline'])[3]"
    questionpublish_xpath = "//button[normalize-space()='Publish']"
    templates_xpath = "//span[normalize-space()='Templates']"
    templateedit_xpath = "//div[@class='templatemediaOverlay certHover']"
    templatename_xpath = "//input[@name='title']"
    logoimg_xpath = "//input[@id='logo']"
    imgsave_xpath = "(//button[text()='Save'])[2]"
    programname_xpath = "//input[@placeholder='Program Name']"
    categoryname_xpath = "//input[@id='category']"
    sign_xpath = "//input[@id='sign']"
    signname_xpath = "//input[@name='signName']"
    signdesignation_xpath = "//input[@name='signDesignation']"
    templatesave_xpath = "//button[normalize-space()='Save']"
    edittemplate_xpath = "//div[@class='flexAutoRow pdngHXXS alignCntr']//span[@class='flexInline primaryTxt pointer']"
    templatepublish_xpath = "//button[contains(text(),'Publish')]"
    certification_xpath = "//span[normalize-space()='Certification']"
    certificationname_xpath = "//input[@type='text']"
    certificationdescription_xpath = "//textarea[@id='description']"
    public_xpath = "//input[@id='public']"
    selectmarkingsystemfield_xpath = "//div[@class='flexRow pdngVXS']//div[@class='MuiFormControl-root MuiFormControl-fullWidth css-tzsjye']//div[1]//div[1]"
    acronymselect_xpath = "//div[@id='menu-']//li[1]"
    # questionnumber_xpath  = "//*[@id='65c4a09577573e35c431acd2']"
    questionnumber_xpath  = "(//input[@type='text'])[2]"
    marks_xpath = "(//input[@type='text'])[4]"
    reapply_xpath = "(//input[@type='text'])[5]"
    minutes_xpath = "(//div[text()='00'])[2]"
    minutestime_xpath = "//li[normalize-space()='03']"
    options_xpath = "//div[text()='A , B']"
    selectoption_xpath = "//li[normalize-space()='I , II']"
    selecttemplate_xpath = "//div[@id='demo-simple-select-Template']"
    templateclick_xpath = "//div[@id='menu-']//li[1]"
    certificatesave_xpath = "//button[normalize-space()='SAVE']"
    certificateconfirmsave_xpath = "(//button[text()='SAVE'])[2]"
    certificateedit_xpath  = "//div[@class='flexInline alignCntr']//span[@class='flexInline primaryTxt pointer']"
    certificatepublish_xpath = "//button[normalize-space()='Publish']"
    certificateconfirmpublish_xpath = "(//button[text()='Publish'])[2]"
    myexams_xpath = "//button[normalize-space()='My exams']"
    getcertificate_xpath = "//button[text()='GET CERTIFICATE']"
    examcheckbox_xpath = "//input[@type='checkbox']"
    certificatedelete_xpath = "//div[@class='flexInline pdngHXXS alignCntr']//span[@class='flexInline primaryTxt pointer']"
    certificateconfirmdelete_xpath = "//button[normalize-space()='Delete']"
    templatedelete_xpath = "(//*[name()='svg'][@aria-label='Delete'])[1]"
    questionbankdelete_xpath = "(//span[@class='flexInline'])[4]"
    acronymdelete_xpath = "//tbody//div[2]//span[1]"
    scrollnote_xpath = "//input[@value='QA']"
    publishedtab_xpath = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]"
    unpublishedtab_xpath = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/button[2]"
    scrollupto_xpath = "//span[contains(text(),'Publish the certificate to selected relations')]"






    def __init__(self, driver):
        self.driver = driver

    def scroll_to_end_of_page(self):
        # Get initial scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to the bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for a short while to let content load (optional)
            time.sleep(1)

            # Calculate new scroll height and compare with the last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                # If scroll height no longer changes, we've reached the end of the page
                break
            last_height = new_height

    def scrollupto(self):
        element = self.driver.find_element(By.XPATH, self.scrollupto_xpath)
        # Scroll to the bottom of the page
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)


    def clickonpublishedtab(self):
        # time.sleep(1)
        # self.driver.find_element(By.XPATH,self.publishedtab_xpath).click()
        wait = WebDriverWait(self.driver, 10)  # Adjust the timeout as needed
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.publishedtab_xpath)))
        element.click()

    def clickonunpublishedtab(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.unpublishedtab_xpath).click()

    def scrollnote(self):
        element = self.driver.find_element(By.XPATH, self.scrollnote_xpath)
        # Scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);", element)
    def clickoncertificationprogramme(self):
        time.sleep(2)
        element = self.driver.find_element(By.XPATH, self.certificationprogramme_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # actions = ActionChains(self.driver)
        #
        # # Press the PAGE_DOWN key to scroll down
        # actions.send_keys(Keys.PAGE_DOWN)
        #
        # # Perform the scrolling action
        # actions.perform()
        # self.driver.find_element(By.XPATH,self.certificationprogramme_xpath).click()
        element.click()
    def clickonmarkingsystem(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.markingsystem_xpath).click()

    def clickonmarkingsystemnew(self):
        self.driver.find_element(By.XPATH,self.markingsystem_new_xpath).click()

    def setacronym1(self,acronym1):
        self.driver.find_element(By.XPATH,self.acronym1_xpath).send_keys(acronym1)

    def clickonaddanotherfield(self):
        self.driver.find_element(By.XPATH,self.addanotherfield_xpath).click()

    def setacronym2(self,acronym2):
        self.driver.find_element(By.XPATH,self.acronym2_xpath).send_keys(acronym2)

    def clickonsave(self):
        self.driver.find_element(By.XPATH,self.save_xpath).click()
        time.sleep(1)


    def setsearch(self,search):
        time.sleep(2)
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,self.search_xpath))
        )
        self.driver.find_element(By.XPATH,self.search_xpath).send_keys(search)
        time.sleep(2)

    def clickonacronymedit(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.acronymedit_xpath))
        )
        self.driver.find_element(By.XPATH,self.acronymedit_xpath).click()

    def clickonacronympublish(self):
        self.driver.find_element(By.XPATH,self.acronympublish_xpath).click()

    def clickonquestionbank(self):
        self.driver.find_element(By.XPATH,self.questionbank_xpath).click()

    def setenterquestion(self,enterquestion):
        self.driver.find_element(By.XPATH,self.enterquestion_xpath).send_keys(enterquestion)

    def setfirstanswer(self,firstanswer):
        self.driver.find_element(By.XPATH,self.firstanswer_xpath).send_keys(firstanswer)

    def clickonadd(self):
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, self.add_xpath)
        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        # Scroll to the element using ActionChains
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        # Click the element
        element.click()

    def setsecondanswer(self,secondanswer):
        self.driver.find_element(By.XPATH,self.secondanswer_xpath).send_keys(secondanswer)


    def clickoncategoryselect(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.categoryselect_xpath).click()
        categoryselect_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.categoryselect_xpath))
        )

        categoryselect_button.click()

    def clickonselectanswer(self):
        time.sleep(2)
        # self.driver.find_element(By.XPATH, self.selectanswer_xpath).click()
        selectanswer_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.selectanswer_xpath))
        )

        selectanswer_button.click()
        time.sleep(3)

    def clickonselectmarkingsystem(self):
        time.sleep(3)
        select_markingsystem = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.selectmarkingsystem_xpath))
        )

        # Scroll to the radio button
        actions = ActionChains(self.driver)
        actions.move_to_element(select_markingsystem).perform()

        select_markingsystem = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.selectmarkingsystem_xpath))
        )
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.selectmarkingsystem_xpath).click()

        # Click on the radio button

    def clickonselectmarkingsystemoption(self):
        time.sleep(2)
        # WebDriverWait(self.driver,20).until(
        #     EC.element_to_be_clickable((By.XPATH,self.selectmarkingsystemoption_xpath))
        # )
        self.driver.find_element(By.XPATH,self.selectmarkingsystemoption_xpath).click()

    def clickonselectacronym(self):
        # self.driver.find_element(By.XPATH,self.selectacronym_xpath).click()
        select_acronym = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.selectacronym_xpath))
        )

        # Scroll to the radio button
        actions = ActionChains(self.driver)
        actions.move_to_element(select_acronym).perform()

        select_acronym = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.selectacronym_xpath))
        )

        # Click on the radio button
        select_acronym.click()

    def clickonquestionsave(self):
        time.sleep(1)
        # self.driver.find_element(By.XPATH,self.save_xpath).click()
        question_save = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.save_xpath))
        )

        # Scroll to the radio button
        actions = ActionChains(self.driver)
        actions.move_to_element(question_save).perform()

        question_save = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.save_xpath))
        )

        # Click on the radio button
        question_save.click()

    def clickonunpublished(self):
        # self.driver.find_element(By.XPATH,self.unpublished_xpath).click()
        unpublished = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.unpublished_xpath))
        )

        # Click on the radio button
        unpublished.click()

    def clickonpublished(self):
        published = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.publish_xpath))
        )

        # Click on the radio button
        published.click()

    def setsearch(self,search):
        self.driver.find_element(By.XPATH,self.search_xpath).send_keys(search)

    def clickonquestionedit(self):
        # Wait for the SVG element to be clickable
        svg_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,self.questionedit_xpath))
        )
        # Click on the SVG element
        svg_element.click()

    def clickonbuttonedit(self):
        edit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.buttonedit_xpath))
        )

        # Scroll the element into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", edit_button)

        # Click on the element using JavaScript
        self.driver.execute_script("arguments[0].click();", edit_button)

    def clickonquestionpublish(self):
        publish_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.questionpublish_xpath))
        )

        # Scroll the publish button into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", publish_button)

        time.sleep(1)

        publish_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.questionpublish_xpath))
        )

        # Click on the publish button
        publish_button.click()

    def clickontemplates(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.templates_xpath)))
        element.click()
        # element = WebDriverWait(self.driver,20).until(
        #     EC.element_to_be_clickable((By.XPATH,self.templates_xpath))
        # )
        #
        # element.click()

    def clickontemplateedit(self):
        # element = WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, self.templateedit_xpath))
        # )
        time.sleep(2)
        # Perform mouseover action
        hover_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.templateedit_xpath))
        )

        # Move the mouse pointer to the hover element
        ActionChains(self.driver).move_to_element(hover_element).perform()

        # Wait for a brief moment
        time.sleep(1)

        # Click on the target element
        hover_element.click()

    def settemplatename(self,templatename):
        self.driver.find_element(By.XPATH,self.templatename_xpath).send_keys(templatename)

    def setlogoimg(self,absolutepath_5):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.logoimg_xpath).send_keys(absolutepath_5)

    def clickonimgsave(self):
        # time.sleep(1)
        # self.driver.find_element(By.XPATH,self.imgsave_xpath).click()
        # time.sleep(1)
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.imgsave_xpath)))
        element.click()
        time.sleep(1)

    def setprogramname(self,programname):
        time.sleep(1)
        WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located((By.XPATH,self.programname_xpath))
        )
        self.driver.find_element(By.XPATH,self.programname_xpath).send_keys(programname)

    def setcategoryname(self,categoryname):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.categoryname_xpath))
        )
        self.driver.find_element(By.XPATH, self.categoryname_xpath).send_keys(categoryname)

    def setsign(self,absolutepath_3):
        sign_img = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.sign_xpath))
        )
        # Scroll to the radio button
        actions = ActionChains(self.driver)
        actions.move_to_element(sign_img).perform()

        sign_img = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.sign_xpath))
        )
        sign_img.send_keys(absolutepath_3)

    def setsignname(self,signname):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.signname_xpath))
        )
        self.driver.find_element(By.XPATH, self.signname_xpath).send_keys(signname)

    def setsigndesignation(self,signdesignation):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.signdesignation_xpath))
        )
        self.driver.find_element(By.XPATH, self.signdesignation_xpath).send_keys(signdesignation)

    def clickontemplatesave(self):
        time.sleep(1)
        template_save = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.templatesave_xpath))
        )
        # Scroll to the radio button
        actions = ActionChains(self.driver)
        actions.move_to_element(template_save).perform()
        template_save.click()
        time.sleep(1)

    def clickonedittemplate(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.edittemplate_xpath))
        )
        self.driver.find_element(By.XPATH,self.edittemplate_xpath).click()

    def clickontemplatepublish(self):
        template_publish = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.templatepublish_xpath))
        )
        # Scroll to the radio button
        actions = ActionChains(self.driver)
        actions.move_to_element(template_publish).perform()
        template_publish.click()

    def clickoncertification(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.certification_xpath))
        )
        self.driver.find_element(By.XPATH,self.certification_xpath).click()

    def setcertificationname(self,certificatename):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.certificationname_xpath))
        )
        self.driver.find_element(By.XPATH, self.certificationname_xpath).send_keys(certificatename)

    def setcertificationdescription(self,certificationdescription):
        WebDriverWait(self.driver,20).until(
            EC.presence_of_element_located((By.XPATH,self.certificationdescription_xpath))
        )
        self.driver.find_element(By.XPATH,self.certificationdescription_xpath).send_keys(certificationdescription)



    def clickonpublic(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.public_xpath).click()

        # Scroll to the element with smooth behavior
        # self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });",
        #                            element_to_scroll)

        # Click on the element


    def clickonselectmarkingsystemfield(self):
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, self.selectmarkingsystemfield_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        time.sleep(1)



    def clickonacronymselect(self):
        acronym_select = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.acronymselect_xpath))
        )

        acronym_select.click()
        time.sleep(1)
    def clickonquestionnumber(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.questionnumber_xpath))
        )
        self.driver.find_element(By.XPATH,self.questionnumber_xpath).click()
        # time.sleep(2)

    def setquestionnumber(self,questionnumber):
        question_number = WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located((By.XPATH,self.questionnumber_xpath))

        )
        # question_number.click()

        # self.driver.find_element(By.XPATH, self.questionnumber_xpath).send_keys(keys.Control+"a", question_number)
        question_number.send_keys(Keys.CONTROL, 'a')

        # Then, send the desired value to the input field
        question_number.send_keys(questionnumber)
    def setMarks(self,marks):
        pass_marks = WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located((By.XPATH,self.marks_xpath))

        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", pass_marks)
        time.sleep(0.5)
        pass_marks.send_keys(Keys.CONTROL, 'a')

        # Then, send the desired value to the input field
        pass_marks.send_keys(marks)


    def setreapply(self,reapply):
        reapply_marks = WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located((By.XPATH,self.reapply_xpath))

        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", reapply_marks)
        time.sleep(0.5)
        reapply_marks.send_keys(Keys.CONTROL, 'a')

        # Then, send the desired value to the input field
        reapply_marks.send_keys(reapply)

    def clickonminutes(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.minutes_xpath))
        )
        self.driver.find_element(By.XPATH,self.minutes_xpath).click()

    def clickonminutestime(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.minutestime_xpath))
        )
        self.driver.find_element(By.XPATH,self.minutestime_xpath).click()

    def clickonoptions(self):
        # WebDriverWait(self.driver,20).until(
        #     EC.element_to_be_clickable((By.XPATH,self.options_xpath))
        # )
        self.driver.find_element(By.XPATH,self.options_xpath).click()

    def clickonselectoption(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.selectoption_xpath))
        )
        self.driver.find_element(By.XPATH,self.selectoption_xpath).click()

    def clickonselecttemplate(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.selecttemplate_xpath))
        )
        self.driver.find_element(By.XPATH,self.selecttemplate_xpath).click()

    def clickontemplateclick(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.templateclick_xpath))
        )
        self.driver.find_element(By.XPATH,self.templateclick_xpath).click()

    def clickoncertificatesave(self):
        element = self.driver.find_element(By.XPATH, self.certificatesave_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

        # Wait for a short while to ensure the element is clickable
        time.sleep(1)

        # Click on the element
        element.click()

    def clickoncertificateconfirmsave(self):
        time.sleep(1)
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.certificateconfirmsave_xpath))
        )
        self.driver.find_element(By.XPATH,self.certificateconfirmsave_xpath).click()
        time.sleep(4)

    def clickoncertificateedit(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.certificateedit_xpath).click()

    def clickoncertificatepublish(self):
        time.sleep(2)
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Certificate template']"))
        )

        # Scroll the publish button into view
        # actions = ActionChains(self.driver)
        # actions.move_to_element(publish_button).perform()
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        #
        time.sleep(1)

        publish_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.certificatepublish_xpath))
        )
        #
        # # Click on the publish button
        publish_button.click()
        # self.driver.find_element(By.XPATH,self.certificatepublish_xpath).click()
        # publish_button = WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, self.certificatepublish_xpath))
        # )
        #
        # # Scroll to the publish button using WebDriver actions
        # actions = ActionChains(self.driver)
        # actions.move_to_element(publish_button).perform()
        #
        # # Click on the publish button
        # publish_button.click()

    def clickoncertificateconfirmpublish(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.certificateconfirmpublish_xpath))
        )
        self.driver.find_element(By.XPATH,self.certificateconfirmpublish_xpath).click()

    def clickonmyexams(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.myexams_xpath))
        )
        self.driver.find_element(By.XPATH,self.myexams_xpath).click()
        time.sleep(1)

    def clickongetcertificate(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.getcertificate_xpath))
        )
        self.driver.find_element(By.XPATH,self.getcertificate_xpath).click()

    def clickonexamcheckbox(self):
        time.sleep(1)
        element = self.driver.find_element(By.XPATH,self.examcheckbox_xpath)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element.click()


    def clickoncertificatedelete(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.certificatedelete_xpath).click()

    def clickoncertificateconfirmdelete(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.certificateconfirmdelete_xpath))
        )
        self.driver.find_element(By.XPATH,self.certificateconfirmdelete_xpath).click()

    def clickontemplatedelete(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.templatedelete_xpath).click()

    def clickonquestionbankdelete(self):
        WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH,self.questionbankdelete_xpath))
        )
        self.driver.find_element(By.XPATH,self.questionbankdelete_xpath).click()

    def clickonacronymdelete(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.acronymdelete_xpath).click()
























