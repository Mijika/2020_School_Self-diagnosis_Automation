import time
import logging
import os
import platform

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import send_mail
from users_data_lodaer import *


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_hander = logging.StreamHandler()
stream_hander.setFormatter(formatter)

logger.addHandler(stream_hander)


# logger.info("text")


DEVELOPMENT = 0  # 개발 중일때 사용
RUN = 10 # 개발 끝나고 사용

# Program STATUS = RUN
PROGRAM_STATUS = DEVELOPMENT


if platform.system() == "Windows":
	DEIVER_PATH = './크롬 드리이버/chromedriver.exe'
elif platform.system() == "Linux":
	DEIVER_PATH = '/usr/local/bin/chromedriver'

TARGET_URL = 'https://hcs.eduro.go.kr/'



class Robot:
	def __init__(self, users_data):
		logger.info("자가 진단 robot 생성")

		self.result_msg = str() # 자가진단 결과를 저장하는 객체
		self.users_data = users_data
		self.users_data_len = len(self.users_data)

		self.driver = None
		self.web_driver_wait = None

		logger.info(str(self.users_data_len) + '명의 자가진단을 자동화 예정')

	def start(self):
		logger.info("브라우저 초기화")

		# 개발 과정에는 브라우저를 실행한다.
		if PROGRAM_STATUS == RUN:
			options = webdriver.ChromeOptions()
			options.add_argument('--headless')
			self.driver = webdriver.Chrome(DEIVER_PATH, options=options)

		elif PROGRAM_STATUS == DEVELOPMENT:
			self.driver = webdriver.Chrome(DEIVER_PATH)

		self.driver.implicitly_wait(10)
		self.web_driver_wait = WebDriverWait(self.driver, 30)

		self.main_process()

	def close(self):
		logger.info("브라우저 종료")

		# driver 객체가 있는지 확인하고 지움
		if isinstance(self.driver, webdriver.Chrome):
			self.driver.quit()

		print('system close')


	def main_process(self):
		logger.info("메인 프로세서 실행")

		for user_data in self.users_data:
			try:
				self.web_page_access(user_data)
				self.user_form_process(user_data)
				self.data_form_process(user_data)

			except Exception as e:
				logger.error("main_process 오류 발생 :"
					+ user_data[0])
				self.result_msg += str(user_data[0]) + " 오류 발생"
				continue

	def web_page_access(user_data):
		try:
			self.driver.get(TARGET_URL)
			self.driver.implicitly_wait(2)

		except Exception as e:
			logger.error("web page access 오류 발생" + str(user_data[0]))

	def user_form_process(user_data):
		pass

	def data_form_process(user_data):
		pass



if __name__ == '__main__':
	data_controller = Users_data_loader()
	users_data = data_controller.get_users_data()
	print(users_data)

	robot = Robot(users_data)
	robot.start()
	robot.close()