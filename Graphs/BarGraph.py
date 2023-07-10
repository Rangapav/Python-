import matplotlib.pyplot as p
import datetime

x = [1,2,3,4,5,6]
# corresponding y axis values
y = [83,94,91,96,85,92 ]

tick_label=['one','two','three','four','five','six']
p.bar(x,y,tick_label=tick_label,width=0.8,color=['red','yellow','green','blue','orange','violet'])
p.xlabel('Semester')
p.ylabel('Percentage')
# p.title('Pavan Degree results',x)
# x=datetime.datetime.now()
p.title('Pavan Degree results')
# p._auto_draw_if_interactive('graph',5)
p.show()