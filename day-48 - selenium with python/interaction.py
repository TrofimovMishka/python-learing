from selenium.webdriver.common.by import By
from selenium import webdriver

ENTER = "\ue007"

# to keep browser open:
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
# driver.get("https://python.org/")
driver.get("https://google.com/")

driver.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[1]").click()
search = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
search.send_keys("Java doc", ENTER)

# ENTER - "\ue007"
# To quit
# driver.quit()