#..........Pandas DataFrames (Data Science)..........
print("..........Pandas DataFrames (Data Science)..........")
"""Pandas is a high-level data manipulation tool. It is built on Numpy package and its key data structure is called the DataFrame.
DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables."""

#There are several ways to create a DataFrame. One way way is to use a dictionary. 
dictionary = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dictionary)
print(brics)

# Set the index for brics
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)


# We can import data from a .csv file:
cost_for_living = pd.read_csv('cost.csv', index_col = 0)
print(cost_for_living)

"""There are several ways to index a Pandas DataFrame. One of the easiest ways to do this is by using square bracket notation."""
"""The single bracket will output a Pandas Series, while a double bracket will output a Pandas DataFrame."""

# Print out Category column as Pandas Series
print(cost_for_living['Category'])
# Print out Category column as Pandas DataFrame
print(cost_for_living[['Category']])

#Square brackets can also be used to access observations (rows) from a DataFrame.
# Print out first 4 observations
print(cost_for_living[0:4])

"""Use loc and iloc to perform just about any data selection operation.
loc is label-based, which means that you have to specify rows and columns based on their row and column labels.
iloc is integer index based"""

# Print out observations for Flixbus and Blanket
print(cost_for_living.loc[['Flixbus', 'Blanket']])

# Print out observation for Chicken Burger
print(cost_for_living.iloc[2])



""" How to iinstall pandas
Step 1. Find the python file path.
Step 2: CMD > Command Prompt
Step 3: cd [python file path] like my case cd C:\Program Files\Python310
Step 4: Then those-
python -m pip install -U pip
python -m pip install pandas

py -m pip install --upgrade pip
py -m pip --version
"""