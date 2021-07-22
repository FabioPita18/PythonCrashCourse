bicycles= ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

bicycles.append('diamond back')
print(bicycles)

bicycles.insert(1, 'mountain trail')
print(bicycles)

del bicycles[1]
print(bicycles)

poppedBicycle= bicycles.pop()
print(poppedBicycle)
print(bicycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

print(cars)
cars.reverse()
print(cars)

print(len(cars))