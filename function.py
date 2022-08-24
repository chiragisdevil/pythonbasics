# def describe_animal(pet_name,animal_type="dog"):
# 	'''Display Pet information '''
# 	print(f"I have a {animal_type.title()}")
# 	print(f"My {animal_type.title()}'s name is {pet_name.title()}\n")

# describe_animal(animal_type = "cat",pet_name = "Citcat")
# describe_animal(pet_name = "choco")
# describe_animal("bunu")


# def get_formatted_name(first_name,last_name):
# 	'''Return a properly formatted name'''
# 	full_name = f"{first_name.title()} {last_name.title()}"
# 	return full_name

# musician = get_formatted_name("jimi","hendrix")
# print(musician)

# def get_formatted_name(first_name,last_name,middle_name=''):
# 	'''Return a properly formatted name'''
# 	if middle_name:
# 		full_name = f"{first_name} {middle_name} {last_name}"
# 	else:
# 		full_name = f"{first_name} {last_name}"
# 	return full_name

# musician = get_formatted_name("John","Hooker","Lee")
# print(musician)
# musician = get_formatted_name("Jimi","Hendrix")
# print(musician)

# def build_person(first_name,last_name):
# 	person = {"first":first_name,"last":last_name}
# 	return person

# normal_person = build_person("Chirag","Walia")
# print(normal_person)

# def build_person(first_name,last_name, age = None):
# 	person = {"first":first_name,"last":last_name}
# 	if age:
# 		person['age'] = age
# 	return person

# normal_person = build_person("Chirag","Walia")
# print(normal_person)
# normal_person = build_person("Chirag","Walia",38)
# print(normal_person)

# def get_formatted_name(first_name,last_name):
# 	'''Return a properly formatted name'''
# 	full_name = f"{first_name.title()} {last_name.title()}"
# 	return full_name

# while(True):
# 	print("\nEnter your name ")
# 	print("Enter 'q' to quit ")

# 	f_name = input("\nFirst Name: ")
# 	if (f_name == 'q'):
# 		break

# 	l_name = input("Last Name: ")
# 	if (f_name == 'q'):
# 		break

# 	print(f"\nHello {get_formatted_name(f_name,l_name)}")

# Greet User - Passing a list
# def greet_users(users):
# 	'''Takes a users list as an input and greets each of them individually'''
# 	for user in users:
# 		print(f"Hello {user.title()}!")

# user_names = ["chirag","tapsi","aradhya"]
# greet_users(user_names)

# # 3D Printing without functions
# unprinted_designs = ["phone case","robot","toy"]
# printed_designs = []

# # Print designs
# while unprinted_designs:
# 	current_design = unprinted_designs.pop()
# 	print(f"Printing the design: {current_design}")
# 	printed_designs.append(current_design)

# print("\n")
# #Display completed designs
# for printed_design in printed_designs:
# 	print(printed_design)

# 3D Printing with functions

# Print designs
# def print_designs(unprinted_designs,printed_design):
# 	'''Print designs from unprinted_design list and then move them to the printed design list'''
# 	while unprinted_designs:
# 		current_design = unprinted_designs.pop()
# 		print(f"Printing the design: {current_design}")
# 		printed_designs.append(current_design)

# def show_completed(printed_designs):
# 	'''Show all the designs in the printed_designs list passed as input'''
# 	for printed_design in printed_designs:
# 		print(printed_design)

# unprinted_designs = ["phone case","robot","toy"]
# printed_designs = []
# print_designs(unprinted_designs[:],printed_designs)
# print("\n")
# show_completed(printed_designs)

# print(unprinted_designs)

# # Pizza
# def make_pizza(*toppings):
# 	print(toppings)

# make_pizza("Cheese")
# make_pizza("Cheese","Olives","Mushrooms")

# Pizza
# def make_pizza(size, *toppings):
# 	'''Make a pizza with certain toppings passed to it as input'''
# 	print(f"Making a {size} inch pizza with the following toppings: ")
# 	for topping in toppings:
# 		print(f"\t -{topping}")

# make_pizza(16,"Cheese")
# make_pizza(18,"Cheese","Olives","Mushrooms")

# Build User Profile
# def build_user_profile(first_name,last_name,**user_info):
# 	'''Build a dictionary containing the details of the user'''
# 	user_info["first_name"] = first_name
# 	user_info["last_name"] = last_name
# 	return user_info

# user_profile = build_user_profile(
# 	"Chirag",
# 	"Walia",
# 	location = "Delhi",
# 	role = "Architect"
# )

# print(user_profile)

# from pizza import *
# make_pizza(18,"cheese","mushroom")
# make_pizza(12,"cheese","tomato","onion","mushrooms","capsicum")
