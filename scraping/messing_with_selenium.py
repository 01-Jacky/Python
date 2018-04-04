import time
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def init_driver():
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, query):
    driver.get("http://www.google.com")
    try:
        box = driver.wait.until(EC.presence_of_element_located(
            (By.NAME, "q")))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.NAME, "btnK")))
        box.send_keys(query)
        button.click()
    except TimeoutException:
        print("Box or Button not found in google.com")

def login_linkedin(driver):
    driver.get("https://www.linkedin.com/")

    try:
        # Toggle to login
        # link = driver.wait.until(EC.presence_of_element_located(
        #     (By.LINK_TEXT, "Sign in")))
        # print('Ready to be toggled')
        # link.click()

        # Sign in
        box_login = driver.wait.until(EC.presence_of_element_located(
            (By.ID, "login-email")))
        box_password = driver.wait.until(EC.presence_of_element_located(
            (By.ID, "login-password")))
        button = driver.wait.until(EC.element_to_be_clickable(
            (By.ID, "login-submit")))

        box_login.send_keys('hklee310@gmail.com')
        box_password.send_keys('Winter1!')
        button.click()
    except TimeoutException:
        print("Failed to login")

    # try:
    #     # Get 1st 5
    #     driver.get("https://www.linkedin.com/jobs/search/?keywords=software%20intern&location=United%20States&locationId=us%3A0&sortBy=DD")
    #     driver.wait.until(EC.presence_of_element_located(
    #         (By.CLASS_NAME, "jobs-search-results")))
    #
    #     'job-card-search__company-name'
    #     html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    #     bsObj = BeautifulSoup(html, "html.parser")
    #     h4s = bsObj.findAll("h4", {"class": "job-card-search__company-name"})
    #     for h4 in h4s:
    #         print(h4.text)
    #     # innerHTML = driver.execute_script("return document.body.innerHTML")  # returns the inner HTML as a string
    #     time.sleep(5)
    #
    #     # Get next 5
    #     driver.get("https://www.linkedin.com/jobs/search/?keywords=software%20intern&location=United%20States&locationId=us%3A0&sortBy=DD&start=5")
    #     driver.wait.until(EC.presence_of_element_located(
    #         (By.CLASS_NAME, "jobs-search-results")))
    #
    #     'job-card-search__company-name'
    #     html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    #     bsObj = BeautifulSoup(html, "html.parser")
    #     h4s = bsObj.findAll("h4", {"class": "job-card-search__company-name"})
    #     for h4 in h4s:
    #         print(h4.text)
    #     # innerHTML = driver.execute_script("return document.body.innerHTML")  # returns the inner HTML as a string
    #     time.sleep(5)
    # except TimeoutException:
    #     print("Failed to navigate job pages")



    # username = driver.find_element_by_id("login-email")  # username form field
    # password = driver.find_element_by_id("login-password")  # password form field
    #
    # username.send_keys("hklee310@gmail.com")
    # password.send_keys("Winter1!")

    # submitButton = browser.find_element_by_id("submit_button_id")
    # button.click()




if __name__ == "__main__":
    driver = init_driver()
    # lookup(driver, "Selenium")
    login_linkedin(driver)

    # time.sleep(5)
    # driver.quit()