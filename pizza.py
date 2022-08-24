# Pizza
def make_pizza(size, *toppings):
	'''Make a pizza with certain toppings passed to it as input'''
	print(f"Making a {size} inch pizza with the following toppings: ")
	for topping in toppings:
		print(f"\t -{topping}")