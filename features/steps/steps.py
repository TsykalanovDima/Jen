import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import *

@given('open page')
def step_impl(context):
    chrome_driver_path = "/Users/dimatsy/Downloads/chromedriver-mac-arm64/chromedriver"
    service = webdriver.chrome.service.Service(chrome_driver_path)
    context.driver = webdriver.Chrome(service=service)

@when('Open page')
def step_impl(context):
    context.driver.get("https://www.google.com")

@when('Click cookie consent')
def step_impl(context):
    cookie_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="L2AGLb"]/div'))
    )
    cookie_button.click()


@then('till infromation')
def step_impl(context):

    input_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="APjFqb"]'))
    )
    input_element.send_keys("привет")
    time.sleep(3)

@then('quit browser')
def step_impl(context):
    context.driver.quit()
