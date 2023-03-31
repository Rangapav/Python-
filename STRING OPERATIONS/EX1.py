print("1.adding strings")
print("2.uppercase")
print("3.lowercase")
print("4.find")
print("5.replace")
operation=int(input("ENTER ANY STRING="))
if operation==1:
    str1=input("ENTER ANY STRING1=")
    str2=input("ENTER ANY STRING2=")
    print(str1+str2)
elif operation==2:
    str1 = input("ENTER ANY STRING1=")
    str2 = input("ENTER ANY STRING2=")
    s1=str1.upper()
    s2=str2.upper()
    print (s1 + s2)
elif operation==3:
    str1 = input("ENTER ANY STRING1=")
    str2 = input("ENTER ANY STRING2=")
    s1=str1.lower()
    s2=str2.lower()
    print (s1 + s2)
elif operation==4:
    str1 = input("ENTER ANY STRING1=")
    str2 = input("ENTER ANY STRING2=")
    s1=str1.find(str2)
    print ("str2 is find in str1 find at position=", s1)
elif operation==5:
    str1 = input("ENTER ANY STRING1=")
    str2 = input("ENTER ANY STRING2=")
    s1=str1.replace(str1,str2)
    print (s1)
elif operation==6:
    str1 =input("ENTER ANY STRING1=")
    str2 = input("ENTER ANY STRING2=")
    s1=str1.count(str1)
    s2=str2.count(str2)
    print ("No of elements in str1=", s1)
    print("No of elements in str2=", s2)


