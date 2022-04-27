from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

# URL decode
import yaml

# input
print('开始读取配置')
yml = yaml.load(open(r'config.yml', 'r', encoding='utf-8'), Loader=yaml.FullLoader)
myName = yml['name']
myHomeAttribute = str(yml['homeAttribute'])
myProvince = yml['province']
myCity = yml['city']
myArea = yml['area']
myPosition = yml['position']
myTemperature = str(yml['temperature'])
link = yml['link']
print('配置读取完毕')

# start
print('开始自动填充')
wd = webdriver.Chrome(service=Service(r'chromedriver.exe'))
wd.get(link)
wd.implicitly_wait(3)

# div1
wd.find_element(By.ID, 'q1').click()
wd.switch_to.frame('yz_popwinIframe')
wd.find_element(By.NAME, 'search-txt').send_keys(myName)
try:
    wd.find_element(By.XPATH, '//li[@data-value="' + myName + '"]').click()
except NoSuchElementException:
    print('未找到该名字\n按回车退出')
    input()
    wd.quit()
    exit(0)
wd.switch_to.default_content()

# div2
try:
    wd.find_element(By.XPATH, '//input[@id="q2_' + myHomeAttribute + '"]/../a').click()
except NoSuchElementException:
    print('居住地属性输入错误\n按回车退出')
    input()
    wd.quit()
    exit(0)

# div3
wd.find_element(By.ID, 'q3').click()
try:
    wd.switch_to.frame('yz_popwinIframe')
    wd.find_element(By.ID, 'select2-province-container').click()
    wd.find_element(By.XPATH, '//ul[@class="select2-results__options"]/li[text()="' + myProvince + '"]').click()
    wd.find_element(By.ID, 'select2-city-container').click()
    wd.find_element(By.XPATH, '//ul[@class="select2-results__options"]/li[contains(@id, "' + myCity + '")]').click()
    wd.find_element(By.ID, 'select2-area-container').click()
    wd.find_element(By.XPATH, '//ul[@class="select2-results__options"]/li[contains(@id, "' + myArea + '")]').click()
    wd.find_element(By.CLASS_NAME, 'button_a').click()
except NoSuchElementException:
    print('省份/城市/区域输入错误\n按回车退出')
    input()
    wd.quit()
    exit(0)
wd.switch_to.default_content()

# div4
try:
    wd.find_element(By.XPATH, '//label[@class="getLocalBtn"]').click()
    wd.switch_to.frame('yz_popwinIframe')
    wd.find_element(By.ID, 'txtInput').send_keys(myPosition)
    wd.find_element(By.ID, 'btnSearch').click()
    sleep(0.1)
    wd.find_element(By.XPATH, '//a[@class="ensure_btn"]').click()
    wd.switch_to.default_content()
except NoSuchElementException :
    print('位置打卡异常！\n按回车退出')
    input()
    wd.quit()
    exit(0)

# div5
wd.find_element(By.XPATH, '//input[@id="q5_1"]/../a').click()

# div6
wd.find_element(By.XPATH, '//input[@id="q6_1"]/../a').click()

# div7
wd.find_element(By.XPATH, '//input[@id="q7_1"]/../a').click()

# div8
wd.find_element(By.XPATH, '//input[@id="q8_1"]/../a').click()
wd.find_element(By.XPATH, '//input[@id="tqq8_1"]').send_keys(myTemperature)

# div9
wd.find_element(By.XPATH, '//input[@id="q9_1"]/../a').click()

# div10
wd.find_element(By.XPATH, '//input[@id="q10_1"]/../a').click()

# div11
wd.find_element(By.XPATH, '//input[@id="q11_1"]/../a').click()

# down
print('自动填充完毕\n输入\'y\'自动提交打卡问卷')
ch = input()
if ch == 'y':
    wd.find_element(By.ID, 'ctlNext').click()
    print('已自动提交打卡')
else:
    print('未自动提交打卡')
print('按回车关闭网页和程序')
input()
wd.quit()
exit(0)
