''' Restaurant Module with Restaurant class'''
class Restaurant:
	'''Restaurant class'''
	def __init__(self,restaurant_name,cuisine_type):
		'''Init method for restaurant class requiring input as restaurant name and cuisine'''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		'''Describes the details of the restaurant'''
		print(f"\nThe restaurant is called '{self.restaurant_name}'")
		print(f"The restraurant serves {self.cuisine_type} food")

	def open_restaurant(self):
		'''Print that the restaurant is open'''
		print("\nThe restraurant is now OPEN!")