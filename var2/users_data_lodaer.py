import os

USERS_DATA_PATH = './users_data2.txt'
# USERS_DATA_PATH = './test_data.txt'

class Users_data_loader():
	def __init__(self):
		self.user_data_list = []
		self.error_check = False

		try:
			self.data_load()
			pass
		except Exception as e:
			print(e)


	def data_load(self):
		with open(USERS_DATA_PATH, 'r', encoding='UTF8') as f:
			while True:
				data = f.readline()

				if not data:
					break

				name, date_of_birth, password = data.split()
				self.user_data_list.append([name, date_of_birth, password])

	def get_users_data(self):
		return self.user_data_list

if __name__ == '__main__':
	data_controller = Users_data_loader()
	data_list = data_controller.get_users_data()
	print(data_list)
