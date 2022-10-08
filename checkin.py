from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 用户名和密码（登陆信息门户用的），自行输入
name = 'xxxxxxxx'
pwd = 'xxxxxxxx'

# 自行选一个驱动 比如Safari、ChromeDriver、Firefox
browser = webdriver.Safari()
wait = WebDriverWait(browser, 10) #等待的最大时间
browser.get("https://app.bupt.edu.cn/ncov/wap/default/index")
browser.switch_to.frame('loginIframe')
time.sleep(1)

# 将扫码登陆切换到密码登陆 2022.10.8修复
side_bar = browser.find_element_by_id('content-title')
login_type = side_bar.find_elements_by_css_selector('a')
login_type[1].click()
time.sleep(1)

user_input = browser.find_element_by_id('username')
password_input = browser.find_element_by_id('password')
usrname = user_input.send_keys(name)
password = password_input.send_keys(pwd)
btn = browser.find_element_by_class_name('submit-btn').click()
time.sleep(1)
browser.switch_to.default_content()
sfzx = wait.until(
    EC.visibility_of_element_located((By.NAME, 'sfzx'))
)
div = sfzx.find_elements_by_css_selector('div')

# 是否在校，在校选yes，不在校选no

# yes = div[1].find_element_by_tag_name('span').click()
no = div[2].find_element_by_tag_name('span').click()

# 是否中高风险地区
zgfxdq = browser.find_element_by_name('zgfxdq')
div = zgfxdq.find_elements_by_css_selector('div')
no = div[2].find_element_by_tag_name('span').click()

# 获取地理位置
area = browser.find_element_by_name('area').find_element_by_tag_name('input').click()

# submit = wait.until(
#     #EC.element_to_be_clickable((By.CLASS_NAME, 'wapcf-btn-qx'))
#     EC.text_to_be_present_in_element((By.XPATH, "//div[@name='area']/input"), "北京市 海淀区")
# )

# 提交
submit = browser.find_element_by_class_name('footers').find_element_by_tag_name('a')
time.sleep(3)
submit.click()
confirm = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'wapcf-btn-ok'))

)
#confirm = browser.find_element_by_class_name('wapat-btn-ok')
confirm.click()
print("打卡完成")   
browser.quit() 
