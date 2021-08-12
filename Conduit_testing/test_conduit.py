import csv
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
import time
from conduit_methods import *


class TestConduit(object):
    def setup(self):
        # browser_options = Options()
        # browser_options.headless = False
        # self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver = webdriver.Chrome("G:\\Desktop\\chromedriver.exe")
        self.driver.get("http://localhost:1667/")
        time.sleep(3)

    def teardown(self):
        self.driver.quit()

    # Regisztráció
    def test_registration(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys("testname1")
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("testmail8@test.hu")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Testpass1")
        self.driver.find_element_by_xpath('//*[@id="app"]//form/button').click()
        time.sleep(3)

        # Regisztráció sikeressége
        success_window = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]')
        assert success_window.text == "Your registration was successful!"
        self.driver.find_element_by_xpath('//button[text()="OK"]').click()

    # # Sütik elfogadása
    # def test_cookies(self):
    #     self.driver.find_element_by_xpath\
    #         ('//button[@class="cookie__bar__buttons__button cookie__bar__buttons__button--accept"]').click()
    #     time.sleep(3)
    #     assert self.driver.find_elements_by_xpath('//button') == []
    #
    # # Bejelentkezés
    # def test_login(self):
    #     conduit_registration(self.driver)
    #     conduit_logout(self.driver)
    #     time.sleep(1)
    #     self.driver.find_element_by_xpath('//a[@href="#/login"]').click()
    #     self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("testmail4@test.hu")
    #     self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Testpass1")
    #     self.driver.find_element_by_xpath('//*[@id="app"]//form/button').click()
    #     time.sleep(3)
    #     my_feed = self.driver.find_element_by_xpath('//a[@href="#/my-feed"]')
    #     assert my_feed.text == "Your Feed"
    #
    # # Listázás
    # def test_listing(self):
    #     conduit_registration(self.driver)
    #     time.sleep(3)
    #     article_titles = self.driver.find_elements_by_xpath('//a[@class="preview-link"]')
    #     assert article_titles != []
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
    #     self.driver.maximize_window()
    #     conduit_registration(self.driver)
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("//a[@class='page-link'][contains(text(),'2')]").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("//a[@class='page-link'][contains(text(),'1')]").click()
