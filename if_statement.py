# Cars
# cars = ["audi","ferrari","bmw", "kia"]

# for car in cars:
# 	if (car == "bmw"):
# 		print(car.upper())
# 	else:
# 		print(car.title())

# Toppings
# topping = 'mushroom'

# if topping != 'olives':
# 	print("Hold the Olives")

#	Magic Number
# number = 18
# if (number != 29):
# 	print("That is not the correct answer, please try again!")

# Age
# age_0 = 22
# age_1 = 18

# if ((age_0 >= 21) or (age_1 >= 21)):
# 	print("We have an adult")
# else:
# 	print("We have only children")

# More Toppings
# toppings = ['mushroom', 'pineapple', 'onions']
# if ('mushroom' in toppings):
# 	print("We have a mushroom topping")
# if ('olives' in toppings):
# 	print("We have Olives in the toping")
# else:
# 	print("We do not have an Olive topping")

# Banned List
# banned_list = ['john','raphinha','saumya']
# user = 'abhay'
# if (user not in banned_list):
# 	print(f"{user.title()}, You are welcome to enter!")

# if statement
# age = 17
# if (age >= 18):
# 	print("You are old enough to vote")
# 	print("Have you registered to vote yet?")
# else:
# 	print("Sorry, you are too yound to vote!")
# 	print("Please register to vote when you turn 18")

# Amusement Park
# age = 12
# if (age < 4):
# 	price = 0
# elif (age < 18):
# 	price = 25
# elif (age < 65):
# 	price = 40
# elif (age >= 65):
# 	price = 20

# print(f"Your admission cost is ${price}")

# Toppings
# toppings = ['mushroom','onion','extra cheese']
# if ('mushroom' in toppings):
# 	print("Adding Mushrooms")
# elif('olives' in toppings):
# 	print("Adding Olives")
# elif('extra cheese' in toppings):
# 	print("Adding Extra Cheese")

# Pizzeria
# requested_toppings = ["mushroom","onion","extra cheese"]
# requested_toppings = []

# if (requested_toppings):
# 	for requested_topping in requested_toppings:
# 		if (requested_topping == "onion"):
# 			print("Sorry! we are out of onions right now!")
# 		else:
# 			print(f"Adding {requested_topping}")

# 	print("\nFinished Making your pizza")
# else:
# 	print("Are you sure you want a plain pizza?")

# Toppings Requesed
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if (requested_topping in available_toppings):
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have the {requested_topping} topping")

print("\nFinished Making your pizza")