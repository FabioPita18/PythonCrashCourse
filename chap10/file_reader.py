file_path = 'text_folder/pi_digits.txt'


# with open(file_path) as file_object:
# 	contents = file_object.read()
# print(contents.rstrip())

with open(file_path) as file_object:
	lines = file_object.readlines()
# 	for line in lines:
#  		print(line.rstrip())

pi_string = ''
for line in lines:
	pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))