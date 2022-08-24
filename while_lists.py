# Moving items from one list to another
# confirmed_users = []
# unconfirmed_users = ["Chirag","Tapsi","Aradhya","Amyra","Ajit","Indu"]

# while unconfirmed_users:
# 	user = unconfirmed_users.pop()
# 	print(f"Verifying user {user}")
# 	confirmed_users.append(user)

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
# 	print(confirmed_user.title())

# Removing a particular (multi) value from the list
# users = ["Chirag","Tapsi","Aradhya","Chirag","Amyra","Ajit","Chirag","Indu"]

# while ("Chirag" in users):
# 	users.remove("Chirag")

# print(users)

# Polling - Filing dictionary with user input
polling_active = True
poll_response = {}

while(polling_active):
	name = input("Enter your name: ")
	response = input("\n Which icecream do you like the most? ")
	poll_response[name] = response

	cont = input("Do you want to let another person respond? (Yes/No): ")
	if (cont == "No"):
		break

print(poll_response)