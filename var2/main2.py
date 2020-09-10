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

# 추가 요구 사항으로는 txt파일 말고 json으로 하고 로그인 절차를 로컬 스토리지에 있는
# 데이터를 사용하여 더 빨리 하자 일단 이것만 하자 ㅇㅋㅇㅋ 수고했엉

# logger.info("text")


DEVELOPMENT = 0  # 개발 중일때 사용
RUN = 10 # 개발 끝나고 사용

PROGRAM_STATUS = RUN
# PROGRAM_STATUS = DEVELOPMENT


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
		i = 0
		for user_data in self.users_data:
			try:
				if i != 0:
					self.clear()
					self.clear()

				self.web_page_access(user_data)
				self.user_login_process(user_data)
				self.data_form_process(user_data)
				self.clear()
				self.clear()
				i += 1

				logger.info(user_data[0] + " 완료")

			except Exception as e:
				logger.error("main_process 오류 발생 :" + user_data[0])
				self.result_msg += str(user_data[0]) + " 오류 발생"
				self.clear()
				continue

		self.result_msg = str(self.users_data_len) + "명의 자가 진단 완료"
		logger.info('main process end')

	def web_page_access(self, user_data):
		try:
			logger.info("사이트 접속")
			self.driver.get(TARGET_URL)
			self.driver.implicitly_wait(2)

		except Exception as e:
			logger.error("web page access 오류 발생" + str(user_data[0]))
			raise e

	def user_login_process(self, user_data):
		logger.info(str(user_data[0])+": 로그인 프로세서 실행")
		try:
			# 로그인 페이지로 이동
			self.element_click('//*[@id="btnConfirm2"]')

			# 학교 찾기
			self.element_click('//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button')
			self.element_click('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select/option[2]')
			self.element_click('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select/option[5]')

			self.element_sned_key('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[1]/input', '로봇')
			self.element_click('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button')
			self.element_click('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li')

			self.element_click('//*[@id="softBoardListLayer"]/div[2]/div[2]/input')

			# 사용자 입력
			self.element_sned_key('//*[@id="WriteInfoForm"]/table/tbody/tr[2]/td/input', user_data[0])
			self.element_sned_key('//*[@id="WriteInfoForm"]/table/tbody/tr[3]/td/input', user_data[1])

			self.element_click('//*[@id="btnConfirm"]')

			# 비밀번호 입력
			self.element_sned_key('//*[@id="WriteInfoForm"]/table/tbody/tr/td/input', user_data[2])

			self.element_click('//*[@id="btnConfirm"]')

		except Exception as e:
			logger.error("사용자 로그인 오류 발생" + str(user_data[0]))
			raise e


	def data_form_process(self, user_data):
		try:
			# 사용자 선택
			logger.info("데이타 입력")
			time.sleep(1)
			self.element_click('//*[@id="container"]/div[2]/section[2]/div[2]/ul/li/a/span[1]')

			self.element_click('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[1]/dd/ul/li[1]/label')
			self.element_click('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[2]/dd/ul/li[1]/label')
			self.element_click('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[3]/dd/ul/li[1]/label')
			self.element_click('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[4]/dd/ul/li[1]/label')
			self.element_click('//*[@id="container"]/div[2]/div/div[2]/div[2]/dl[5]/dd/ul/li[1]/label')

			self.element_click('//*[@id="btnConfirm"]')
			self.driver.get('https://hcs.eduro.go.kr/#/main')
			#self.element_click('//*[@id="container"]/div[1]/ul/li/a')

		except Exception as e:
			logger.error("데이타 입력 폼 오류 발생" + str(user_data[0]))
			raise e

	def element_click(self, xpath):
		self.web_driver_wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
		self.driver.find_element_by_xpath(xpath).click()
		# self.web_driver_wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))

	def element_sned_key(self, xpath, data):
		time.sleep(1)
		self.web_driver_wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
		self.driver.find_element_by_xpath(xpath).send_keys(data)

	def clear(self):
		logger.info("로컬 스로리지 초기화")
		self.driver.execute_script("window.localStorage.clear();")

	def get_result(self):
		return self.result_msg

if __name__ == '__main__':
	data_controller = Users_data_loader()
	users_data = data_controller.get_users_data()
	logger.info(users_data)

	robot = Robot(users_data)
	robot.start()
	robot.close()

	logger.info(robot.get_result())
	meg = robot.get_result()
	sender = send_mail.MainSender()
	sender.send_mail('sbahn42@gmail.com', 'sbahn42@gmail.com', meg)