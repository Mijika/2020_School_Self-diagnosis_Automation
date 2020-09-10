import smtplib
from email.mime.text import MIMEText
import platform
import time


class MainSender:
	우분투_키 = "xuahpdngddqfxqyy"
	윈도우_키 = "aactbhwxpchkatsc"
	def __init__(self):
		self.current_key = None

		if platform.system() == "Linux":
			self.current_key = self.우분투_키
		elif platform.system() == "Windows":
			self.current_key = self.윈도우_키

	def send_mail(self, me, you, msg):
		try:
			smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			smtp.login(me, self.current_key)

			now = time.localtime()
			msg = MIMEText(msg)
			msg['Subject'] = "%04d/%02d/%02d %02d:%02d:%02d 학교 자가 진단 완료" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

			smtp.sendmail(me, you, msg.as_string())
		except Exception as e:
			print(e)
			smtp.quit()

	# def send_mail(self, me, you, msg):
	# 	smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)

	# 	smtp.login(me, self.윈도우_키)
	# 	msg = MIMEText(msg)
	# 	msg['Subject'] = 'TEST'
	# 	smtp.sendmail(me, you, msg.as_string())
	# 	smtp.quit()

if __name__ == '__main__':

	sender = MainSender()
	sender.send_mail('sbahn42@gmail.com', 'sbahn42@gmail.com', "정상 완료")
