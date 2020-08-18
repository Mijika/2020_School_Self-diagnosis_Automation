from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os


# DEIVER_PATH = '/usr/local/bin/chromedriver'
DEIVER_PATH = './크롬 드리이버/chromedriver.exe'
TARGET_URL = 'https://eduro.sen.go.kr/stv_cvd_co00_010.do'
USERS_DATA_PATH = './users_data.txt'
# USERS_DATA_PATH = './test_data.txt'


class Users_data_loader():
	def __init__(self):
		self.user_data_list =list()
		self.error_check = False

		try:
			self.data_load()
		except Exception as e:
			print(e)


	def data_load(self):
		with open(USERS_DATA_PATH, 'r', encoding='UTF8') as f:
			while True:
				data = f.readline()

				if not data:
					break

				name = data.split()[0]
				key = data.split()[1]

				if len(key) != 6:
					continue

				self.user_data_list.append([name, key])

	def get_users_data(self):
		return self.user_data_list

class Robot():
	def __init__(self, users_data):
		print("자가진단 자동화 생성")
		self.users_data = users_data
		self.users_data_len = len(self.users_data)

		print(self.users_data_len, '명의 자가진단을 자동화 예정')

	def start(self):
		# 브라우저 초기화
		options = webdriver.ChromeOptions()
		options.add_argument('--headless')
		self.driver = webdriver.Chrome(DEIVER_PATH, options=options)
		self.web_driver_wait = WebDriverWait(self.driver, 30)

		self.main_process()

	def close(self):
		# 브라우저 종료
		self.driver.quit()
		print('system close')

	def main_process(self):
		print('main process start')

		for user_name, user_key in self.users_data:
			try:
				self.web_page_access()
				self.user_form_process(user_name, user_key)
				self.data_form_process(user_name)

			except Exception as e:
				print(user_name, "오류 발생")
				continue

			print(user_name, '완료')

		print('main process end')

	def web_page_access(self):
		try:
			self.driver.implicitly_wait(10)
			self.driver.get(TARGET_URL)
			# time.sleep(1)

		except Exception as e:
			print("web page access error")
			raise e

	def user_form_process(self, user_name, user_key):
		try:
			# form 입력
			self.driver.find_element_by_xpath('//*[@id="pName"]').send_keys(user_name)
			self.driver.find_element_by_xpath('//*[@id="qstnCrtfcNo"]').send_keys(user_key)

			self.driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

		except Exception as e:
			print("user form process error")
			raise e


	def data_form_process(self, user_name):
		try:
			# data 입력
			time.sleep(0.3)

			self.driver.find_element_by_xpath('//*[@id="rspns011"]').click()
			self.web_driver_wait.until(EC.element_to_be_clickable((By.ID, 'rspns011')))
			self.driver.find_element_by_xpath('//*[@id="rspns02"]').click()
			self.web_driver_wait.until(EC.element_to_be_clickable((By.ID, 'rspns02')))
			self.driver.find_element_by_xpath('//*[@id="rspns070"]').click()
			self.web_driver_wait.until(EC.element_to_be_clickable((By.ID, 'rspns070')))
			self.driver.find_element_by_xpath('//*[@id="rspns080"]').click()
			self.web_driver_wait.until(EC.element_to_be_clickable((By.ID, 'rspns080')))
			self.driver.find_element_by_xpath('//*[@id="rspns090"]').click()
			self.web_driver_wait.until(EC.element_to_be_clickable((By.ID, 'rspns090')))

			self.driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

		except :
			print("data form process error")

			# 잘못된 인증 정보일시 Alert 예외처리
			try:
				result = self.driver.switch_to.alert()
				print(result.text)

			except Exception as e:
				raise e
			else:
				return



if __name__ == '__main__':
	data_controller = Users_data_loader()
	data_list = data_controller.get_users_data()
	# print(data_list)

	robot = Robot(data_list)
	robot.start()
	robot.close()
