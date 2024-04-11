import asyncio
import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class Resources:
    ContentManagemaent_xpath = "//span[normalize-space()='Content']"
    Categorynew_xpath = "//button[normalize-space()='New']"
    categoryimage_xpath = "//input[@id='preview']"
    categoryimagesave_xpath = "//button[contains(text(),'Save')]"
    categorytitle_xpath = "//input[@id='outlined-basic']"
    categorydescription_xpath = "//textarea[@placeholder='Write a summary about (250 characters)']"
    categorypublic_xpath = "//input[@id='public']"
    categoryenable_xpath = "//div[@class='flexMinWidthRow alignCntr pdngHSM']//span[@aria-label='Click on the button to enable this category']"
    categorysave_xpath = "//button[normalize-space()='Save']"
    categorysearch_xpath = "//input[@type='search']"
    categoryclick_xpath = "//div[@class='flexCol CntimgOverlay pdngVSM categoryHover']"
    subcategorynew_xpath = "//button[@id='fade-button']"
    subcategorybutton_xpath = "//li[normalize-space()='Category']"
    subcategoryimage_xpath = "//input[@id='preview']"
    subcategoryimagesave_xpath = "//button[contains(text(),'Save')]"
    subcategorytitle_xpath = "//input[@id='outlined-basic']"
    subcategorydescription_xpath = "//textarea[@placeholder='Write a summary about (250 characters)']"
    subcategoryenable_xpath = "//span[@aria-label='Click on the button to enable this sub-category']//input[@type='checkbox']"
    subcategorysave_xpath = "//button[normalize-space()='Save']"
    contentnew_xpath = "//li[normalize-space()='Content']"
    addcategory_xpath = "//button[normalize-space()='Add CATEGORY']"
    categoryclose_xpath = "(//*[name()='svg'][@aria-label='Close'])[2]"
    contentbannerimage_xpath = "//input[@id='preview']"
    bannerimagesave_xpath = "(//button[text()='Save'])[3]"
    contenttitle_xpath = "//input[@id='title']"
    contentdescription_xpath = "//textarea[@id='summary']"
    contentcanshare_xpath = "//input[@id='canShare']"
    contentsectionname_xpath = "//input[@id='outlined-basic']"
    contentsectiondescription_xpath = "//div[@class='ql-editor ql-blank']//p"
    sectionimagepath_xpath = "//span[@class='pdngSM primaryTxt'][normalize-space()='Upload image']"
    sectionimageselect_xpath = "//span[@class='lightTxt headingSM pdngTXXS']"
    sectionimagedescription_xpath = "//textarea[@id='description']"
    sectionsave_xpath = "//button[contains(text(),'Save')]"
    contentpublish_xpath = "//button[normalize-space()='Publish']"
    menu_xpath = "//div[@class='flexAutoRow mobHamburgerBox mobShow alignCntr justifyCntr']"
    resources_xpath = "(//span[normalize-space()='Resources'])[2]"
    resourcescategorysearch_xpath = "//input[@placeholder='Search Categories']"
    logout_xpath = "//span[text()='Log out']"
    networkresources_xpath = "//button[normalize-space()='NETWORK RESOURCES']"
    searchcompanyname_xpath = "//input[@placeholder='Search Companies']"
    companyselect_xpath = "//div[@class='flexRow pdngXS brdrBtm']"
    contents_xpath="//button[normalize-space()='Contents']"
    searchcontents_xpath = "//input[@placeholder='Search Contents']"
    subcategoryclick_xpath = "//div[@class='flexCol CntimgOverlay pdngVSM categoryHover']"
    categorypartner_xpath = "//div[contains(@role,'presentation')]//div[5]//div[1]//span[1]//input[1]"
    categoryshare_xpath = "//div[@class='flexWrap ']//div[1]//div[1]//div[1]//div[2]//div[1]//div[3]//div[1]"
    categorysharepublic_xpath = "//input[@id='public']"
    categoryshareaccessyes_xpath = "//button[normalize-space()='Yes']"
    contentmanagementbreadcrumb_xpath = "//span[@class='primaryTxt pointer capitalTxt headingSM alignCntr breadCrumbTxt']"
    categoryedit_xpath = "//div[@class='flexAutoRow pdngTSM']//div[@aria-label='Edit']"
    categorydisable_xpath = "//div[contains(@class,'flexMinWidthRow alignCntr')]//input[contains(@type,'checkbox')]"
    categoryupdate_xpath = "//button[normalize-space()='Update']"
    subcategoryedit_xpath = "//div[@class='flexRow pdngXS']//div[@class='flexAutoRow pdngHXXS alignCntr']"
    subcategorydisable_xpath = "//div[contains(@class,'flexMinWidthRow alignCntr')]//span[contains(@aria-label,'Click on the button to disable this sub-category')]//input[contains(@type,'checkbox')]"
    subcategoryupdate_xpath = "//button[normalize-space()='Update']"
    contentviewmore_xpath = "//small[@class='primaryTxt pointer']"
    sectionedit_xpath = "//div[@class='flexAutoRow justifyEnd pdngXS ']//div[@aria-label='Edit']"
    sectionupdate_xpath = "//button[normalize-space()='Update']"
    contentdelete_xpath = "//div[@aria-label='Delete']"
    contentconfirmdelete_xpath = "//button[normalize-space()='Delete']"
    subcategorydelete_xpath = "//div[@aria-label='Delete']"
    Closetoaster_xpath = "//button[@class='Toastify__close-button Toastify__close-button--light']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]"
    contentscroll_xpath = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/div[1]"
    scrollpublic_xpath = "//label[@id='outlined-basic-label']"
    uploadvideo_xpath = "//span[normalize-space()='Upload Video files or URL']"
    videoinput_xpath = "//input[@placeholder='Add YouTube Video URL here']"
    uploadvideofile_xpath = "//button[normalize-space()='Upload Files']"
    addvideo_xpath = "//button[normalize-space()='Add']"
    backresources_xpath = "//span[text()='My Resources']"
    contentclose_xpath = "//button[@aria-label='Close']"
    videosbutton_xpath = "//button[normalize-space()='Videos']"
    videoselect_xpath = "//h4[contains(text(),'PeopleLink at InfoComm 2020 - One of the largest A')]"
    videoshare_xpath = "//div[@class='flexInline justifyEnd pointer']"







    def __init__(self, driver):
        self.driver = driver

    def clickClosetoaster(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Closetoaster_xpath))
        )
        element.click()
        time.sleep(2)

    def scrollcontent(self):

        element = self.driver.find_element(By.XPATH,self.contentscroll_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)

    def scrollpublic(self):
        element = self.driver.find_element(By.XPATH, self.scrollpublic_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)



    def clickonuploadvideo(self):
        time.sleep(2)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.uploadvideo_xpath).click()

    def setvideoinput(self,videoinput):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.videoinput_xpath).send_keys(videoinput)

    def clickonuploadvideofile(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.uploadvideofile_xpath).click()

    def clickonaddvideo(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.addvideo_xpath).click()

    def clickonbackresources(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.backresources_xpath).click()

    def clickoncontentclose(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.contentclose_xpath).click()

    def clickonvideosbutton(self):
        # time.sleep(1)
        # self.driver.find_element(By.XPATH,self.videosbutton_xpath).click()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.videosbutton_xpath))
        )
        element.click()

    def clickonvideoselect(self):
        time.sleep(1)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, self.videoselect_xpath))
        # )
        # element.click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.videoselect_xpath).click()
        time.sleep(1)

    def clickonvideoshare(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.videoshare_xpath).click()


    def clickoncontentmanagement(self):
        self.driver.find_element(By.XPATH,self.ContentManagemaent_xpath).click()

    def clickoncategorynew(self):
        self.driver.find_element(By.XPATH,self.Categorynew_xpath).click()

    def setcategoryimage(self, absolute_path7):
        # self.driver.find_element(By.XPATH,self.gallery_xpath).send_keys(gallery)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.categoryimage_xpath).send_keys(absolute_path7)
        time.sleep(2)

    def clickoncategoryimagesave(self):
        self.driver.find_element(By.XPATH,self.categoryimagesave_xpath).click()

    def setcategorytitle(self,categorytitle):
        self.driver.find_element(By.XPATH,self.categorytitle_xpath).send_keys(categorytitle)

    def setcategorydescription(self, categorydescription):
        self.driver.find_element(By.XPATH, self.categorydescription_xpath).send_keys(categorydescription)
        time.sleep(2)

    def clickoncategorypublic(self):

            time.sleep(2)
            category_public_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.categorypublic_xpath))
        )

            category_public_element.click()

    def clickoncategoryenable(self):
        category_enable_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.categoryenable_xpath))
        )
        category_enable_element.click()

    def clickoncategorysave(self):
        category_save_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.categorysave_xpath))
        )
        category_save_element.click()

    def setcategorysearch(self, categorysearch):
        time.sleep(1)
        category_search_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.categorysearch_xpath))
        )
        category_search_element.send_keys(categorysearch)

    def clickoncategoryclick(self):
        self.driver.find_element(By.XPATH,self.categoryclick_xpath).click()

    def clickonsubcategorynew(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.subcategorynew_xpath).click()

    def clickonsubcategorybutton(self):
        self.driver.find_element(By.XPATH,self.subcategorybutton_xpath).click()

    def setsubcategoryimage(self,absolute_path8):
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.categoryimage_xpath).send_keys(absolute_path8)
        time.sleep(2)

    def clickonsubcategoryimagesave(self):
        self.driver.find_element(By.XPATH,self.subcategoryimagesave_xpath).click()

    def setsubcategorytitle(self,subcategorytitle):
        self.driver.find_element(By.XPATH,self.subcategorytitle_xpath).send_keys(subcategorytitle)

    def setsubcategorydescription(self,subcategorydescription):
        self.driver.find_element(By.XPATH,self.subcategorydescription_xpath).send_keys(subcategorydescription)

    def clickonsubcategoryenable(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.subcategoryenable_xpath).click()

    def clickonsubcategorysave(self):
        self.driver.find_element(By.XPATH,self.subcategorysave_xpath).click()

    def clickoncontentnew(self):
        self.driver.find_element(By.XPATH,self.contentnew_xpath).click()

    def clickonaddcategory(self):
        time.sleep(1)
        # WebDriverWait(self.driver,20).until(
        #     EC.element_to_be_clickable((By.XPATH,self.addcategory_xpath))
        # )
        self.driver.find_element(By.XPATH,self.addcategory_xpath).click()

    def clickoncategoryclose(self):
        # self.driver.find_element(By.XPATH,self.categoryclose_xpath).click()
        time.sleep(1)
        category_close_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.categoryclose_xpath))
        )
        category_close_element.click()

    def setcontentbannerimage(self,absolute_path1):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.contentbannerimage_xpath).send_keys(absolute_path1)

    def clickonbannerimagesave(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.bannerimagesave_xpath).click()


    def setcontenttitle(self,contenttitle):
        self.driver.find_element(By.XPATH,self.contenttitle_xpath).send_keys(contenttitle)

    def setcontentdescription(self,contentdescription):
        self.driver.find_element(By.XPATH,self.contentdescription_xpath).send_keys(contentdescription)

    def clickoncontentcanshare(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.contentcanshare_xpath).click()

    def setcontentsectionname(self,contentsectionname):
        self.driver.find_element(By.XPATH,self.contentsectionname_xpath).send_keys(contentsectionname)

    def setcontentsectiondescription(self,contentsectiondescription):
        self.driver.find_element(By.XPATH,self.contentsectiondescription_xpath).send_keys(contentsectiondescription)

    def clickonsectionimagepath(self):
        time.sleep(2)
        actions = ActionChains(self.driver)

        # Press the PAGE_DOWN key to scroll down
        actions.send_keys(Keys.PAGE_DOWN)

        # Perform the scrolling action
        actions.perform()
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.sectionimagepath_xpath).click()
        time.sleep(2)
        # section_image_path = WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located((By.XPATH, self.sectionimagepath_xpath)))
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", section_image_path)
        #
        # section_image_path.click()

    def clickonsectionimageselect(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.sectionimageselect_xpath).click()


    def setsectionimageselect(self, absolute_path1):
         time.sleep(3)
         self.driver.find_element(By.XPATH, self.sectionimageselect_xpath).send_keys(absolute_path1)
         time.sleep(2)

    def setsectionimagedescription(self,sectionimagedescription):
        self.driver.find_element(By.XPATH,self.sectionimagedescription_xpath).send_keys(sectionimagedescription)

    def clickonsectionsave(self):
        time.sleep(2)
        # actions = ActionChains(self.driver)
        #
        # # Press the PAGE_DOWN key to scroll down
        # actions.send_keys(Keys.PAGE_DOWN)
        #
        # # Perform the scrolling action
        # actions.perform()
        # time.sleep(6)
        # self.driver.find_element(By.XPATH,self.sectionsave_xpath).click()
        # time.sleep(2)
        section_image_path = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.sectionsave_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", section_image_path)
        time.sleep(2)

        section_image_path.click()

    def clickoncontentpublish(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.contentpublish_xpath).click()
        time.sleep(1)

    def clickonresources(self):
        time.sleep(1)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.menu_xpath)))
        self.driver.find_element(By.XPATH, self.menu_xpath).click()
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.resources_xpath)))
        self.driver.find_element(By.XPATH,self.resources_xpath).click()
        time.sleep(2)



    def setresourcescategorysearch(self, resourcescategorysearch):
        time.sleep(3)
        category_search_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.resourcescategorysearch_xpath))
        )
        category_search_element.send_keys(resourcescategorysearch)

    def clickonlogout(self):
        logout_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.logout_xpath))
        )

        # Click on the element
        logout_button.click()
        time.sleep(2)

    def clickonnetworkresources(self):
        time.sleep(1)
        network_resources_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.networkresources_xpath))
        )

        # Click on the element
        network_resources_element.click()

    def setsearchcompanyname(self, companyname):
        time.sleep(1)
        companyname_search_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.searchcompanyname_xpath))
        )
        companyname_search_element.send_keys(companyname)
        time.sleep(1)

    def clickoncompanyselect(self):
        time.sleep(2)
        company_select_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.companyselect_xpath))
        )

        # Click on the element
        company_select_element.click()

    def clickoncontents(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,self.contents_xpath).click()
        time.sleep(1)

    def setsearchcontents(self,searchcontents):
        time.sleep(2)
        try:
            asyncio.sleep(2)
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, self.searchcontents_xpath).send_keys(searchcontents))
        )
        except Exception as e:
            self.driver.find_element(By.XPATH,self.searchcontents_xpath).send_keys(searchcontents)
            time.sleep(1)

    def clickonsubcategoryclick(self):
        self.driver.find_element(By.XPATH,self.subcategoryclick_xpath).click()

    def clickoncategorypartner(self):
        try:
            time.sleep(3)  # Add a sleep to wait for the banner to display (if needed)
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.categorypartner_xpath))
            ).click()
        except Exception as e:
            print("Exception occurred while waiting for or clicking the element:", e)
            # Handle the exception as needed, such as clicking the element without waiting
            self.driver.find_element(By.XPATH, self.categorypartner_xpath).click()
    def clickoncategoryshare(self):
        self.driver.find_element(By.XPATH,self.categoryshare_xpath).click()

    def clickoncategorysharepublic(self):
        self.driver.find_element(By.XPATH,self.categorysharepublic_xpath).click()

    def clickoncategoryshareaccessyes(self):
        self.driver.find_element(By.XPATH,self.categoryshareaccessyes_xpath).click()

    def clickoncontentmanagementbreadcrumb(self):
        # self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        # contentmanagement_breadcrumb = WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located((By.XPATH, self.contentmanagementbreadcrumb_xpath))
        # )
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", contentmanagement_breadcrumb)
        # time.sleep(2)
        #
        # # Scroll down
        # WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, self.contentmanagementbreadcrumb_xpath)))
        # time.sleep(2)
        #
        # contentmanagement_breadcrumb.click()
        contentmanagement_breadcrumb = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.contentmanagementbreadcrumb_xpath))
        )

        # Scroll to the element using Actions class
        actions = ActionChains(self.driver)
        actions.move_to_element(contentmanagement_breadcrumb).perform()

        # Wait for the element to be clickable
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.contentmanagementbreadcrumb_xpath))
        )

        # Click on the element
        contentmanagement_breadcrumb.click()
        time.sleep(1)

    def clickoncategoryedit(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.categoryedit_xpath).click()

    def clickoncategorydisable(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.categorydisable_xpath).click()

    def clickoncategoryupdate(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.categoryupdate_xpath).click()

    def clickonsubcategoryedit(self):
        time.sleep(2)

        element = self.driver.find_element(By.XPATH, self.subcategoryedit_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'start', inline: 'nearest'});", element)
        element.click()

    def clickonsubcategorydisable(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.subcategorydisable_xpath).click()

    def clickonsubcategoryupdate(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH,self.subcategoryupdate_xpath).click()

    def clickoncontentviewmore(self):
        time.sleep(2)
        content_viewmore = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.contentviewmore_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", content_viewmore)
        time.sleep(2)

        content_viewmore.click()

    def clickonsectionedit(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.sectionedit_xpath).click()

    def clickonsectionupdate(self):
        time.sleep(2)
        section_update = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.sectionupdate_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", section_update)
        time.sleep(2)

        section_update.click()
        time.sleep(2)

    def clickoncontentdelete(self):
        time.sleep(1)
        delete_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.contentdelete_xpath))
        )

        # Click on the delete button
        delete_button.click()

    def clickoncontentconfirmdelete(self):
        time.sleep(2)
        confirmdelete_button = WebDriverWait(self.driver,20).until(
            EC.element_to_be_clickable((By.XPATH, self.contentconfirmdelete_xpath))
        )

        confirmdelete_button.click()
        time.sleep(1)

    def clickonsubcategorydelete(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.subcategorydelete_xpath))
        )
        element.click()
        time.sleep(1)






