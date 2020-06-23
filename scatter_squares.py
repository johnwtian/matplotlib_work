import matplotlib.pyplot as plt 

plt.scatter(2,4, s=200)

x_values = [1,2,3,4,5]
y_values = [1,4,9,19,25]
plt.scatter(x_values, y_values, s=100)

x_values_2 = list(range(1,1001))
y_values_2 = [x**2 for x in x_values_2]
plt.scatter(x_values_2, y_values_2, c='red',0edgecolor= 'none', s=40)

# Set chart title and label axes
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# Set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
plt.axis([0, 1100, 0, 1100000])
plt.show()