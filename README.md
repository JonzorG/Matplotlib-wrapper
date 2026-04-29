# Matplotlib SplitPlot

A lightweight Python library to solve a common Matplotlib issue: splitting a single line plot into different colors when it crosses a specific threshold (like y=0).

Because Matplotlib draws point-to-point, lines crossing a threshold can't change colors midway. This library uses linear interpolation to calculate the exact crossing point and injects a new data coordinate, allowing for a seamless, multi-colored line.

## Installation

```bash
pip install matplotlib-splitplot

from splitplot import plot_split_color

# Your data
x_data = [1, 2, 3, 4, 5]
y_data = [-5, -2, 4, 8, -1]

fig, ax = plt.subplots()

# Plot the line with a split color at y=0
plot_split_color(ax, x_data, y_data, threshold=0, color_above='green', color_below='red')

plt.axhline(0, color='black', linestyle='--')
plt.show()
