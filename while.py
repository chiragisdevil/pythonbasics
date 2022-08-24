# Simple While 
# current_num = 1


# while (current_num <=5):
# 	print(current_num)
# 	current_num += 1

# Parrot
# prompt = "\nTell me something and I will repeat it after you"
# prompt += "\n Type 'quit' to finish: "

# message = ""
# while (message != 'quit'):
# 	message = input(prompt)
# 	if (message != 'quit'):
# 		print(message)

# Parrot with flag
# prompt = "\nTell me something and I will repeat it after you"
# prompt += "\n Type 'quit' to finish: "

# active = True
# while (active):
# 	message = input(prompt)
# 	if (message == 'quit'):
# 		active = False
# 	else:
# 		print(message)

# Cities
# prompt = "\n Enter the cities that you have visited"
# prompt += "\n Enter 'quit' to exit: "

# active = True
# while (active):
# 	city = input(prompt)
# 	if city == 'quit':
# 		break
# 	else:
# 		print(f"\nI love {city}")

# Odd numbers
current_num = 0
while (current_num < 10):
	current_num += 1
	if (current_num%2 == 0):
		continue
	else:
		print(current_num)