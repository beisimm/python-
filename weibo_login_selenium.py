from selenium import webdriver
import time

browse = webdriver.Chrome('./chromedriver.exe')
browse.get('https://weibo.com/login.php')
# 等待
browse.implicitly_wait(3)

loginname_element = browse.find_element_by_id('loginname')
password_element = browse.find_element_by_xpath('//div/div/input[@type="password"]')

loginname_element.send_keys('')
# time.sleep(0.5)
password_element.send_keys('')
# time.sleep(0.5)

browse.find_element_by_xpath('//div/a[@node-type="submitBtn"]').click()


# browse.close()