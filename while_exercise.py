# 7-4 Pizza Toppings
# prompt = "\n Enter the pizza toppings that you desire."
# prompt += "\n Enter 'quit' to finish: \n"

# active = True
# while(active):
# 	topping = input(prompt)
# 	if (topping == 'quit'):
# 		break
# 	else:
# 		print(f"Adding {topping} to the pizza")

# 7-5 Movie Tickets
prompt = "\nEnter your age"
prompt += "\nEnter 0 to finish: "
active = True

while (active):
	age = int(input(prompt))

	if (age ==0):
		break
	elif(age < 3):
		cost = "free"
	elif (age <= 12):
		cost = "$10"
	else:
		cost = "$15"

	print(f"The costs of movie ticket are {cost}")

