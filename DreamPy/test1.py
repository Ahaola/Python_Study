from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")  #获取百度网址
driver.maximize_window()  #最大化
driver.get_screenshot_as_file("baidu.png") #截图，图片格式要求为.png
title = driver.title #获取网页标题
print(title)

#基于属性的定位
driver.find_element(By.ID,"kw")
driver.find_element(By.NAME,"wd")
driver.find_element(By.CLASS_NAME,"s_ipt")
driver.find_element(By.TAG_NAME,"input")

#表达式定位
# driver.find_element(By.XPATH,'//*[@id="kw"]')#使用Xpath定位元素注意使用单引号
baidu = driver.find_element(By.CSS_SELECTOR,"#kw")
baidu.send_keys("24秋招拿下！！")
baidu.click(By.CSS_SELECTOR,'#su')
driver.quit() #关闭浏览器
