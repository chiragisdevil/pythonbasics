# 6-7 People
# person_1 = {
# 	"fname":"Chirag",
# 	"lname":"Walia",
# 	"city":"Delhi"
# }

# person_2 = {
# 	"fname":"Tapsi",
# 	"lname":"Walia",
# 	"city":"Shamli"
# }

# person_3 = {
# 	"fname":"Ajit",
# 	"lname":"Walia",
# 	"city":"Delwara"
# }

# people = [person_1, person_2,person_3]

# for person in people:
# 	print(f"Name: {person['fname']} {person['lname']}")
# 	print(f"City: {person['city']} \n")

# 6-8 Pets
# choco = {
# 	"name":"choco",
# 	"type":"dog",
# 	"owner":"aradhya",
# }

# meow = {
# 	"name":"meow",
# 	"type":"cat",
# 	"owner": "amyra",
# }

# slimy = {
# 	"name":"slimy",
# 	"type":"snake",
# 	"owner":"chirag",
# }

# pets = [choco,meow,slimy]

# for pet in pets:
# 	print(f"{pet['name'].title()} is a {pet['type']} belonging to {pet['owner'].title()}")

# 6-9 Favorite Places
# favorite_places = {
# 	"Chirag":["Goa","Scotland"],
# 	"Tapsi":["Reading","Goa","Malaysia"],
# 	"Aradhya":["Singapore"],
# }

# for name,places in favorite_places.items():
# 	print(f"{name}'s favorite places are:")
# 	for place in places:
# 		print(f"\t {place}")

# 6-11 Cities
cities = {
	"delhi":{
		"country":"india",
		"population":"32M",
		"fact":"Delhi is the home to the largest market of spices in Asia",
	},
	"london":{
		"country":"england",
		"population":"9M",
		"fact":"London Is The Smallest City In England",
	},
	"rennes":{
		"country":"france",
		"population":"0.2M",
		"fact":"Tenth largest city in france",
	},
}

for city, details in cities.items():
	print(f"City: {city.title()}")
	for detail,value in details.items():
		print(f"\t{detail.title()} : {value.title()}")
	
