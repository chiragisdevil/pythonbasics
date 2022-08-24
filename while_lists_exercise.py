# 7-8 Deli
# sandwich_order = ["spinach","mayo veg","egg","panner"]
# finished_sandwiches = []

# while (sandwich_order):
# 	sandwich = sandwich_order.pop()
# 	print(f"I made you a {sandwich} sandwich")
# 	finished_sandwiches.append(sandwich)

# print("\nThe following sandwiches were made: ")

# for sandwich in finished_sandwiches:
# 	print(f"\t{sandwich}")

# 7-9 pastrami
# sandwich_order = ["pastrami","spinach","pastrami","mayo veg","egg","panner","pastrami"]
# finished_sandwiches = []

# print("Apologies, We have run out of Pastrami!!\n")

# while ("pastrami" in sandwich_order):
# 	sandwich_order.remove("pastrami")

# while (sandwich_order):
# 	sandwich = sandwich_order.pop()
# 	print(f"I made you a {sandwich} sandwich")
# 	finished_sandwiches.append(sandwich)

# print("\nThe following sandwiches were made: ")

# for sandwich in finished_sandwiches:
# 	print(f"\t{sandwich}")

# 7-10 Dream Vacation

vacation = {}
poll_active = True
prompt = "If you could visit one place in the world where would you go?"

while poll_active:
	name = input("Enter your name: ")
	place = input(prompt)
	vacation[name] = place

	cont = input("Continue for another user (Y/N)?")
	if cont == 'N':
		poll_active = False

print(vacation)



