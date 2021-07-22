# def make_pizza(*toppings):
# 	"""Print the list of toppings that have been requested."""
# 	print("\nMaking a pizza with the following toppings:")
# 	for topping in toppings:
# 		print(f"\t- {topping}")

# make_pizza()
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, price, *toppings):
	"""Summarize the pizza we are about to make."""
	print(f"\nMaking a {size}-inch pizza for ${price}, with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

# make_pizza(16, 15.5, 'pepperoni')
# make_pizza(12, 15.5, 'mushrooms', 'green peppers', 'extra cheese')