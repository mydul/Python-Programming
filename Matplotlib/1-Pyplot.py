"""Matplotlib is a low level graph plotting library in python that serves as a visualization utility."""
"""matplotlib.pyplot is a collection of functions that make matplotlib work like MATLAB."""
"""Each pyplot function makes some change to a figure: e.g., creates a figure,
creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc."""

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
plt.xlabel("Voltage")
plt.ylabel("Current")
plt.show()



""" How to iinstall matplotlib
Step 1. Find the python file path.
Step 2: CMD > Command Prompt
Step 3: cd [python file path] like my case cd C:\Program Files\Python310
Step 4: Then those-
python -m pip install -U pip
python -m pip install matplotlib

py -m pip install --upgrade pip
py -m pip --version