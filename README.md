# zzu_jkdk
郑州大专疫情打卡脚本


1. 环境准备
1) python环境
2) webdriver库
3) chrome浏览器
4) chromedriver并配置环境   



2. 脚本代码

from selenium import webdriver
import random
from time import sleep

driver = webdriver.Chrome()

driver.get("https://jksb.v.zzu.edu.cn")

now_handle = driver.current_window_handle
driver.switch_to.window(now_handle)
driver.find_element_by_xpath('//*[@id="mt_5"]/div[2]/div[3]/input').clear()
driver.find_element_by_xpath('//*[@id="mt_5"]/div[3]/div[3]/input').clear()
driver.find_element_by_xpath('//*[@id="mt_5"]/div[2]/div[3]/input').send_keys("2021223******")

driver.find_element_by_xpath('//*[@id="mt_5"]/div[3]/div[3]/input').send_keys("你自己的疫情打卡网站的password")	
driver.find_element_by_xpath('//*[@id="mt_5"]/div[5]/div/input').click()
real_mid_page_url = driver.find_element_by_xpath("//*[@id='zzj_top_6s']").get_attribute("src")
driver.get(real_mid_page_url)
driver.find_element_by_xpath('//*[@id="bak_0"]/div[11]/div[3]/div[4]/span').click()
driver.find_element_by_xpath('//*[@id="bak_0"]/div[7]/div[2]/div[2]/div[2]/div[6]/div[4]/span').click()




3. 任务定时启动
选择用win10自带的“任务计划程序”。
单击右侧创建基本任务
跟着提示往下走
在“程序或脚本”处选择自己的python环境所在位置
在“添加参数处”输入py文件的路径

成功

