from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

cookies_when_log = ['']
options = Options()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"

options.add_argument("user-agent={}".format(user_agent))
# options.add_argument("--headless")


driver = webdriver.Firefox(options=options)
driver.get("https://www.goplayone.com/")
sleep(30)


# button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/header/div/div/div[2]/button')
# button.click()
# sleep(2)

# ac = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[4]/div[1]/div/input')
# ac.send_keys("123")

# pw = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/div[4]/div[2]/div/input')
# pw.send_keys("123")
# pw.send_keys(Keys.ENTER)


cookies = driver.get_cookies()
print(cookies)