from selenium import webdriver
from selenium.webdriver.common.by import By
import time

ERRORS = ["Internal Error. Please try again later.",
            "The phone number you've entered is not valid. Please enter a valid phone number."]

def check_error(driver):
    for error in ERRORS:
        if error in driver.page_source:
            return True

def create_driver():
    driver = webdriver.Firefox(executable_path="geckodriver")
    return driver

def destroy_driver(driver):
    driver.quit()

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
    driver.find_element(By.XPATH, "//input[@id='cvf-input-code']").send_keys(otp)
    driver.find_element(By.ID, "cvf-submit-otp-button").click()

def fill_po(driver, country, number):
    driver.find_element(By.CLASS_NAME, "a-dropdown-prompt").click()
    time.sleep(0.5)
    driver.find_element(By.ID, country).click()
    driver.find_element(By.CLASS_NAME, "a-button-input notranslate").send_keys(number)