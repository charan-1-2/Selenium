import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def test1():
    driver=Chrome()
    driver.implicitly_wait(10)
    wait=WebDriverWait(driver,10)
    driver.maximize_window()
    driver.get("https://demo.dealsdray.com/")
    driver.find_element(By.NAME,"username").send_keys("prexo.mis@dealsdray.com")
    driver.find_element(By.NAME,"password").send_keys("prexo.mis@dealsdray.com")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    driver.find_element(By.XPATH,"//span[text()='chevron_right']").click()
    driver.find_element(By.XPATH,"//span[text()='Orders']").click()
    driver.find_element(By.XPATH,"//button[text()='Add Bulk Orders']").click()
    relative_path="./../data/demo-data.xlsx"
    Absollute_path=os.path.abspath(relative_path)
    driver.find_element(By.XPATH,"//input[@type='file']").send_keys(Absollute_path)
    driver.find_element(By.XPATH,"//button[text()='Import']").click()
    driver.find_element(By.XPATH,"//button[text()='Validate Data']").click()
    wait.until(EC.alert_is_present())
    alert=driver.switch_to.alert
    alert.accept()
    driver.get_screenshot_as_file("./validation.png")
    time.sleep(4)
    driver.close()

