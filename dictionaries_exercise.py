# 6-1 Person
# person = {
# 	"first_name":"Tapsi",
# 	"last_name":"Walia",
# 	"age":"35",
# 	"city":"Delhi"
# }

# print(person["first_name"])
# print(person["last_name"])
# print(person["age"])
# print(person["city"])

# 6-2 Favorite Numbers
# favorite_numbers = {
# 	"Tapsi":7,
# 	"Chirag":29,
# 	"Aradhya":3,
# 	"Amyra":15,
# 	"Indu": 4,
# }

# print("Tapsi:" + str(favorite_numbers["Tapsi"]))
# print("Chirag:" + str(favorite_numbers["Chirag"]))
# print("Aradhya:" + str(favorite_numbers["Aradhya"]))
# print("Amyra:" + str(favorite_numbers["Amyra"]))
# print("Indu:" + str(favorite_numbers["Indu"]))
# print(f'Tapsi: {str(favorite_numbers["Tapsi"])}')

# 6-3 Glossary
# glossary = {
# 	"variable":"temporarily stores a value",
# 	"list":"Collection of items in a particular order",
# 	"dictionary":"Collection of name value pairs",
# 	"conditional_test":"Expression that evaluates to true or false",
# 	"data_type": "Simple Data types are string, float, float and boolean"
# }

# print(f'Variable: \n\t\t {glossary["variable"].title()}')
# print(f'List: \n\t\t {glossary["list"].title()}')
# print(f'Dictionary: \n\t\t {glossary["dictionary"].title()}')
# print(f'Conditional Test: \n\t\t {glossary["conditional_test"].title()}')
# print(f'Data Type: \n\t\t {glossary["data_type"].title()}')

# 6-4 Glossary 2
# glossary = {
# 	"variable":"temporarily stores a value",
# 	"list":"Collection of items in a particular order",
# 	"dictionary":"Collection of name value pairs",
# 	"conditional_test":"Expression that evaluates to true or false",
# 	"data_type": "Simple Data types are string, float, float and boolean", 
# 	"set": "Collection in which items must be unique",
# }

# for key,value in glossary.items():
# 	print(f"{key}: \n\t\t {value}")

# 6-5 Rivers
# rivers = {
# 	"nile": "egypt",
# 	"ganga": "india",
# 	"amazon": "brazil"
# }

# for river,country in rivers.items():
# 	print(f'{river.title()} flows through {country.title()}')

# print("\n")
# for river in rivers.keys():
# 	print(f"{river.title()}")

# print("\n")
# for country in rivers.values():
# 	print(f"{country}")

# 6-6 Polling
favorite_language = {
	"chirag":"python",
	"tapsi":"java",
	"aradhya":"c",
	"amyra":"go",
	"ajit": "c++"
}

mandatory_poll = ["chirag", "tapsi", "indu"]

for person in mandatory_poll:
	if (person in favorite_language.keys()):
		print(f"Thank you {person.title()} for taking the poll")
	else:
		print(f"{person.title()}, Can you please take the poll?")