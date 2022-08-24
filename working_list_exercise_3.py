# 4-10 Slices
# threes = list(range(3,16,3))
# for three in threes:
# 	print(three)

# print("\nThe first three items in the list are:")
# print(threes[:3])

# print("\n Three items from the middle are:")
# print(threes[1:-1])

# print("\n The last 3 items in the list are:")
# print(threes[-3:])

# 4-11 My Pizzas, Your Pizzas
# pizzas = ["paneer","veggie delight", "farmhouse"]
# for pizza in pizzas:
# 	print(f"I like {pizza} pizza")
# print("I love pizzas for their cheese") 
# print("Specially the cheese burst pizza")
# print("They are also easily edible")

# friends_pizzas = pizzas[:]
# pizzas.append("cheese")
# friends_pizzas.append("mexican greenwave")

# print("\nMy favorite Pizzas are:")
# for pizza in pizzas:
# 	print(pizza)

# print("\nMy friend's favorite pizzas are:")
# for friends_pizza in friends_pizzas:
# 	print(friends_pizza)

# 4-12 More Loops
my_foods = ["Pizza","Paneer","Pasta"]
wife_foods = my_foods[:]
print(my_foods)
print(wife_foods)
my_foods.append("Kheer")
wife_foods.append("Gheeya")

print("\nMy favorite foods are:")
for my_food in my_foods:
	print(my_food)

print("\nMy wife's favorite foods are:")
for wife_food in wife_foods:
	print(wife_food)