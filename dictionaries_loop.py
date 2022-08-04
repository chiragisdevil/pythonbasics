# user = {
# 	'user_name':'chiragisdevil',
# 	'first_name':'Chirag',
# 	'last_name':'Walia',
# }

# for key,value in user.items():
# 	print(f"\n Key: {key}")
# 	print(f" Value: {value}")


# Favorite Language
# favorite_language = {
# 	"Chirag":"python",
# 	"tapsi":"java",
# 	"aradhya":"Python",
# 	"amyra":"C",
# 	"Ajit":"go",
# 	"indu":"Javascript",
# }

# for name,language in favorite_language.items():
# 	print(f"{name.title()}'s favorite language is {language.title()}")

favorite_language = {
	"Chirag":"python",
	"tapsi":"java",
	"aradhya":"python",
	"amyra":"C",
	"Ajit":"go",
	"indu":"Javascript",
}

for language in set(favorite_language.values()):
	print(language)

# if ("Chandni" not in favorite_language.keys()):
# 	print("Chandni, please take the poll")

# friends = ['Chirag', 'aradhya']

# for name in sorted(favorite_language.keys()):
# 	print(f"Hi! {name.title()}")
# 	if (name in friends):
# 		print(f"\t{name.title()}, I see you love the language {favorite_language[name]}")

