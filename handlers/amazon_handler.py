from selenium import webdriver
from selenium.webdriver.common.by import By

def create_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, executable_path=r"./chromedriver.exe")
    return driver

def register_page(driver):
    driver.get("https://www.amazon.com/")
    driver.find_element(By.ID, "nav-link-accountList").click()
    driver.find_element(By.ID, "createAccountSubmit").click()

def fill_register(driver, data):
    driver.find_element(By.ID, "ap_customer_name").send_keys(data["name"])
    driver.find_element(By.ID, "ap_email").send_keys(data["email"])
    driver.find_element(By.ID, "ap_password").send_keys(data["password"])
    driver.find_element(By.ID, "ap_password_check").send_keys(data["password"])
    driver.find_element(By.ID, "continue").click()

def captcha(driver):
    if "Solve this puzzle to protect your account" in driver.page_source:
        input("Captcha detected. Complete it and then press ENTER to continue...")

def fill_otp(driver, otp):
    driver.find_element(By.ID, "cvf-input-code").send_keys(otp)
    #driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div/div/div[1]/form/div[5]/div[2]/div/input").send_keys(otp)
    driver.find_element(By.NAME, "a-button-input").click()
    input()

def fill_po(driver, country, number):
    driver.find_element(By.ID, country).click()
    driver.find_element(By.NAME, "cvf_phone_num").send_keys(number)
    input()
