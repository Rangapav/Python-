l=[-1,-2,-3,-4,-5,0,1,2,3,4,5]

# for i in l:
#     if i<=0:
#      print(i)

for i in range(len(l)):
    if l[i]<=0:
        l[i]="pavan"
print(l)