from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

try:
    print("Opening Google...")
    driver.get("https://www.google.com")

    print("Finding search field...")
    search = driver.find_element(By.NAME, "q")

    print("Entering search text...")
    search.send_keys("Google")

    print("Submitting search...")
    search.submit()

    assert "Google" in driver.title

    print("Result: Test successfully passed!!")

finally:
    input("Press Enter to close the browser...")
    driver.quit()
