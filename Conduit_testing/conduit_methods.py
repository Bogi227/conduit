import time


def conduit_registration(driver):
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder="Username"]').send_keys("testname1")
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("testmail29@test.hu")
    driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Testpass1")
    driver.find_element_by_xpath('//*[@id="app"]//form/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('//button[text()="OK"]').click()


def conduit_logout(driver):
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a').click()
