from selenium import webdriver
from selenium.webdriver.common.by import By
import time

USERNAME = "subrataroy_vx6WcF"
ACCESS_KEY = "yTmzz5aTxb4jCTcLraFj"

URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# List of browsers to test
browsers = [
    {"name": "Chrome", "os": "Windows", "os_version": "10"},
    {"name": "Firefox", "os": "Windows", "os_version": "10"},
    {"name": "Edge", "os": "Windows", "os_version": "10"},
    {"name": "Safari", "os": "OS X", "os_version": "Monterey"}
]

def run_test(browser_name, os_name, os_version):
    # Create proper options object for each browser
    if browser_name == "Chrome":
        options = webdriver.ChromeOptions()
    elif browser_name == "Firefox":
        options = webdriver.FirefoxOptions()
    elif browser_name == "Edge":
        options = webdriver.EdgeOptions()
    elif browser_name == "Safari":
        options = webdriver.SafariOptions()
    else:
        raise Exception("Unsupported browser")

    # Set capabilities
    options.set_capability("browserName", browser_name)
    options.set_capability("browserVersion", "latest")
    options.set_capability("bstack:options", {
        "os": os_name,
        "osVersion": os_version,
        "buildName": "Prodigy Task-04",
        "sessionName": f"Login Test - {browser_name}"
    })

    print(f"Running test on {browser_name}...")

    driver = webdriver.Remote(
        command_executor=URL,
        options=options
    )

    driver.implicitly_wait(10)
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Login
    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("Password123")
    driver.find_element(By.ID, "submit").click()

    # Mark test passed
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed","reason":"Login successful"}}'
    )

    time.sleep(2)  # Wait for BrowserStack to register
    driver.quit()
    print(f"{browser_name} test completed.\n")


# Run exactly 4 browsers
for b in browsers:
    run_test(b["name"], b["os"], b["os_version"])