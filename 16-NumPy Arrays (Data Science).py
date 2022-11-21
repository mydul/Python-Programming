#..........NumPy Arrays (Data Science)..........
print("..........NumPy Arrays (Data Science)..........")
"""NumPy is multi-dimensional arrays which is a great alternatives to Python Lists. Some of the key advantages of NumPy-
they are fast, easy to work with, and give users the opportunity to perform calculations across entire arrays."""

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 76.18, 100.45]

# Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

# Calculate bmi
bmi = np_weight / np_height ** 2
print(bmi)

# Print only those observations above 23
print(bmi[bmi > 23])


#..........NumPy Arrays (Data Science) Exercise..........
print("..........NumPy Arrays (Data Science) Exercise..........")
"""First, convert the list of weights from a list to a Numpy array. Then, convert all of the weights from kilograms to pounds.
Use the scalar conversion of 2.2 lbs per kilogram to make your conversion. Lastly, print the resulting array of weights in pounds."""

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2

# Print out np_weight_lbs
print(np_weight_lbs)

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


""" How to iinstall NumPy
Step 1. Find the python file path.
Step 2: CMD > Command Prompt
Step 3: cd [python file path] like my case cd C:\Program Files\Python310
Step 4: Then those-
python -m pip install -U pip
python -m pip install numpy

py -m pip install --upgrade pip
py -m pip --version
"""
