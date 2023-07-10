import matplotlib.pyplot as p

semester=['1st sem','2nd sem','3rd sem','4th sem','5th sem','6th sem']

x=[5,6,7,4,3,2]
colors=['r','y','g','b','g','r']

p.pie(x,labels=semester,colors=colors,startangle=90, shadow = True, explode = (0, 0, 0.1, 0,0,0.1),
        radius = 1.2, autopct = '%1.1f%%')
p.legend()
p.show()