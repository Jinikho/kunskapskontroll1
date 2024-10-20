import numpy as np
import matplotlib.pyplot as plt

#1. Object-Oriented (OO) Approach:Involves explicitly creating figure and axes objects 
# and calling methods on these objects. Example: fig, ax = plt.subplots().

# Pyplot (Stateful) Approach: This method is easier for simple plots, using the 
# pyplot interface directly (e.g., plt.plot()).

# The object-oriented approach is generally recommended, especially for more complex 
# plots, as it provides more control and flexibility.

#2. Figure is the entire plotting areathat holds all elements, such as plots, labels, and axes.
# Axes is the area on which data is plotted (i.e., a single graph or chart). 
# Axis refers to the horizontal (x-axis) or vertical (y-axis) lines in a plot that represent data coordinates. 
# Artist is any object that can be drawn on a figure, such as a line, text, or rectangle.

#3. The most common input data types for plotting in Matplotlib are lists, NumPy arrays,
# or Pandas Series/DataFrames. These formats represent numerical data.

#4. OO Approach:
x = np.linspace(-4, 4, 100)
y = x ** 2

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('y = x^2')
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

# Pyplot Approach:
plt.plot(x, y)
plt.title('y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


#5.

# Data for scatter plot
np.random.seed(15)
random_data_x = np.random.randn(1000)
random_data_y = np.random.randn(1000)

# Data for bar plot
fruit_data = {'grapes': 22, 'apple': 8, 'orange': 15, 'lemon': 20, 'lime': 25}
names = list(fruit_data.keys())
values = list(fruit_data.values())

# 
# subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Scatter plot
ax1.scatter(random_data_x, random_data_y)
ax1.set_title('Scatter Plot')
ax1.set_xlabel('Random X')
ax1.set_ylabel('Random Y')

# Bar plot
ax2.bar(names, values)
ax2.set_title('Fruit Count')
ax2.set_xlabel('Fruit')
ax2.set_ylabel('Count')

plt.tight_layout()
plt.show()