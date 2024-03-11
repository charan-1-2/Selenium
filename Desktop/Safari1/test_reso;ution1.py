from selenium import webdriver
from selenium.webdriver.safari.options import Options as SafariOptions

def test_res1():
    options = SafariOptions()
    options.browser_version = 'latest'
    options.platform_name = 'macOS 13'
    sauce_options = {}
    sauce_options['username'] = 'oauth-charannaik764-26394'
    sauce_options['accessKey'] = '5cde0ccd-8792-46f3-b678-5d3db21beac8'
    sauce_options['build'] = '<your build id>'
    sauce_options['name'] = '<your test name>'
    options.set_capability('sauce:options', sauce_options)

    url = "https://oauth-charannaik764-26394:5cde0ccd-8792-46f3-b678-5d3db21beac8@ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    driver = webdriver.Remote(command_executor=url, options=options)
    driver.get("https://aksharatraining.com/")
    print(driver.title)
    driver.quit()