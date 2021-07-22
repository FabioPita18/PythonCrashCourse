# def get_formatted_name(first_name, last_name):
# 	"""Return a full name, neatly formatted."""
# 	full_name = f"{first_name} {last_name}"
# 	return full_name.title()

# musician1 = get_formatted_name('jimi', 'hendrix')
# musician2 = get_formatted_name('travis', 'scott')
# musician3 = get_formatted_name('j.', 'cole')
# print(f'{musician1}\n{musician2}\n{musician3}')

def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"

	return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)