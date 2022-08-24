# # 9-1 Restaurant
# class Restaurant:
# 	def __init__(self,restaurant_name,cuisine_type):
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type

# 	def describe_restaurant(self):
# 		print(f"\nThe restaurant is called '{self.restaurant_name}'")
# 		print(f"The restraurant serves {self.cuisine_type} food")

# 	def open_restaurant(self):
# 		print("\nThe restraurant is now OPEN!")

# restaurant = Restaurant("Juggernaut","South Indian")
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)
# restaurant.open_restaurant()
# restaurant.describe_restaurant()

# 9-2 Three Restaurants
# class Restaurant:
# 	def __init__(self,restaurant_name,cuisine_type):
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type

# 	def describe_restaurant(self):
# 		print(f"\nThe restaurant is called '{self.restaurant_name}'")
# 		print(f"The restraurant serves {self.cuisine_type} food")

# 	def open_restaurant(self):
# 		print("\nThe restraurant is now OPEN!")

# restaurant1 = Restaurant("Juggernaut","South Indian")
# restaurant2 = Restaurant("Mainland China","Chinese")
# restaurant3 = Restaurant("Bikanerwala","North Indian")

# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

# 9-3 Users
# class User:
# 	def __init__(self,first_name,last_name, email="", age=None, gender = ""):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.email = email
# 		self.age = age
# 		self.gender = gender

# 	def describer_user(self):
# 		print(f"User Details below: \n\tFirst Name: {self.first_name}\n\tLast Name: {self.last_name}")
# 		if(self.age):
# 			print(f"\tAge: {self.age}")
# 		if(self.email):
# 			print(f"\tEmail: {self.email}")
# 		if(self.gender):
# 			print(f"\tGender: {self.gender}")

# 	def greet_user(self):
# 		print(f"\nWelcome to Python Club {self.first_name} {self.last_name}!!!\n")

# user1 = User(first_name = "Chirag",last_name = "Walia", age = 38, gender="M")
# user1.describer_user()
# user1.greet_user()
# user1 = User(first_name = "Tapsi",last_name = "Walia", age = 35, gender="F")
# user1.describer_user()
# user1.greet_user()

# 9-4 Number Served
# class Restaurant:
# 	def __init__(self,restaurant_name,cuisine_type):
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type
# 		self.number_served = 0

# 	def describe_restaurant(self):
# 		print(f"\nThe restaurant is called '{self.restaurant_name}'")
# 		print(f"The restraurant serves {self.cuisine_type} food")

# 	def open_restaurant(self):
# 		print("\nThe restraurant is now OPEN!")

# 	def set_number_served(self, number_served):
# 		self.number_served = number_served

# 	def increment_number_served(self, increment):
# 		self.number_served += increment

# restaurant = Restaurant("Juggernaut","South Indian")
# print(f"Number of customers served: {restaurant.number_served}")
# restaurant.number_served = 5
# print(f"Number of customers served: {restaurant.number_served}")
# restaurant.set_number_served(10)
# print(f"Number of customers served: {restaurant.number_served}")
# restaurant.increment_number_served(3)
# print(f"Number of customers served: {restaurant.number_served}")
# restaurant.increment_number_served(8)
# print(f"Number of customers served: {restaurant.number_served}")

# 9-5 Login attempts
# class User:
# 	def __init__(self,first_name,last_name, email="", age=None, gender = "", login_attempts=0):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.email = email
# 		self.age = age
# 		self.gender = gender
# 		self.login_attempts = login_attempts

# 	def describer_user(self):
# 		print(f"User Details below: \n\tFirst Name: {self.first_name}\n\tLast Name: {self.last_name}")
# 		if(self.age):
# 			print(f"\tAge: {self.age}")
# 		if(self.email):
# 			print(f"\tEmail: {self.email}")
# 		if(self.gender):
# 			print(f"\tGender: {self.gender}")

# 	def greet_user(self):
# 		print(f"\nWelcome to Python Club {self.first_name} {self.last_name}!!!\n")

# 	def increment_login_attempts(self):
# 		self.login_attempts += 1

# 	def reset_login_attempts(self):
# 		self.login_attempts = 0

# user1 = User(first_name = "Chirag",last_name = "Walia", age = 38, gender="M")
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()
# print(f"Count of login attempts: {user1.login_attempts}")
# user1.reset_login_attempts()
# print(f"Count of login attempts: {user1.login_attempts}")

# 9-6 Ice Cream Stand
# class Restaurant:
# 	def __init__(self,restaurant_name,cuisine_type):
# 		self.restaurant_name = restaurant_name
# 		self.cuisine_type = cuisine_type

# 	def describe_restaurant(self):
# 		print(f"\nThe restaurant is called '{self.restaurant_name}'")
# 		print(f"The restraurant serves {self.cuisine_type} food")

# 	def open_restaurant(self):
# 		print("\nThe restraurant is now OPEN!")

# class IceCreamStand(Restaurant):
# 	def __init__(self,restaurant_name,cuisine_type):
# 		super().__init__(restaurant_name,cuisine_type)
# 		self.flavours = ["Mango","Orange","Chocolate"]

# 	def display_flavours(self):
# 		print(f"The {self.restaurant_name} Restaurant offers the following flavours: ")
# 		for flavour in self.flavours:
# 			print(f"\t{flavour}")

# icecreamstand = IceCreamStand("Baskin Robbins","Ice Cream")
# icecreamstand.display_flavours()

# # 9-7 Admin
# class User:
# 	def __init__(self,first_name,last_name, email="", age=None, gender = ""):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.email = email
# 		self.age = age
# 		self.gender = gender
# 	def describer_user(self):
# 		print(f"User Details below: \n\tFirst Name: {self.first_name}\n\tLast Name: {self.last_name}")
# 		if(self.age):
# 			print(f"\tAge: {self.age}")
# 		if(self.email):
# 			print(f"\tEmail: {self.email}")
# 		if(self.gender):
# 			print(f"\tGender: {self.gender}")

# 	def greet_user(self):
# 		print(f"\nWelcome to Python Club {self.first_name} {self.last_name}!!!\n")

# class Admin(User):
# 	'''Admin user'''
# 	def __init__(self,first_name,last_name):
# 		'''Initialize the admin user and invoke the User class init method'''
# 		super().__init__(first_name,last_name)
# 		self.privileges = ["Add Post", "Delete Post","Ban User","Add User"]

# 	def show_privileges(self):
# 		'''Show privileges for the admin user'''
# 		print(f"The admin user {self.first_name} {self.last_name} has these privileges:")
# 		for privilege in self.privileges:
# 			print(f"\t{privilege}")

# user1 = Admin("Chirag","Walia")
# user1.show_privileges()

# 9-8 Privileges
# class User:
# 	def __init__(self,first_name,last_name, email="", age=None, gender = ""):
# 		self.first_name = first_name
# 		self.last_name = last_name
# 		self.email = email
# 		self.age = age
# 		self.gender = gender
# 	def describer_user(self):
# 		print(f"User Details below: \n\tFirst Name: {self.first_name}\n\tLast Name: {self.last_name}")
# 		if(self.age):
# 			print(f"\tAge: {self.age}")
# 		if(self.email):
# 			print(f"\tEmail: {self.email}")
# 		if(self.gender):
# 			print(f"\tGender: {self.gender}")

# 	def greet_user(self):
# 		print(f"\nWelcome to Python Club {self.first_name} {self.last_name}!!!\n")

# class Admin(User):
# 	'''Admin user'''
# 	def __init__(self,first_name,last_name):
# 		'''Initialize the admin user and invoke the User class init method'''
# 		super().__init__(first_name,last_name)
# 		self.admin_privileges = Privileges() 

# class Privileges():
# 	'''Privilege Object'''
# 	def __init__(self):
# 		self.privileges = ["Add Post", "Delete Post","Ban User","Add User"]

# 	def show_privileges(self):
# 		'''Show privileges for the admin user'''
# 		print("The user has the following privileges:")		
# 		for privilege in self.privileges:
# 			print(f"\t{privilege}")

# user1 = Admin("Chirag","Walia")
# user1.admin_privileges.show_privileges()

# 9-10 Imported Restaurant
from restaurant import Restaurant
my_restaurant = Restaurant("Juggernaut","South Indian")
my_restaurant.describe_restaurant()