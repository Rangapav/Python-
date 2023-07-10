# importing the required module
import matplotlib.pyplot as plt
import datetime

# x axis values
x = [1,2,3,4,5,6]
# corresponding y axis values
y = [83,94,91,96,85,92 ]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('x - axis(semesters)')
# naming the y axis
plt.ylabel('y - axis(percentage)')

# giving a title to my graph
plt.title('Degree sem graph!')
plt.style()

# function to show the plot
plt.show()
