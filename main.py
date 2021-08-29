#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--headless")
driver = Firefox(options=options)

class Email:
    def getEmail():
        driver.get("https://generator.email")
        inputDomain = driver.find_element_by_xpath("//*[@id='domainName2']")
        inputDomain.click()
        inputDomain.send_keys(Keys.CONTROL, 'a')
        inputDomain.send_keys('.', 's', 'i', 't', 'e')
        time.sleep(2)
        inputDomain.send_keys(Keys.DOWN)
        inputDomain.send_keys(Keys.RETURN)

    def getEmailName():
        emailId = driver.find_element_by_id("email_ch_text")
        emailId.click()
        time.sleep(2)
        email = emailId.get_attribute("innerHTML")
        return email


if __name__ == "__main__":
    Email.getEmail()
    print("Your current email account : {}".format(Email.getEmailName()))
