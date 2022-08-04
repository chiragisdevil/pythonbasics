### Adding items to a list using append method

# motor_cycles = []

# motor_cycles.append('honda')
# motor_cycles.append('yamaha')
# motor_cycles.append('suzuki')

# print(motor_cycles)

### Inserting Elements into specific positions

# motor_cycles = ['honda', 'yamaha', 'suzuki']
# motor_cycles.insert(0,'ducati')
# print(motor_cycles)

### Removing Element using del statement (not method)
# motor_cycles = ['honda', 'yamaha', 'suzuki']
# del motor_cycles[2]
# print(motor_cycles)

### Removing Element using pop() method4
# motor_cycles = ['honda', 'yamaha', 'suzuki']
# favorite_bike = motor_cycles.pop()
# print(motor_cycles)
# print(favorite_bike)

### Removing Element in specific positions using pop() method 
# motor_cycles = ['honda', 'yamaha', 'suzuki']
# favorite_bike = motor_cycles.pop(1)
# print(motor_cycles)
# print(favorite_bike)

### Removing Element using value with remove() method 
too_expensive = 'ducati'
motor_cycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motor_cycles.remove(too_expensive)
print(motor_cycles)
print(f"A {too_expensive} is too expensive for me!")

