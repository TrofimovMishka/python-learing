from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINKEDIN = "https://www.linkedin.com"
EMAIL = 'my_email'
PASS = 'my_pass'
ENTER = "\ue007"

# to keep browser open:
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(LINKEDIN)

# Define a timeout for the explicit wait (e.g., 10 seconds)
wait = WebDriverWait(driver, 10)

sign_button = 'body > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis'
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, sign_button))).click()
# driver.find_element(By.CSS_SELECTOR, value=sign_button).click()

email_sign_input_selector = '#username'
pass_sign_input_selector = '#password'
sign_in_button = '#organic-div > form > div.login__form_action_container > button'

email_sign_input = driver.find_element(By.CSS_SELECTOR, value=email_sign_input_selector)
email_sign_input.send_keys(EMAIL)

pass_sign_input = driver.find_element(By.CSS_SELECTOR, value=pass_sign_input_selector)
pass_sign_input.send_keys(PASS)

# driver.find_element(By.CSS_SELECTOR, value='#global-nav > div > nav > ul > li:nth-child(3) > a > div > div > li-icon').click()

# driver.find_element(By.XPATH, value=sign_in_button).click()
driver.find_element(By.CSS_SELECTOR, value=sign_in_button).click()

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/header/div/nav/ul/li[3]/a/div'))).click()
# wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/header/div/nav/ul/li[3]/a'))).click()

job_input = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]')))
# job_input = driver.find_element(By.CSS_SELECTOR, value='#jobs-search-box-keyword-id-ember196')
job_input.send_keys("java", ENTER)

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[3]/div/span/button'))).click()
wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[3]/div/div/div/div[1]/div/form/fieldset/div[1]/ul/li[4]/input'))).send_keys(ENTER)
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[3]/div/div/div/div[1]/div/form/fieldset/div[2]/button[2]'))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/ul/li[7]/div/button'))).click() # easy apply

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[4]/div/div/div/button'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[1]/input'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]'))).click()


# driver.find_element(By.CSS_SELECTOR, value='#ember455').click()
# driver.find_element(By.CSS_SELECTOR, value='#searchFilter_timePostedRange').click()
# driver.find_element(By.CSS_SELECTOR, value='#timePostedRange-r86400').click()
# driver.find_element(By.CSS_SELECTOR, value='#ember959').click()

# To quit
# driver.quit()
