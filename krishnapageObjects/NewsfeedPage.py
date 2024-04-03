import time
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class NewsFeed:
    what_xpath = "//span[@class='pdngXS brdrBlackSM postWidth brdrRadiusXSM pointer lightTxt feedHover']"
    whats_txtbox_xpath = "//div[@class='ql-editor ql-blank']"
    whatsedit_txtbox_xpath = "//div[@class='ql-editor']"
    post_xpath = "//button[text()='Post']"
    logout_xpath = "//span[text()='Log out']"
    public_xpath = "//input[@id='public']"
    employeechck_xpath = "//div[@class='flexCol brdrBSM']//div[1]//div[1]"
    partnerchck_xpath = "//span[normalize-space()='partner']"
    statuschck_xpath = "//input[@id='activeType']"
    threedots_xpath = "//div[@class='flexAutoRow alignCntr justifyCntr']"
    archive_xpath = "(//li[@class='MuiButtonBase-root MuiMenuItem-root MuiMenuItem-gutters MuiMenuItem-root MuiMenuItem-gutters css-1slzbpg'])[2]"
    gallery_xpath = "//input[@id='imageType']"
    image_xpath = "//div[@class='auto-grid']//div[1]//span[1]//img[1]"
    video_xpath = "//input[@id='videoType']"
    youtube_xpath = "//span[@title='Youtube Url']"
    youtubeurl_xpath = "//input[@placeholder='Paste URL here']"
    done_xpath = "//button[normalize-space()='Done']"
    threedot_xpath = "(//*[name()='svg'][@class='pointer'])[1]"
    edit_xpath = "//li[normalize-space()='Edit']"
    update_xpath = "//button[text()='Update post']"
    delete_xpath = "//li[normalize-space()='Delete']"
    deletechckboox_xpath = "//input[@name='archive']"
    deletebutton_xpath = "//button[normalize-space()='Delete']"
    bookmark_xpath = "//li[normalize-space()='Bookmark']"
    explore_xpath = "//span[@aria-label='Explore bookmarks']"
    remove_xpath = "//span[text()='Remove']"
    filter_xpath = "//span[text()='Filter']"
    all_xpath = "//input[@id='feedsAllField']"
    self_xpath = "//input[@id='feedsSelfField']"
    apply_xpath = "//button[normalize-space()='Apply']"
    share_xpath = "//span[text()='Share']"
    whatsapp_xpath = "//button[@aria-label='whatsapp']"
    facebook_xpath = "//button[@aria-label='facebook']"
    twitter_xpath = "//button[@aria-label='twitter']"
    linkedin_xpath = "//button[@aria-label='linkedin']"
    telegram_xpath = "//button[@aria-label='telegram']"
    instagram_xpath = "//div[@class='flexCol fxdSocialMediaSlider slideIn']//div[6]//div[1]//div[1]//div[1]"
    gmail_xpath = "//div[@class='flexCol fxdSocialMediaSlider slideIn']//div[7]//div[1]//div[1]//div[1]"
    comment_xpath = "(//span[text()='Comment'])[1]"
    commenttxtare_xpath = "//textarea[@id='outlined-basic']"
    send_xpath = "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorPrimary MuiButton-disableElevation MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-colorPrimary MuiButton-disableElevation primaryBg brdrRadius50 imgAvatarSM css-191um2i']"
    cancelcmnt_xpath = "//div[@class='flexAutoRow pointer pdngRXS']"
    comments_xpath = "(//span[text()='Comment'])[2]"
    replycmnt_xpath = "//span[text()='Reply']"
    replytxt_xpath = "//textarea[@id='outlined-adornment-weight']"
    replysend_xpath = "//*[@id='root']/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/div"
    viewreply_xpath = "//legend[@class='lightTxt headingSM pointer pdngHSM']"
    commentthreedot_xpath = "//span[@class='pointer']"
    commentedit_xpath = "//div[@id='demo-positioned-menu']//li[1]"
    commenteditsend_CSS_SELECTOR = "svg[data-testid='SendIcon']"
    commentdelete_xpath = "//span[@class='flexInline pointer']"
    commentconfirmdelete_xpath = "//button[normalize-space()='Delete']"
    rolechange_xpath = "//div[@id='demo-multiple-name']"
    employeeselect_xpath = "//li[@data-value='true']"
    search_xpath = "//input[@placeholder='Search All feeds...']"
    like_xpath = "//span[text()='Like']"
    dislike_xpath = "(//span[text()='Like'])[2]"

    def __init__(self, driver):
        self.driver = driver

    def clickonrolechange(self):
        self.driver.find_element(By.XPATH, self.rolechange_xpath).click()

    def clickonemployeeselect(self):
        self.driver.find_element(By.XPATH, self.employeeselect_xpath).click()

    def setsearch(self, search):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.search_xpath).send_keys(search)
        time.sleep(1)

    def clickonlike(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.like_xpath).click()

    def clickondislike(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.dislike_xpath).click()

    def clickOnwhat(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.what_xpath))
        )

        # Click on the element
        element.click()

    def setwhats(self, whats):
        text_box = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.whats_txtbox_xpath))
        )

        # Send keys to the text box
        text_box.send_keys(whats)
        time.sleep(2)

    def clickonpost(self):
        time.sleep(3)
        post_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.post_xpath))
        )

        # Click on the element
        post_button.click()
        time.sleep(1)

    def clickonlogout(self):
        logout_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.logout_xpath))
        )

        # Click on the element
        logout_button.click()
        time.sleep(2)

    def setwhatso(self, whatso):
        text_box = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.whats_txtbox_xpath))
        )

        # Send keys to the text box
        text_box.send_keys(whatso)
        time.sleep(2)

    def clickonpublic(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.public_xpath).click()
        # time.sleep(3)
        # public_button = WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, self.public_xpath))
        # )
        #
        # # Click on the element
        # public_button.click()

    def clickonemp(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.employeechck_xpath).click()

    def clickonpartner(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.partnerchck_xpath).click()

    def setwhatson(self, whatson):
        text_box = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.whats_txtbox_xpath))
        )

        # Send keys to the text box
        text_box.send_keys(whatson)

    def clickonstatus(self):
        self.driver.find_element(By.XPATH, self.statuschck_xpath).click()
        # status_check = WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, self.statuschck_xpath))
        # )
        #
        # # Click on the element
        # status_check.click()

    def clickonthreedots(self):
        self.driver.find_element(By.XPATH, self.threedots_xpath).click()

    def clickonarchive(self):
        self.driver.find_element(By.XPATH, self.archive_xpath).click()

    def setgallery(self, absolute_path1):
        # self.driver.find_element(By.XPATH,self.gallery_xpath).send_keys(gallery)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.gallery_xpath).send_keys(absolute_path1)
        time.sleep(2)

    def setgallery(self, absolute_path2):
        # self.driver.find_element(By.XPATH,self.gallery_xpath).send_keys(gallery)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.gallery_xpath).send_keys(absolute_path2)
        time.sleep(2)

    def setgallery(self, absolute_path3):
        # self.driver.find_element(By.XPATH,self.gallery_xpath).send_keys(gallery)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.gallery_xpath).send_keys(absolute_path3)
        time.sleep(2)

    def setgallery(self, absolute_path4):
        # self.driver.find_element(By.XPATH,self.gallery_xpath).send_keys(gallery)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.gallery_xpath).send_keys(absolute_path4)
        time.sleep(2)

    def setgallery(self, absolute_path5):
        # self.driver.find_element(By.XPATH,self.gallery_xpath).send_keys(gallery)
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, self.gallery_xpath).send_keys(absolute_path5)
        time.sleep(2)

    def clickonimage(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.image_xpath).click()

    def setoneimage(self, oneimage):
        text_box = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.whats_txtbox_xpath))
        )

        text_box.send_keys(oneimage)

    def imageicon(self):
        imageicon = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@title='Upload image']"))
        )
        imageicon.click()
        imageicon1 = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='uploadLogoWidth pointer']"))
        )
        imageicon1.click()

    def uploadimage(self, fiveimages):
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//body/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/label[1]"))
        )
        element.send_keys(fiveimages)

        # element_to_hover_over = WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//body/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/label[1]"))
        # )
        # Perform mouse hover action
        # ActionChains(self.driver).move_to_element(element_to_hover_over).perform()

        # # Wait for the element to be clickable
        # element = WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//body/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/label[1]"))
        # )
        # # element.click()
        # # Send keys after hover
        # element.send_keys(fiveimages)

    def clickuploadimage(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(//div[@role='presentation'])[3]"))
        )
        element.click()

    def AddClick(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Add')]"))
        )
        element.send_keys()


    def setfiveimages(self, fiveimages):
        text_box = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, self.whats_txtbox_xpath))
        )

        # Send keys to the text box
        text_box.send_keys(fiveimages)

    def setvideo(self, absolute_pathvideo):
        # self.driver.find_element(By.XPATH,self.gallery_xpath).send_keys(gallery)

        time.sleep(2)
        self.driver.find_element(By.XPATH, self.video_xpath).send_keys(absolute_pathvideo)
        time.sleep(2)

    def setwhatvideo(self, whatvideo):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.whats_txtbox_xpath).send_keys(whatvideo)

    def setwhatvideos(self, whatvideos):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.whats_txtbox_xpath).send_keys(whatvideos)

    def setwhatyoutube(self, whatyoutube):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.whats_txtbox_xpath).send_keys(whatyoutube)

    def clickonyoutube(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.youtube_xpath).click()

    def setyoutubeurl(self, youtubeurl):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.youtubeurl_xpath).send_keys(youtubeurl)

    def clickondone(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.done_xpath).click()
        time.sleep(1)

    def clickonthreedot(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.threedot_xpath).click()

    def clickonedit(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.edit_xpath).click()

    def setwhatedit(self, whatedit):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.whatsedit_txtbox_xpath).send_keys(whatedit)

    def clickonupdate(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.update_xpath).click()

    def clickondelete(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.delete_xpath).click()

    def clickondeletecheckbox(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.deletechckboox_xpath).click()

    def clickondeletebutton(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.deletebutton_xpath).click()
        time.sleep(1)

    def clickonbookmark(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.bookmark_xpath).click()
        time.sleep(1)

    def clickonexplore(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.explore_xpath).click()
        time.sleep(1)

    def clickonremove(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.remove_xpath).click()

    def clickonfilter(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.filter_xpath).click()

    def clickonall(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.all_xpath).click()

    def clickonself(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.self_xpath).click()

    def clickonapply(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.apply_xpath).click()

    def clickonshare(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, self.share_xpath).click()

    def clickonwhatsapp(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.whatsapp_xpath).click()

    def clickonfacebook(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.facebook_xpath).click()

    def clickontwitter(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.twitter_xpath).click()

    def clickonlinkedin(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.linkedin_xpath).click()

    def clickontelegram(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.telegram_xpath).click()

    def clickoninstagram(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.instagram_xpath).click()

    def clickongmail(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.gmail_xpath).click()

    def clickoncomment(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.comment_xpath).click()

    def setcommenttext(self, commenttext):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.commenttxtare_xpath).send_keys(commenttext)

    def clickonsend(self):
        time.sleep(2)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.send_xpath).click()

    def clickoncancelcmnt(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.cancelcmnt_xpath).click()

    def clickoncomments(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.comments_xpath).click()

    def clickonreplycmnt(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.replycmnt_xpath).click()

    def setreplytext(self, replytext):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.replytxt_xpath).send_keys(replytext)

    def clickonreplysend(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.replysend_xpath).click()

    def clickonviewreply(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.viewreply_xpath).click()

    def clickoncommentthreedot(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.commentthreedot_xpath).click()

    def clickoncommentedit(self):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.commentedit_xpath).click()

    def setcommentedittext(self, commentedittext):
        time.sleep(1)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.replytxt_xpath).send_keys(commentedittext)

    def clickoncommenteditsend(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CSS_SELECTOR, self.commenteditsend_CSS_SELECTOR).click()

    def clickoncommentdelete(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.commentdelete_xpath).click()

    def clickoncommentconfirmdelete(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.commentconfirmdelete_xpath).click()
