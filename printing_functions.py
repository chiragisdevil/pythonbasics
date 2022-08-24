# 3D Printing with functions

# Print designs
def print_designs(unprinted_designs,printed_designs):
	'''Print designs from unprinted_design list and then move them to the printed design list'''
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing the design: {current_design}")
		printed_designs.append(current_design)

def show_completed(printed_designs):
	'''Show all the designs in the printed_designs list passed as input'''
	for printed_design in printed_designs:
		print(printed_design)