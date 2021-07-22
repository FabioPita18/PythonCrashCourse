class Dog:

	"""A simple attempt to model a dog."""

	def __init__(self, name, age, breed, colour):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age 
		self.breed = breed
		self.colour = colour

	def get_description(self):
		print(f"\nMy dog's name is {self.name}.")
		print(f"\nMy dog is {self.age} years old.")
		print(f"\nMy dog is a {self.colour} {self.breed}.")

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")


# my_dog = Dog('Willie', 6, 'Chua Chua', 'brown and white')
# tonys_dog= Dog('Gaby', 2, 'Rotti', 'brown and black')
# joaos_dog = Dog('Tia', 6, 'Sausage Dog', 'white')

# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age}. years old")
# print(f"My dog is a {my_dog.colour} {my_dog.breed}.")
# my_dog.sit()
# my_dog.roll_over()

# print(f"My dog's name is {tonys_dog.name}.")
# print(f"My dog is {tonys_dog.age}. years old")
# print(f"My dog is a {tonys_dog.colour} {tonys_dog.breed}.")
# tonys_dog.sit()
# tonys_dog.roll_over()

# print(f"My dog's name is {joaos_dog.name}.")
# print(f"My dog is {joaos_dog.age}. years old")
# print(f"My dog is a {joaos_dog.colour} {joaos_dog.breed}.")
# joaos_dog.sit()
# joaos_dog.roll_over()