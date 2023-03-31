# 3)READ MODE---->'r'

# a=open('file1.txt','r')
# x=a.read()
# print(x)

# 4)append mode---->'a'

# s=open('file1.txt','a')
# p=s.write('\n'"He completed his graduation in the year 2022\n Now he was doing a Full stack python developer course")
# print(p)

a=open('file1.txt','r')
x=a.readline()
print(x,end='')
y=a.readline()
print(y)