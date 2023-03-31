# ARRAYS IS USED TO STORE DATA IN THE SPECIFIED MEMORY LOCATION
# ARRAY IS LIKE A LIST BUT ARRAY IS HOMOGENEOUS

import array as arr

p=arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8])
# print(p)
#

x=arr.array('d',[1,2,3,4,5.6,7.8,9.7])
print(x)
x.reverse()
print(x.tolist())
print(type(x))
x.byteswap()
print(x)