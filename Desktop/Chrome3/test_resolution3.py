import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_res3():
    chrom_option = Options()
    chrom_option.add_argument("--disable-notifications")
    driver = Chrome(options=chrom_option)
    driver.implicitly_wait(10)
    def go_back(driver):
        time.sleep(1)
        driver.back()
        time.sleep(1)
    driver.get("https://www.getcalley.com/page-sitemap.xml")
    driver.set_window_size(1536,864)

    driver.find_element(By.XPATH,"//a[text()='https://www.getcalley.com/']").click()
    driver.get_screenshot_as_file("./homepage1.png")
    go_back(driver)

    driver.find_element(By.XPATH, "//a[text()='https://www.getcalley.com/calley-call-from-browser/']").click()
    driver.get_screenshot_as_file("./homepage2.png")
    go_back(driver)

    driver.find_element(By.XPATH, "//a[text()='https://www.getcalley.com/calley-pro-features/']").click()
    driver.get_screenshot_as_file("./homepage3.png")
    go_back(driver)

    driver.find_element(By.XPATH, "//a[text()='https://www.getcalley.com/best-auto-dialer-app/']").click()
    driver.get_screenshot_as_file("./homepage4.png")
    go_back(driver)

    driver.find_element(By.XPATH, "//a[text()='https://www.getcalley.com/how-calley-auto-dialer-app-works/']").click()
    driver.get_screenshot_as_file("./homepage5.png")
    time.sleep(2)

    driver.quit()

