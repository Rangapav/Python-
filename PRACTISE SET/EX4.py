l=[1,2,3,4,1,2,3,10,9]
# print(type(l))
# print(l.count(4))
# print(l.copy())
# print(l.reverse())
# print(l.insert(1,4))
# print(l.pop())
l.sort()
print(l)
l.sort(reverse=True)
print(l)
for i in range(len(l)):
    if l[i]>=5:
        l[i]="pavan"
print(l)
