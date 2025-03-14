from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from conduit_methods import *


class TestConduit(object):
    def setup(self):
        browser_options = Options()
        browser_options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.driver.get("http://localhost:1667/")
        time.sleep(3)

    def teardown(self):
        self.driver.quit()

    # Regisztráció
    def test_registration(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys("testname1")
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("testmail61@test.hu")
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
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[@href="#/login"]').click()
        self.driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("testmail61@test.hu")
        self.driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Testpass1")
        self.driver.find_element_by_xpath('//*[@id="app"]//form/button').click()
        time.sleep(3)
        my_feed = self.driver.find_element_by_xpath('//a[@href="#/my-feed"]')
        assert my_feed.text == "Your Feed"

    # Listázás
    def test_listing(self):
        conduit_login(self.driver)
        time.sleep(5)
        article_titles = self.driver.find_elements_by_xpath('//a[@class="preview-link"]')
        assert article_titles != []


    # Kijelentkezés
    def test_logout(self):
        conduit_login(self.driver)
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a').click()
        time.sleep(5)
        assert self.driver.find_element_by_xpath('//a[@href="#/login"]').text == "Sign in"

    # Lapozás
    def test_pagination(self):
        conduit_login(self.driver)
        time.sleep(4)
        self.driver.find_element_by_xpath("//a[@class='page-link'][contains(text(),'2')]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//a[@class='page-link'][contains(text(),'1')]").click()
        assert self.driver.find_element_by_xpath("//li[@class='page-item active']").text == "1"

    # Post létrehozása
    def test_new_post(self):
        conduit_login(self.driver)
        time.sleep(3)
        self.driver.find_element_by_xpath("//a[@href='#/editor']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(
            "Test Title")
        self.driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]').send_keys(
            "test test")
        self.driver.find_element_by_xpath("//textarea[@placeholder='Write your article (in markdown)']").send_keys(
            "test test test")
        self.driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys("TEST")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        assert self.driver.find_element_by_xpath("//h1").text == "Test Title"

    # Post törlése
    def test_delete_post(self):
        conduit_login(self.driver)
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[@href='#/editor']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(
            "Test Title Del")
        self.driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]').send_keys(
            "test delete")
        self.driver.find_element_by_xpath("//textarea[@placeholder='Write your article (in markdown)']").send_keys(
            "test test delete")
        self.driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys("TEST")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[@class='btn btn-outline-danger btn-sm']//span[1]").click()
        time.sleep(3)
        delete_test = self.driver.find_elements_by_xpath('//h1')
        for i in delete_test:
            assert i.text != "Test Title Del"

    # Post módosítása
    def test_modify_post(self):
        conduit_login(self.driver)
        time.sleep(8)
        self.driver.find_element_by_xpath("//a[@href='#/editor']").click()
        time.sleep(4)
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(
            "Test Mod Title")
        self.driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]').send_keys(
            "test modify")
        self.driver.find_element_by_xpath("//textarea[@placeholder='Write your article (in markdown)']").send_keys(
            "test test modify")
        self.driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys("modify1")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//a[@class='btn btn-sm btn-outline-secondary']//span[1]").click()
        time.sleep(4)
        self.driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys("modify2")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(6)
        assert self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/div[2]/a[2]').text == "modify2"


    # Sorozatos adatbevitel
    def test_upload_data(self):
        conduit_login(self.driver)
        time.sleep(4)
        self.driver.find_element_by_xpath("//a[@href='#/editor']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@placeholder="Article Title"]').send_keys(
            "Test Data2")
        self.driver.find_element_by_xpath('//input[@placeholder="What\'s this article about?"]').send_keys(
            "test test data")
        self.driver.find_element_by_xpath("//textarea[@placeholder='Write your article (in markdown)']").send_keys(
            "test test test data")
        self.driver.find_element_by_xpath("//input[@placeholder='Enter tags']").send_keys("data")
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(4)
        comment_field = self.driver.find_element_by_xpath("//textarea[@class='form-control']")
        post_comment_btn = self.driver.find_element_by_xpath("//button[text()='Post Comment']")
        with open('Conduit_testing/data.txt', 'r', encoding='utf-8') as f:
            comment = f.readlines()
            for row in comment:
                comment_field.send_keys(row)
                time.sleep(3)
                post_comment_btn.click()

    # Adat lementése
    def test_saving_data(self):
        conduit_login(self.driver)
        time.sleep(6)
        self.driver.find_element_by_xpath("//li[4]//a[1]").click()
        time.sleep(4)
        data_name = self.driver.find_element_by_xpath('//h4').text
        with open('savedata.txt', 'w') as file:
            file.write(data_name)
        with open('Conduit_testing/savedata.txt', 'r') as file_b:
            txt_content = file_b.read()









