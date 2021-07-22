prompt ="Enter a number, and I'll tell you if it's even or odd."
prompt += "\nEnter 'quit' to exit"
message = ''

while True:
	message = input(prompt)

	if message == 'quit':
		break
	elif int(message) % 2 ==0:
		print(f"\nThe number {message} is even.")
	elif int(message) % 2 !=0:
		print(f"\nThe number {message} is odd.")
	else:
		print("Invalid Input!")