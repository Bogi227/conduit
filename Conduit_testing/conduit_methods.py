def conduit_login(driver):
    driver.find_element_by_xpath('//a[@href="#/login"]').click()
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys("testmail61@test.hu")
    driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("Testpass1")
    driver.find_element_by_xpath('//*[@id="app"]//form/button').click()

def conduit_logout(driver):
    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[5]/a').click()
