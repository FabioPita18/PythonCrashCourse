Person = {'first_name': 'fabio',
		  'last_name': 'pita',
		  'age': '19',
   		'city' : 'johannesburg'
			}
for key, value  in Person.items():
	print(f' {key.title()}, {value.title()}' )

#6-2	
FavoriteNumbers = {'fabio' : '1',
		 		 'tony':'2',
		 		 'herc': '3',
   				'rick' : '4',
   				'morty':'5'
			}
for key, value  in FavoriteNumbers.items():
	print(f' {key.title()}, {value.title()}' )

glossary={
			'concatenate':'to add to an existing variable',
			'increment': 'to add to a value incremently',
			'decrement': 'to subtract from a value incremently',
			'modula': 'provides you with the remiander when dividing two numbers',
			'int': 'converts a string into a number'
}	

for key, value  in glossary.items():
	print(f' {key.title()}, {value.title()}\n')

#6-4
glossary={
			'concatenate':'to add to an existing variable',
			'increment': 'to add to a value incremently',
			'decrement': 'to subtract from a value incremently',
			'modula': 'provides you with the remiander when dividing two numbers',
			'int': 'converts a string into a number',
			'>>>': 'This is the default prompt of the Python interactive shell. We have seen this a lot in our examples.',
			' …':'The default prompt of the Python interactive shell when entering code under an indented block or within a pair of matching delimiters. Delimiters may be parentheses, curly braces, or square brackets.This is also called the ellipsis object.',
			'Asynchronous Context Manager':'ACM is an object that controls the environment observed in an async with statement. It does so by defining __aenter__() and __aexit__().',
			'Attribute':'An attribute is a value an object holds. We can access an object’s attributes using the dot operator (.). In our examples, we have done this as following:',
			'Awaitable':'Any object in Python that we can use in an await expression is an awaitable. It can be a coroutine or any object with an __await__() method'

}	

for key, value  in glossary.items():
	print(f'Term: {key.title()}, Definition: {value.title()}\n')

#6-5
rivers= {
			'nile':'egypt',
			'amazon': 'south america',
			'mississippi': 'USA'
}

for key in rivers.keys():
	print(f' {key.title()}\n')

for value in rivers.values():
	print(f' {value.title()}\n')
