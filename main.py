from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # For simulating keyboard inputs
import time
import random

from utils import move_download

# Provide the path to the ChromeDriver
service = Service('./chromedriver/chromedriver')

# Initialize the WebDriver with the service object
driver = webdriver.Chrome(service=service)

driver.get('https://www.unternehmensregister.de/')
driver.implicitly_wait(5)

button_cookie = driver.find_element(By.XPATH, '//button[@class="btn btn-gray"]')
button_cookie.click()

input_field = driver.find_element(By.XPATH, '//input[@id="globalSearchForm:extendedResearchCompanyName"]')
company = 'GetCouped Technologies GmbH'
input_field.send_keys(company)

button = driver.find_element(By.XPATH, '//input[@id="globalSearchForm:btnExecuteSearchOld"]')
driver.implicitly_wait(5)
button.click()
driver.implicitly_wait(5)

regGer = driver.find_element(By.XPATH, '//a[contains(@href, "registerPortalAdvice.html")]')
regGer.click()
driver.implicitly_wait(5)

regGerAnz = driver.find_element(By.XPATH, '//a[contains(@href, "registerPortal.html")]')
regGerAnz.click()
driver.implicitly_wait(5)

dk = driver.find_element(By.XPATH, '//a[contains(text(), "DK")]')
dk.click()


dkReg = driver.find_element(By.XPATH, '//a[contains(text(), "Dokumente zur Registernummer")]')
dkReg.click()
driver.implicitly_wait(5)

gesList = driver.find_element(By.XPATH, '//a[starts-with(text(), "Liste der Gesellschafter")]')
gesList.click()
driver.implicitly_wait(5)

totalGesListen = len(driver.find_elements(By.XPATH, '//a[starts-with(text(), "Liste der Gesellschafter - Aufnahme in den")]'))

print(totalGesListen)

for i in range(totalGesListen):
    back = -1

    gesListen = driver.find_elements(By.XPATH, '//a[starts-with(text(), "Liste der Gesellschafter - Aufnahme in den")]')
    gesListen[i].click()
    back+=1

    driver.implicitly_wait(10)
    add2cart = driver.find_element(By.XPATH, '//input[@id="add2cart"]')
    add2cart.click()
    back+=1

    driver.implicitly_wait(5)
    viewCart = driver.find_element(By.XPATH, '//a[contains(@href, "doccart.html") and @class="btn btn-green"]')
    viewCart.click()
    back+=1
    
    driver.implicitly_wait(5)
    submit = driver.find_element(By.XPATH, '//input[@type="submit" and @class="btn btn-green"]')
    submit.click()
    back+=1
    
    driver.implicitly_wait(5)
    submit = driver.find_element(By.XPATH, '//input[@type="submit" and @class="btn btn-green"]')
    submit.click()
    back+=1
    
    driver.implicitly_wait(5)
    docCart = driver.find_element(By.XPATH, '//a[contains(@href, "doccart.html") and @class="btn btn-green"]')
    docCart.click()
    back+=1
    
    driver.implicitly_wait(5)
    download = driver.find_element(By.XPATH, '//a[contains(@href, "registerdocument.zip")]')
    download.click()
    back+=1

    for b in range(back):
        driver.back()

    time.sleep(random.uniform(3, 10))

    new_file_name = company + " " + str(i)

    move_download(new_file_name)

driver.close()