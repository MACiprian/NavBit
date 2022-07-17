from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


DELAY = 5
URL = "https://www.youtube.com"
XPATHS = {
    'ACCEPT_COOKIES' : '//*[@id="content"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]',
    'SEARCH_BAR' : ''
}

def wait_for_elem(driver, xpath):
    return WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.XPATH, xpath)))

def start_browser():
    options = Options()
    options.add_experimental_option("detach", True)  # keep browser alive
    options.add_argument("start-maximized")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def main():
    driver = start_browser()
    driver.get(URL)
    # accept cookies
    try:
        wait_for_elem(driver, XPATHS["ACCEPT_COOKIES"]).click()
    except TimeoutException:
        print('Failed to accept cookies')
        driver.quit()
        exit()

if __name__ == '__main__':
    main()

