import matplotlib.pyplot as p

x = [1,2,3,4,5,6]
# corresponding y axis values
y = [83,94,91,96,85,92 ]

p.plot(x,y, color='red',linestyle='dashed',linewidth='3',marker='o', markerfacecolor='blue', markersize=12)

p.xlabel('Semester')
p.ylabel('Percentage')

p.title('Pavan Degree results')

p.show()