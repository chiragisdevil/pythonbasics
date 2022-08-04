# # 4-3 Counting to Twenty

# for num in range(1,21):
# 	print(num)

# # 4-4 One Million

# for num in range(1,1000001):
# 	print(num)

# 4-5 Summing a Million
# million = list(range(1,1000001))
# print(min(million))
# print(max(million))

# sum = 0
# for val in million:
# 	sum = sum + val

# print(f"The sum is: {sum}")

# 4-6 Odd Numbers
# odd_numbers = list(range(1,20,2))
# for odd_number in odd_numbers:
# 	print(odd_number)

# 4-7 Threes

# threes = list(range(3,31,3))
# for three in threes:
# 	print(three)

# 4-8 cubes
# cube = []
# numbers = list(range(1,11))
# for number in numbers:
# 	cube.append(number**3)

# print(cube)

# 4-9 cubes with comprehension
cube = [value**3 for value in range(1,11)]
print(cube)


