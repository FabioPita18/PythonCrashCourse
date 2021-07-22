# Question 15 and Questin 16
import datetime

class Person:

	def __init__(self, name, surname, birthdate, email, middleName=''):
		self.name = name
		self.middleName = middleName
		self.surname = surname
		self.birthdate = birthdate
		self.email = email

	def details(self):
		print(self.name)
		print(self.middleName)
		print(self.surname)
		print(self.birthdate)
		print(self.email)

person1 = Person('Fabio', 'Pita', datetime.date(2002, 7, 20), 'fabiopita267@gmail.com', 'Miguel')
person2 = Person('Tony', 'Gallucci', datetime.date(2002, 6, 24), 'agallucci@gmail.com')

person1.details()
person2.details()