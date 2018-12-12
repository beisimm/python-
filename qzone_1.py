import time #用来延时
from selenium import webdriver

driver = webdriver.Chrome() #选择浏览器，此处我选择的Chrome

driver.get('http://i.qq.com/')
driver.switch_to.frame('login_frame')
driver.find_element_by_id('switcher_plogin').click()

driver.find_element_by_name('u').clear()
driver.find_element_by_name('u').send_keys('345199390') # 此处输入你的QQ号
driver.find_element_by_name('p').clear()
driver.find_element_by_name('p').send_keys('s456123.') # 此处输入你的QQ密码



driver.execute_script("document.getElementById('login_button').parentNode.hidefocus=false;")
time.sleep(5) # 可能有人机滑块验证

driver.find_element_by_xpath('//*[@id="loginform"]/div[4]/a').click()
# driver.find_element_by_id('login_button').click()


# driver.find_element_by_id('dialog_button_1').click() # 这个地方是我把那个弹窗给点击了，配合上面的延时用的，延时是等待那个弹窗出现，然后此处点击取消

btns = driver.find_elements_by_css_selector('a.item.qz_like_btn_v3') # 此处是CSS选择器
for btn in btns:
 btn.click()
