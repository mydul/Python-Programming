"""Matplotlib is a low level graph plotting library in python that serves as a visualization utility."""
"""matplotlib.pyplot is a collection of functions that make matplotlib work like MATLAB."""
"""Each pyplot function makes some change to a figure: e.g., creates a figure,
creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc."""

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 2, 3, 4])
plt.xlabel("Voltage")
plt.ylabel("Current")
plt.show()

