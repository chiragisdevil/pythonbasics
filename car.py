'''Class used to present a car'''
class Car:
	'''A simple attempt to represent a car'''
	def __init__(self,make,model,year):
		'''Initialize attributes of a car'''
		self.make = make
		self.model = model
		self.year = year
		self.distance_travelled = 0

	def get_descriptive_name(self):
		'''Gets the name in the format <Year> <Make> <Model> '''
		descriptive_name = f"{self.year} {self.make} {self.model}"
		return descriptive_name

	def print_distance(self):
		'''Prints the distance travelled by the car'''
		print(f"Distance travelled is : {self.distance_travelled}") 

	def update_distance(self,new_distance):
		'''Updates the distnace travelled by the car to a value passed as input'''
		self.distance_travelled = new_distance

	def increment_distance(self,kms):
		self.distance_travelled += kms

	def fill_gas_tank(self):
		print("Petrol tank is now full!")

class ElectricCar(Car):
	'''Represents attributes unique to the Electric car'''
	def __init__(self,make,model,year):
		'''Initialize attributes of the parent class'''
		super().__init__(make,model,year)
		self.battery = Battery(battery_size=100)

	def fill_gas_tank(self):
		'''Over ride the Car method as this is not relevant for an Electric car'''
		print("This car does not need a Petrol tank")

class Battery:
	'''A seperate Battery class for an eletric car'''
	def __init__(self,battery_size=75):
		'''Initialize the battery attributes'''
		self.battery_size = battery_size

	def get_battery_size(self):
		'''print the battery size of the Electric Car'''
		print(f"This car has a {self.battery_size} KWh battery")