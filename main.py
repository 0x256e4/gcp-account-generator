#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options2 = Options()
#options.add_argument("--headless")
options2.add_argument("--headless")
driver = Firefox(options=options)
driver2 = Firefox(options=options2)

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

    def refreshEmail():
        WebDriverWait(driver, 300).until(lambda button: button.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div[2]/div[4]/div[3]/center/div/table/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[4]/td/table/tbody/tr/th[1]/table/tbody/tr/td/a"))
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/div[2]/div[4]/div[3]/center/div/table/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[4]/td/table/tbody/tr/th[1]/table/tbody/tr/td/a").click()

class QwiklabsAccount:
    def createAccount():
        #work in progress feature
        pass

    def createBonus():
        email = Email.getEmailName()
        driver2.get("https://inthecloud.withgoogle.com/google-cloud-skills/register.html")
        driver2.find_element_by_xpath("//*[@id='FirstName']").send_keys("tulang")
        driver2.find_element_by_xpath("//*[@id='LastName']").send_keys("ikan")
        driver2.find_element_by_xpath("//*[@id='Company']").send_keys("{}".format(email))
        driver2.find_element_by_xpath("//*[@id='Email']").send_keys("{}".format(email))
        driver2.find_element_by_xpath("/html/body/main/div[2]/div[1]/section[20]/div/div/form/div[6]/div/div/select/option[7]").click()
        driver2.find_element_by_xpath("//*[@id='Phone']").send_keys("1337")
        driver2.find_element_by_xpath("/html/body/main/div[2]/div[1]/section[20]/div/div/form/div[8]/div/div/select/option[107]").click()
        driver2.find_element_by_xpath("/html/body/main/div[2]/div[1]/section[20]/div/div/form/div[11]/div/div/select/option[2]").click()
        driver2.find_element_by_xpath("//*[@id='mktoRadio_959319_0']").click()
        driver2.find_element_by_xpath("//*[@id='mktoRadio_959305_0']").click()
        driver2.find_element_by_xpath("/html/body/main/div[2]/div[1]/section[20]/div/div/form/div[27]/span/button").click()



if __name__ == "__main__":
    Email.getEmail()
    print("Your current email account : {}".format(Email.getEmailName()))
    QwiklabsAccount.createBonus()
    print("Appeal is proceed")
    Email.refreshEmail()
