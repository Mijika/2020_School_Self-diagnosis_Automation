from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

#DEIVER_PATH = '/usr/local/bin/chromedriver'

DEIVER_PATH = './크롬 드리이버/chromedriver.exe'
TARGET_URL = 'https://hcs.eduro.go.kr/'

NAME = '안담기'
password = '2404'


driver = webdriver.Chrome(DEIVER_PATH)
driver.implicitly_wait(1)
# 사이트 접속
driver.get(TARGET_URL)
driver.implicitly_wait(2)
web_driver_wait = WebDriverWait(driver, 30)

# 로그인 페이지로 이동
driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()
driver.implicitly_wait(1)

# 학교 찾기
driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select/option[2]').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select/option[5]').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[1]/input').send_keys("로봇")
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
driver.implicitly_wait(1)

# 사용자 입력
driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[2]/td/input').send_keys("안담기")
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[3]/td/input').send_keys("020608")
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
driver.implicitly_wait(3)

# 비밀번호 입력
time.sleep(1)
driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input').send_keys("2404")
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
driver.implicitly_wait(3)


# 사용자 데이터 입력 폼
time.sleep(1)
header = driver.find_element_by_xpath('//*[@id="container"]/div[2]/section[2]/div[2]/ul')
for i in range(1, ((len(header.text.split('\n')) + 1) // 5 ) + 1):
    try:
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="container"]/div[2]/section[2]/div[2]/ul/li['+ str(i) +']/a/span[1]').click()
        web_driver_wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="container"]/div[2]/section[2]/div[2]/ul/li['+ str(i) +']/a/span[1]')))

        driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label').click()
        web_driver_wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label')))
        driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label').click()
        web_driver_wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label')))
        driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label').click()
        web_driver_wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label')))
        driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[4]/dd/ul/li[1]/label').click()
        web_driver_wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[4]/dd/ul/li[1]/label')))
        driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[5]/dd/ul/li[1]/label').click()
        web_driver_wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[5]/dd/ul/li[1]/label')))
        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
        web_driver_wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="btnConfirm"]')))


        driver.find_element_by_xpath('//*[@id="container"]/div[1]/ul/li/a').click()
        web_driver_wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/ul/li/a')))

        time.sleep(1)

    except Exception as e:
        driver.find_element_by_xpath('//*[@id="container"]/div[1]/ul/li/a').click()
        web_driver_wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/ul/li/a')))

        continue
# # 사용자 데이터 입력 폼
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="container"]/div[2]/section[2]/div[2]/ul/li[1]/a/span[1]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label').click()
# driver.implicitly_wait(3)
# driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label').click()
# driver.implicitly_wait(3)
# driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label').click()
# driver.implicitly_wait(3)
# driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[4]/dd/ul/li[1]/label').click()
# driver.implicitly_wait(3)
# driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[5]/dd/ul/li[1]/label').click()
# driver.implicitly_wait(3)
# driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
# driver.implicitly_wait(3)

# driver.find_element_by_xpath('//*[@id="container"]/div[1]/ul/li/a').click()
# driver.implicitly_wait(3)
