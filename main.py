import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import random
from time import sleep


# 选择Chrome浏览器
driver = webdriver.Chrome()
# 这是我学校的打卡网页，需自行修改
driver.get("https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0")

# 这两步把操作界面切换到新打开的浏览器页面
now_handle = driver.current_window_handle
driver.switch_to.window(now_handle)
#清空账号密码
driver.find_element_by_xpath('//*[@id="mt_5"]/div[2]/div[3]/input').clear()
driver.find_element_by_xpath('//*[@id="mt_5"]/div[3]/div[3]/input').clear()
#填写账号密码
driver.find_element_by_xpath('//*[@id="mt_5"]/div[2]/div[3]/input').send_keys("2021***")	# 账号
driver.find_element_by_xpath('//*[@id="mt_5"]/div[3]/div[3]/input').send_keys("*****")	# 密码
#
driver.find_element_by_xpath('//*[@id="mt_5"]/div[5]/div/input').click()

# 缓10秒
time.sleep(10)
real_mid_page_url = driver.find_element_by_xpath("//*[@id='zzj_top_6s']").get_attribute("src")
driver.get(real_mid_page_url)

driver.find_element_by_xpath('//*[@id="bak_0"]/div[11]/div[3]/div[4]/span').click()

# 缓30秒，等网页获取完地址
time.sleep(30)
#点击确认
# //*[@id="btn416a"]/span
# //*[@id="btn416b"]/span
driver.find_element_by_xpath('//*[@id="btn416b"]/span').click()
driver.find_element_by_xpath('//*[@id="bak_0"]/div[7]/div[4]/span').click()
time.sleep(2)

