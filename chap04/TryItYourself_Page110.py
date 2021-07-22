#4-3
for value in range(1, 21):
	print(value)

#4-4
numbers = list(range(1, 1000001))
for number in numbers:
	print(number)

#4-5
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

#4-7
Threes = list(range(3, 31, 3))
for Three in Threes:
	print(Three)

#4-8
cubes=list(range(1,11))
for cube in cubes:
	cube=cube**3
	print(cube)

#4-9
cubes = [value**3 for value in range(1, 11)]
print(cubes)