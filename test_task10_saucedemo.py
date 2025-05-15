# Task 10: SauceDemo Login Page Test Case 
# This test case will check the title, URL, and login functionality of the SauceDemo website.
# Storing the URL, username, password, and expected values for the test case as variables

# Importing necessary libraries
# Importing the necessary libraries for web automation and testing

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

login_url = "https://www.saucedemo.com/"
username = "standard_user"
password = "secret_sauce"
expected_title = "Swag Labs"
expected_home_url = login_url
expected_dashboard_url = "https://www.saucedemo.com/inventory.html"

@pytest.fixture(scope="module")
def driver():
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Run in headless mode for CI/CD
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()  
    yield driver
    # Cleanup code after tests are done
    driver.quit()

# Test case details
# 1. Open the SauceDemo login webpage.
# 2. Verify the title of the webpage.

def test_title(driver):
    driver.get(login_url)
    assert driver.title == expected_title, f"Expected title: {expected_title}, but got: {driver.title}"

# 3. Verify the URL of the page.
def test_homepage_url(driver):
    driver.get(login_url)
    assert driver.current_url == expected_home_url, f"Expected URL: {expected_home_url}, but got: {driver.current_url}" 

# 4. Verify the Login and Dashboard URL of the webpage.
def test_login_and_dashboard_url(driver):
    driver.get(login_url)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(3) 
    assert driver.current_url == expected_dashboard_url, f"Expected URL: {expected_dashboard_url}, but got: {driver.current_url}"
    
# The test case will also save the page source to a text file - Webpage_task_11.txt for further analysis.  
    with open ("Webpage_task_11.txt", "w", encoding='utf-8') as file:
        file.write(driver.page_source)

def test_title_fail(driver):
    driver.get(login_url)
    # Intentionally using an incorrect title to trigger a failure
    expected_title = "Incorrect Title"  
    assert driver.title == expected_title, f"Expected title: {expected_title}, but got: {driver.title}"


def test_homepage_url_fail(driver):
    driver.get(login_url)
    # Intentionally using an incorrect URL to trigger a failure
    expected_home_url = "https://www.example.com/"  
    assert driver.current_url == expected_home_url, f"Expected URL: {expected_home_url}, but got: {driver.current_url}" 

def test_login_and_dashboard_url_fail(driver):
    # Intentionally using the wrong field for username and password to trigger a failure
    driver.get(login_url)
    driver.find_element(By.ID, "password").send_keys(username) 
    driver.find_element(By.ID, "user-name").send_keys(password) 
    # Intentionally using the wrong credentials to trigger a failure
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    assert driver.current_url == expected_dashboard_url, f"Expected URL: {expected_dashboard_url}, but got: {driver.current_url}"
