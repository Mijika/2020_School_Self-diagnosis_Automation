from selenium import webdriver
import os


DEIVER_PATH = './크롬 드리이버/chromedriver.exe'
TARGET_URL = 'https://eduro.sen.go.kr/hcheck/index.jsp'
NAME = '홍길동'
KEY = 'GDGEGV'

def main():
	# 브라우저 초기화
	driver = webdriver.Chrome(DEIVER_PATH)
	driver.implicitly_wait(1)
	driver.get(TARGET_URL)
	driver.implicitly_wait(1)

	# 사용자 입력 페이지로 이동
	driver.find_element_by_xpath('//*[@id="container"]/div/div/div/div[2]/div/a[1]/div').click()
	driver.implicitly_wait(1)

	# form 입력
	driver.find_element_by_xpath('//*[@id="pName"]').send_keys(NAME)
	driver.find_element_by_xpath('//*[@id="qstnCrtfcNo"]').send_keys(KEY)

	driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()


	# data 입력
	driver.find_element_by_xpath('//*[@id="rspns011"]').click()
	driver.find_element_by_xpath('//*[@id="rspns02"]').click()
	driver.find_element_by_xpath('//*[@id="rspns070"]').click()
	driver.find_element_by_xpath('//*[@id="rspns080"]').click()
	driver.find_element_by_xpath('//*[@id="rspns090"]').click()

	driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
	driver.implicitly_wait(2)

	# 브라우저 종류
	driver.quit()

if __name__ == '__main__':
	main()
