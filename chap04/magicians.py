magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
#4-10
names=['fabio', 'tony', 'rick','morty', 'squanchy', 'meseeks']
print('The first three items in the list are ')
for name in names[:3]: 
		print(f' my name is {name.title()}')

print('Three items from the middle of the list are ')
for name in names[2:5]: 
		print(f' my name is {name.title()}')	

print('The last three items in the list are ')
for name in names[3:6]: 
		print(f' my name is {name.title()}')