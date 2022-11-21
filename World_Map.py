""" To iinstall pygal
Step 1. Find the python file path.
Step 2: CMD > Command Prompt
Step 3: cd [python file path] like cd C:\Program Files\Python310
Step 4: Then those-
python -m pip install -U pip
python -m pip install pygame
python -m pip install pygal
"""

# import pygal library
import pygal

# create a world map
worldmap = pygal.maps.world.World()

# set the title of the map
worldmap.title = 'Countries'

# adding the countries
worldmap.add('Random Data', {
    'aq' : 10,
    'cd' : 30,
    'hk' : 23,
    'in' : 70,
    'ip' : 54,
    'nz' : 41,
    'kz' : 32,
    'us' : 66
})

# save into the file
worldmap.render_to_file('abc.svg')

print("Success")