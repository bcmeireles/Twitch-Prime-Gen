from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def registerPage(driver):
    driver.get("https://www.twitch.tv/")
    driver.find_element(By.XPATH, "//button[@class='ScCoreButton-sc-1qn4ixc-0 ScCoreButtonPrimary-sc-1qn4ixc-1 ffyxRu dDxrgX']").click()
    input()

def fillRegiser(driver):
    driver.find_element(By.ID, "signup-username").send_keys("Testejkbsdasdasdasdfhjksfds")
    driver.find_element(By.ID, "password-input").send_keys("Pirocada12#")
    driver.find_element(By.ID, "password-input-confirmation").send_keys("Pirocada12#")
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)
    actions.send_keys("a")
    actions.send_keys(Keys.TAB)
    actions.send_keys("13")
    actions.send_keys(Keys.TAB)
    actions.send_keys("1999")
    actions.perform()

def fillEmail(driver, email):
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[4]/div/div[2]/button").click()
    driver.find_element(By.ID, "email-input").send_keys(email)
    input("cona\n")
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[5]/button").click()

def captcha(driver):
    if not "Verify Your Email Address" in driver.page_source:
        input("Captcha detected. Complete it and then press ENTER to continue...")

def verifyEmail(driver):
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/input").click()


