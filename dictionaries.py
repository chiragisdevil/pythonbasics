# alien_0 = {'color':'green','points':5}
# print(alien_0['color'])
# print(alien_0['points'])

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# print(alien_0)

# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)
# alien_0['color'] = 'yellow'
# print(alien_0)

# alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
# print(f"Original position is {alien_0['x_position']}")

# if (alien_0['speed'] == 'slow'):
# 	x_increment = 1
# elif (alien_0['speed'] == 'medium'):
# 	x_increment = 2
# else:
# 	x_increment = 3

# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position is {alien_0['x_position']}")

# alien_0 = {'color':'green','points':5}
# del alien_0['points']
# print(alien_0)

# favorite_language = {
# 	"chirag":"python",
# 	"tapsi":"java",
# 	"aradhya":"c",
# 	"amyra":"go",
# }

# print(f"Chirag's favorite language is {favorite_language['chirag'].title()}")

alien_0 = {'color':'green','points':5}
points = alien_0.get('points','Sorry the value could not be found in dictionary')
print(points)
del alien_0['points']
points = alien_0.get('points','Sorry the value could not be found in dictionary')
print(points)
