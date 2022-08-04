# 3 Aliens

# alien_0 = {'colour':'green', 'points':5}
# alien_1 = {'colour':'yellow', 'points':10}
# alien_2 = {'colour':'red', 'points':10}

# aliens = [alien_0,alien_1,alien_2]

# for alien in aliens:
# 	print(alien)

# Several Aliens
# aliens = []

# for alien_num in range(0,30):
# 	new_alien = {'colour':'green', 'points':5}
# 	aliens.append(new_alien)

# for alien in aliens[:3]:
# 	if (alien['colour'] == 'green'):
# 		alien['colour'] = 'yellow'
# 		alien['points'] = 10

# for alien in aliens[:5]:
# 	print(alien)

# print(f"Total Aliens created are: {len(aliens)}")

# Pizza Toppings list
# pizza = {
# 	'crust':'thin',
# 	'toppings': ['mushrooms','olives']
# }

# print(f"You have ordered {pizza['crust']} pizza with following toppings:")

# for topping in pizza['toppings']:
# 	print(f"\t {topping}") 

# Favorite Languages as a list
# favorite_languages = {
# 	'chirag':['python','java','javascript'],
# 	'tapsi':['python'],
# 	'aradhya':['c','python'],
# 	'amyra':'c',
# }

# for name,languages in favorite_languages.items():
# 	print(f"{name.title()}'s favorite languages are:")

# 	for language in languages:
# 		print(f"\t {language.title()}")

# Users - Dictionary inside dictionary
users = {
	'chiragisdevil':{
		'fname':'chirag',
		'lname':'walia'
	},
	'tapsiwalia29':{
		'fname':'tapsi',
		'lname':'walia'
	}
}

for user, user_details in users.items():
	print(f"Username: {user}")
	print(f"Full Name: {user_details['fname']} {user_details['lname']} \n")