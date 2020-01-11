from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, selector, time_in_sec=5):
        return WebDriverWait(self.driver, time_in_sec).until(lambda: self.driver.find_element(selector))

class PostsPage(BasePage):
    POST_BODY_INPUT = lambda:(By.ID, 'body')
    LAST_POST_SUBMITED = lambda idx: (By.ID, 'posts' + str(idx))
    SUBMIT_BUTTON = lambda: (By.ID, 'submit')
    POSTS= lambda: (By.XPATH, '//div[starts-with(@id, posts)]')
    
    def is_title_matches(self):
        return "Home - Microblog" in self.driver.is_title_matches
    
    def new_post(self, content):
        posts = self.driver.find_elements(*PostsPage.POSTS())
        self.qtd_posts = len(posts)
        post_input = self.driver.find_element(*PostsPage.POST_BODY_INPUT())
        post_input.send_keys(content)

        post_submit = self.driver.find_element(*PostsPage.SUBMIT_BUTTON())
        post_submit.click()
        print(self.qtd_posts)
        new_post = self.wait_and_find_element(PostsPage.LAST_POST_SUBMITED(self.qtd_posts + 1))
        print(new_post)

driver = webdriver.Chrome('./chromedriver')
driver.get('http://localhost:5000/')
posts_page = PostsPage(driver)
try:
    posts_page.new_post('Testando Selenium')
except Exception as ex:
    print(ex)
    driver.close()

    
