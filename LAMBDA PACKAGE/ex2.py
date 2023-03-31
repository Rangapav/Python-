import functools
num=[1,2,3,4,5,6,7,8,9,10]
print(functools.reduce(lambda x,y:x*y,num))

# def reduce(num):
#    return x*y
# p=functools.reduce(num)
# print(p)

# import functools
#
# # initializing list
# lis = [1, 3, 5, 6, 2]
#
# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: a + b, lis))
#
# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))

