# car = 'kia'
# print("Is car == 'kia'? I predict True")
# print(car=='kia')

# print("\nIs the car == 'audi'? I predict False")
# print(car=='audi')


# 5-3 Alien Colors #1
# alien_color = "green"

# if (alien_color == "green"):
# 	print("Player just earned 5 points!")

# 5-4 Alien Colors #2
# alien_color = "yellow"

# if (alien_color == "green"):
# 	print("Player just earned 5 points for shooting the alien!")
# else:
# 	print("Player earned 10 points")


# # 5-5 Alien Colors #3
# alien_color = "red"

# if (alien_color == "green"):
# 	print("Player just earned 5 points")
# elif (alien_color == "yellow"):
# 	print("Player earned 10 points")
# elif (alien_color == "red"):
# 	print("Player earned 15 points")

# 5-6 Stages of Life
# age = 65

# if (age < 2):
# 	print("Person is a baby")
# elif (age < 4):
# 	print("Person is a toddler")
# elif (age < 13):
# 	print("Person is a kid")
# elif (age < 20):
# 	print("Person is a teenager")
# elif (age < 65):
# 	print("Person is an adult")
# else:
# 	print("Person is an elder")

# 5-7 Favorite Fruit
# favorite_fruits = ["Mango", "Banana", "Peach"]

# if ("Mango" in favorite_fruits):
# 	print("You really like Mangoes")
# if ("Watermelon" in favorite_fruits):
# 	print("You really like Watermelons")
# if ("Banana" in favorite_fruits):
# 	print("You really like Bananas")
# if ("Peach" in favorite_fruits):
# 	print("You really like Peaches")
# if ("Oranges" in favorite_fruits):
# 	print("You really like Oranges")

# 5-8 Hello Admin
# user_names = ["chirag","tapsi","admin","aradhya","amyra"]


# for user_name in user_names:
# 	if user_name == 'admin':
# 		print("Hello admin, would you like to see a status report?")
# 	else:
# 		print(f"Hello {user_name}, thank you for logging in again")

# 5-9 No users
# user_names = []

# if (user_names):
# 	for user_name in user_names:
# 		if user_name == 'admin':
# 			print("Hello admin, would you like to see a status report?")
# 		else:
# 			print(f"Hello {user_name}, thank you for logging in again")
# else:
# 	print("We need to find some users")

# 5-10 Checking User Names
# current_users = ["CHIRAG","Tapsi","admin","aradhya","amyra"]
# new_users = ["ajit","indu","Chirag","TApsi","chandni"]

# current_users_lower = [user.lower() for user in current_users]

# for new_user in new_users:
# 	if (new_user.lower() in current_users_lower):
# 		print(f"Please enter a new username as {new_user} is already taken")
# 	else:
# 		print(f"Username {new_user} is available")

# 5-11 Ordinal Numbers
nums = [1,2,3,4,5,6,7,8,9]


for num in nums:
	if num == 1:
		suffix = "st"
	elif num == 2:
		suffix = "nd"
	elif num == 3:
		suffix = "rd"
	else:
		suffix = "th"
	print(f"{num}{suffix}")
