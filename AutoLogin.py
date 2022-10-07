#coding:UTF-8

headers = { 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36 Edge/17.17134',
}

from cmath import e
from selenium import webdriver
from time import sleep
from webbrowser import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tokenize import Name
import time

######## 參考路徑宣告 ########
path = r'c:/tools/chromedriver.exe'
url = 'https://shopee.tw/buyer/login'
########  E   N   D  ########

options = Options()
options.add_argument("--disable-notifications") # 取消網頁中的彈出視窗，避免妨礙網路爬蟲的執行。


chrome = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
chrome.get(url)

windowSize = chrome.get_window_size()

loginKey = chrome.find_element('name', 'loginKey')
password = chrome.find_element('name', 'password')

loginKey.send_keys('isMyid')
time.sleep(1)
password.send_keys('isMyPwd')
time.sleep(1)
password.submit()
time.sleep(1)

chrome.quit()
