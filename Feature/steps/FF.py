import time

from behave import use_step_matcher
from behave import *

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Steps import *
from Steps.step_impl_web_element_handling import get_chrome_driver_and_navigate_to_url_with_title, driver, \
    webdriver_shutdown
from TestData.excelDemo import readExcelDataAsperTestCase
from ReadProperties import ReadPropertiesFile

use_step_matcher("re")
@given('Open Browser and launch application "(?P<TestcaseName>.+)"')
def step_impl(context,TestcaseName):
    Applicationurl = str(readExcelDataAsperTestCase(TestcaseName,"URL"))
    print(Applicationurl)
    get_chrome_driver_and_navigate_to_url_with_title(Applicationurl)

@when("Test2")
def step_impl(context):
    print(driver.title)
    search_bar = driver.find_element_by_name("q")
    search_bar.clear()
    search_bar.send_keys("learn python")
    search_bar.send_keys(Keys.RETURN)
    print(driver.current_url)
    print("Executed When")

@then("Test3")
def step_impl(context):
    Actual = driver.find_element_by_xpath("//*[contains(text(),'Python Online Training - Learn Python in just 4 weeks')]").get_attribute("value")
    Expected = "Selenium Python Automation Testing from Scratch + Frameworks"
    # if condition returns False, AssertionError is raised:
    assert "goodbye", "x should be 'hello'"
    if Actual==Expected:
        print("Pass")
    else:
        print("Fail")
    print("Executed Then")

@when("Provide credential UserID and Password")
def step_impl(context):
    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//*[text()='Login'])[2]")))
    UserID = ReadPropertiesFile.ReadDataFromPropertiesFile("UserID")
    Password = ReadPropertiesFile.ReadDataFromPropertiesFile("Password")
    # driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",UserID, "background:yellow; color:Red; border:4px dotted solid yellow")
    driver.find_element_by_xpath("(//*[@type='text'])[2]").send_keys(UserID)
    driver.find_element_by_xpath("//*[@type='password']").send_keys(Password)
    driver.find_element_by_xpath("(//*[text()='Login'])[3]").click()


@then("Validate whether Login is successful or not")
def step_impl(context):
    time.sleep(10)

@then("Logout")
def step_impl(context):

    element = driver.find_element_by_xpath("//*[text()='Prosenjit']")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    driver.find_element_by_xpath("//*[text()='Logout']").click()
    webdriver_shutdown(driver)

