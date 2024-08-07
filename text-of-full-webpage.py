from selenium import webdriver

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def main():
    driver = get_driver()
    # Find all div elements on the page
    div_elements = driver.find_elements(by="tag name", value="div")
    # Extract and concatenate the text from each div
    page_text_by_division = "\n".join([div.text for div in div_elements])
    driver.quit()
    return page_text_by_division

print(main())
