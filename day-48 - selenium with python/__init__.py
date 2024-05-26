from selenium.webdriver.common.by import By
from selenium import webdriver

# to keep browser open:
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://python.org/")
# driver.get("https://google.com/")

# driver.find_element(by=By.ID, value="W0wltc").click()
# driver.find_element(by=By.CLASS_NAME, value="gb_f").click()

menu = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
elements_of_menu = menu.find_elements(by=By.TAG_NAME, value="li")

items = [{'time': i.text.split("\n")[0], 'name': i.text.split("\n")[1]} for i in elements_of_menu]
# items = [{'time': i.text.split("\n")[0], 'name': i.text.split("\n")[1]} for i in elements_of_menu]

print(items)

# To quit
driver.quit()