import csv
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from conduit_methods import *


class TestConduit(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        # self.driver = webdriver.Chrome("G:\\Desktop\\chromedriver.exe")
        self.driver.get("http://localhost:1667/")
        time.sleep(3)

    def teardown(self):
        self.driver.quit()

    # Regisztráció
    def test_registration(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys("testname1")
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("testmail11@test.hu")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Testpass1")
        self.driver.find_element_by_xpath('//*[@id="app"]//form/button').click()
        time.sleep(3)

        # Regisztráció sikeressége
        success_window = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]')
        assert success_window.text == "Your registration was successful!"
        self.driver.find_element_by_xpath('//button[text()="OK"]').click()

    # Sütik elfogadása
    def test_cookies(self):
        self.driver.find_element_by_xpath\
            ('//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]').click()
        time.sleep(3)
        assert self.driver.find_elements_by_xpath('//button') == []

    # Bejelentkezés
    def test_login(self):
        conduit_registration(self.driver)
        conduit_logout(self.driver)
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[@href="#/login"]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("testmail26@test.hu")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Testpass1")
        self.driver.find_element_by_xpath('//*[@id="app"]//form/button').click()
        time.sleep(3)
        my_feed = self.driver.find_element_by_xpath('//a[@href="#/my-feed"]')
        assert my_feed.text == "Your Feed"

    # Listázás
    def test_listing(self):
        conduit_registration(self.driver)
        time.sleep(3)
        article_titles = self.driver.find_elements_by_xpath('//a[@class="preview-link"]')
        assert article_titles != []
    #
    # # Kijelentkezés
    # def test_logout(self):
    #     conduit_registration(self.driver)
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a').click()
    #     time.sleep(3)
    #     assert self.driver.find_element_by_xpath('//a[@href="#/login"]').text == "Sign in"
    #
    # # Lapozás
    # def test_pagination(self):
    #     conduit_registration(self.driver)
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("//a[@class='page-link'][contains(text(),'2')]").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("//a[@class='page-link'][contains(text(),'1')]").click()
    #
    # def test_new_post(self):
    #     conduit_registration(self.driver)
    #     self.driver.find_element_by_xpath("//a[@href='#/editor']").click()
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(
    #         "Test Title")
    #     self.driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]').send_keys(
    #         "test test")
    #     self.driver.find_element_by_xpath("//textarea[@placeholder='Write your article (in markdown)']").send_keys(
    #         "test test test")
    #     self.driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys("TEST")
    #     self.driver.find_element_by_xpath("//button[contains(text(),'Publish Article')]").click()
    #     time.sleep(3)
    #     assert self.driver.find_element_by_xpath("//h1").text == "Test Title"
    #
    # def test_delete_post(self):
    #     conduit_registration(self.driver)
    #     self.driver.find_element_by_xpath("//a[@href='#/editor']").click()
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(
    #         "Test Title Del")
    #     self.driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]').send_keys(
    #         "test delete")
    #     self.driver.find_element_by_xpath("//textarea[@placeholder='Write your article (in markdown)']").send_keys(
    #         "test test delete")
    #     self.driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys("TEST")
    #     self.driver.find_element_by_xpath("//button[contains(text(),'Publish Article')]").click()
    #     time.sleep(3)
    #     self.driver.find_element_by_xpath("//button[@class='btn btn-outline-danger btn-sm']//span[1]").click()
    #     delete_test = self.driver.find_elements_by_xpath('//h1[text()="Test Title Del"]')
    #     assert len(delete_test) == 0

    # def test_save_data(self):
    #     conduit_registration(self.driver)
    #     self.driver.find_element_by_xpath("//a[@class ='nav-link'][normalize-space()='asdasd']").click()
    #     with open("profilename.txt", 'w+') as file:




