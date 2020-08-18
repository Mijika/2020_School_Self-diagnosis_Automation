USERS_DATA = '../users_data.txt'

users = list()

with open(USERS_DATA, 'r', encoding='UTF8') as f:
	while True:
	    line = f.readline()

	    name = line[0:3]
	    key = line[4:10]

	    if not line: break
	    users.append([name, key])

print(users)

