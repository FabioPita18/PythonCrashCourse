users = {
'aeinstein': {
				'first': 'albert',
				'last': 'einstein',
				'location': 'princeton',
			 },
'mcurie': {
				'first': 'marie',
				'last': 'curie',
				'location': 'paris',
			},
}


for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']
	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")

Students = {
'fpita': {
				'first_name': 'fabio',
				'last_name': 'pita',
				'second_name': 'miguel',
			 },
'tgallucci': {
				'first_name': 'toni',
				'last_name': 'gallucci',
				'second_name': 'pizza',
			},
}

for student_code, student_info in Students.items():
	print(f"\nStudent code: {student_code}")
	full_name = f"{student_info['first_name']} {student_info['second_name']} {student_info['last_name']}"
	print(f"\tFull name: {full_name.title()}")