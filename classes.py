# 1. Dog
# class Dog:
# 	'''	A simple attempt to model the dog '''

# 	def __init__(self,name,age):
# 		'''Initialize name and age'''
# 		self.name = name
# 		self.age = age

# 	def sit(self):
# 		'''Simulate a dog sitting'''
# 		print(f"{self.name.title()} is now sitting.")

# 	def roll_over(self):
# 		'''Simulate a dog rolling over'''
# 		print(f"{self.name.title()} rolled over")

# my_dog = Dog("choco",5)
# your_dog = Dog("rocket",8)
# print(f"My dog's name is {my_dog.name.title()}")
# print(f"His age is {my_dog.age}\n")

# my_dog.sit()
# my_dog.roll_over()
# print("\n")
# your_dog.sit()
# your_dog.roll_over()

# 2.Car
# class Car:
# 	'''A simple attempt to represent a car'''
# 	def __init__(self,make,model,year):
# 		'''Initialize attributes of a car'''
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.distance_travelled = 0

# 	def get_descriptive_name(self):
# 		'''Gets the name in the format <Year> <Make> <Model> '''
# 		descriptive_name = f"{self.year} {self.make} {self.model}"
# 		return descriptive_name

# 	def print_distance(self):
# 		'''Prints the distance travelled by the car'''
# 		print(f"Distance travelled is : {self.distance_travelled}") 

# 	def update_distance(self,new_distance):
# 		'''Updates the distnace travelled by the car to a value passed as input'''
# 		self.distance_travelled = new_distance

# 	def increment_distance(self,kms):
# 		self.distance_travelled += kms

# my_car = Car("Kia","Carens","2022")
# print(my_car.get_descriptive_name())
# my_car.print_distance()
# # Update the distance using the update_distance() method
# my_car.update_distance(50_000)
# my_car.print_distance()
# # Increment the distance travelled by 1000
# my_car.increment_distance(1000)
# my_car.print_distance()

# 3.Electric Car
# class Car:
# 	'''A simple attempt to represent a car'''
# 	def __init__(self,make,model,year):
# 		'''Initialize attributes of a car'''
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.distance_travelled = 0

# 	def get_descriptive_name(self):
# 		'''Gets the name in the format <Year> <Make> <Model> '''
# 		descriptive_name = f"{self.year} {self.make} {self.model}"
# 		return descriptive_name

# 	def print_distance(self):
# 		'''Prints the distance travelled by the car'''
# 		print(f"Distance travelled is : {self.distance_travelled}") 

# 	def update_distance(self,new_distance):
# 		'''Updates the distnace travelled by the car to a value passed as input'''
# 		self.distance_travelled = new_distance

# 	def increment_distance(self,kms):
# 		self.distance_travelled += kms

# 	def fill_gas_tank(self):
# 		print("Petrol tank is now full!")

# class ElectricCar(Car):
# 	'''Represents attributes unique to the Electric car'''
# 	def __init__(self,make,model,year):
# 		'''Initialize attributes of the parent class'''
# 		super().__init__(make,model,year)
# 		self.battery = Battery(battery_size=100)

# 	def fill_gas_tank(self):
# 		'''Over ride the Car method as this is not relevant for an Electric car'''
# 		print("This car does not need a Petrol tank")

# class Battery:
# 	'''A seperate Battery class for an eletric car'''
# 	def __init__(self,battery_size=75):
# 		'''Initialize the battery attributes'''
# 		self.battery_size = battery_size

# 	def get_battery_size(self):
# 		'''print the battery size of the Electric Car'''
# 		print(f"This car has a {self.battery_size} KWh battery")

# my_car = ElectricCar("tesla","model s","2019")
# print(my_car.get_descriptive_name())
# my_car.battery.get_battery_size()


# 4. Importing a car
# from car import Car

# my_car = Car("Kia","Carens","2022")
# print(my_car.get_descriptive_name())

# 5. Storing Multiple classes in same module:
# from car import ElectricCar
# my_car = ElectricCar("Tesla","Model S","2002")
# my_car.fill_gas_tank()
# print(my_car.get_descriptive_name())

# 6. Importing multiple classes from a module
# from car import Car,ElectricCar,Battery
# my_normal_car = Car("Kia","Carens","2022")
# my_ev_car = ElectricCar("Tesla","Model S","2022")

# print(my_normal_car.get_descriptive_name())
# print(my_ev_car.get_descriptive_name())

# 7. Importing an entire module
import car 
my_car = car.Car("Kia","Carens","2022")
print(my_car.get_descriptive_name())
my_ev_car = car.ElectricCar("Tesla","Model S","2022")
print(my_ev_car.get_descriptive_name())