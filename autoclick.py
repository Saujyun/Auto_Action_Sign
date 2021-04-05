import os
# 方便延时加载
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

# 模拟浏览器打开网站
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
#windows电脑
# browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
#mac电脑调试将下面路径换成你的chromedriver本地路径即可，
browser = webdriver.Chrome("/usr/local/bin/chromedriver")

def saveFile(message):
    # 保存email内容
    with open("email.txt", 'a+', encoding="utf-8") as email:
        email.write(message+'\n')


def situyun():
    browser.get('http://situcloud.xyz/auth/login')
    # 将窗口最大化
    browser.maximize_window()
    # 格式是PEP8自动转的
    # 这里是找到输入框,发送要输入的用户名和密码,模拟登陆
    browser.find_element_by_xpath(
        "/html/body/div[1]/section/div/div/div/div[2]/form/div/div[1]/input").send_keys("2679225466@qq.com")
    browser.find_element_by_xpath(
        "/html/body/div[1]/section/div/div/div/div[2]/form/div/div[2]/input").send_keys("12345678")
    # 在输入用户名和密码之后,点击登陆按钮
    browser.find_element_by_xpath("/html/body/div[1]/section/div/div/div/div[2]/form/div/div[5]/button").click()
    time.sleep(10)
    try:
        if(browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/button")!= None):
            browser.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/button").click()
            time.sleep(5)
        if("明日再来" in browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div[1]/div/div/a").text):
            saveFile("明日再来!")
        else:
            browser.find_element_by_xpath("/html/body/div[1]/div/div[3]/section/div[1]/div/div/a").click()
            print("司徒云打卡成功2")
        time.sleep(3)
    except NoSuchElementException as e:
        print ("NoSuchElementException!")
        saveFile("司徒云签到代码存在异常"+str(e))

if __name__ == '__main__':
    situyun()
    # 脚本运行成功,退出浏览器
    browser.quit()
