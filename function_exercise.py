# 8-3 T-Shirt
# def make_shirt(size, print_text):
# 	print(f'The T-Shirt of size {size} says "{print_text}"')

# make_shirt("small","Devil's Child")
# make_shirt(size="medium",print_text="Love & Peace")

# 8-4 Large Shirts
# def make_shirt(size="large", print_text="I love Python"):
# 	print(f'The T-Shirt of size {size} says "{print_text}"')

# make_shirt()
# make_shirt(size="medium")
# make_shirt(size="small",print_text="Love and Peace")

# 8-5 Cities
# def describe_city(city_name,country="India"):
# 	print(f"{city_name.title()} is in {country.title()}")

# describe_city("Delhi")
# describe_city(city_name="Bangalore",country="India")
# describe_city("London","UK")

# 8-6 City Names
# def city_country(city,country):
# 	return f"{city.title()}, {country.title()}"

# print(city_country("Bangalore","India"))
# print(city_country("London","United Kingdom"))
# print(city_country("Perth","australia"))

# 8-7 Album
# def make_album(artist,title,count_songs=None):
# 	album = {"artist":artist,"title":title}
# 	if count_songs:
# 		album['song_count'] = count_songs

# 	return album

# print(make_album("Metallica","The Black Album"))
# print(make_album("Kr$na","Still Here"))
# print(make_album("Pantera","Vulgar Display of Power"))
# print(make_album("Iron Maiden","Fear of the Dark",12))

# 8-9 Messages
# messages = ["hi","whats up","will you do frandship with me"]

# def show_messages(messages):
# 	'''Prints the messages passed to it as a list'''
# 	for message in messages:
# 		print(message)

# # 8-10 Sending Messages
# messages = ["hi","whats up","will you do frandship with me"]
# sent_messages = []

# def show_messages(messages):
# 	'''Prints the messages passed to it as a list'''
# 	for message in messages:
# 		print(message)

# def send_messages(messages,sent_messages):
# 	'''Print the messages in the list messages and move it to a new list sent_messages'''
# 	while(messages):
# 		message = messages.pop()
# 		print(message)
# 		sent_messages.append(message)

# show_messages(messages)
# print("\n")
# send_messages(messages,sent_messages)
# print("\n")
# print(messages)
# print(sent_messages)

# # 8-10 Archiving Messages
# messages = ["hi","whats up","will you do frandship with me"]
# sent_messages = []

# def show_messages(messages):
# 	'''Prints the messages passed to it as a list'''
# 	for message in messages:
# 		print(message)

# def send_messages(messages,sent_messages):
# 	'''Print the messages in the list messages and move it to a new list sent_messages'''
# 	while(messages):
# 		message = messages.pop()
# 		print(message)
# 		sent_messages.append(message)

# show_messages(messages)
# print("\n")
# send_messages(messages[:],sent_messages)
# print("\n")
# print(messages)
# print(sent_messages)

# 8-12 Sandwiches
# def make_sandwich(*items):
# 	'''Make a sandwich by printing all items accepted in an arbitrary argument'''
# 	print("\nMaking sandwich with following items: ")
# 	for item in items:
# 		print(f" - {item}")

# make_sandwich("lettuce","tomato","cheese")
# make_sandwich("cheese")
# make_sandwich("lettuce","tomato","cucumber","onions")

# 8-13 User Profile 
# def build_user_profile(first_name,last_name,**user_info):
# 	'''Build a dictionary containing the details of the user'''
# 	user_info["first_name"] = first_name
# 	user_info["last_name"] = last_name
# 	return user_info

# user_profile = build_user_profile(
# 	"Chirag",
# 	"Walia",
# 	location = "Delhi",
# 	role = "Architect",
# 	experience = 17
# )

# print(user_profile)

# 8-14 Cars
# def create_car(manufacturer,model,**car_props):
# 	car_props["manufacturer"] = manufacturer
# 	car_props["model"] = model
# 	return car_props

# car = create_car("kia","carens",color="grey",price=13)
# print(car)

# 8-15 Printing Models
from printing_functions import print_designs,show_completed
unprinted_designs = ["phone case","robot","toy"]
printed_designs = []
print_designs(unprinted_designs,printed_designs)
print("\n")
show_completed(printed_designs)