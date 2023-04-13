import pytest
from pytest_bdd import scenario, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
# from test_data.orangehrmlive_login_data import username, password


# @scenario("./features/login.feature", "User logs in with valid credentials")
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@given("the login page is displayed")
def login_page(browser):
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when("the user enters valid username and password")
def enter_credentials(browser):
    browser.find_element(By.NAME, "username").send_keys("Admin")
    browser.find_element(By.NAME, "password").send_keys("admin123")


@when("clicks on the login button")
def click_login(browser):
    browser.find_element(By.XPATH, '//button[text()=" Login "]').click()


@then("the user should be logged in")
def verify_login(browser):
    assert "Dashboard" in browser.page_source
