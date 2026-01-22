from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://yeezy.com/")

wait = WebDriverWait(driver, 5)

driver.find_element(By.CSS_SELECTOR, 'button[aria-label="View PK-01"]').click()

line = wait.until(EC.presence_of_element_located((By.TAG_NAME, "line")))
line.find_element(By.XPATH, "..").click()

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "garment-size-label")))
size = driver.find_elements(By.CLASS_NAME, "garment-size-label")[2]
size.find_element(By.XPATH, "../..").click()

driver.find_element(By.ID, "cart-button").click()

email_input = wait.until(EC.element_to_be_clickable((By.ID, "contact-email")))
email_input.click()
email_input.send_keys("me@email.com")
