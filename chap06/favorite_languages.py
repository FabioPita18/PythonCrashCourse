favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

language1 = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language1}.")

language2 = favorite_languages.get('John', 'No point value assigned')
print({language2})

favorite_foods = {
'keagan': 'pizza',
'sarah': 'pasta',
'edward': 'chicken',
'phil': 'steak',
}

for key, value in favorite_foods.items():
		print(f'Key: {key.title()},  value: {value.title()}')

print('Accessing keys')
for key in favorite_foods.keys():
		print(f'Key: {key.title()}')


print('Accessing values')
for key in favorite_foods.values():
		print(f'value: {key.title()}')


#6-6

languange_poll = ['phil', 'jen', 'keags', 'jerry']

for names in languange_poll:
	for names2 in favorite_languages.keys():
		if names==names2:
			print(f'{names} thank you')
			break
	else:
		print(f'{names} come join the poll')