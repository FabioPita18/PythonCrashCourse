def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(f"First Name: {user_profile['first_name'].title()}")
print(f"Last Name: {user_profile['last_name'].title()}")
print(f"Location: {user_profile['location'].title()}")
print(f"Field: {user_profile['field'].title()}")