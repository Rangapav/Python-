print("welcome to the world of cricket")
n=input("enter your name:")
if n=="pavan":
    print("Login succesfully")
    l1=int(input("enter any value="))
    if l1==1:
        print("1ST LEVEWL COMPLETED")
        l2 = int(input("enter any value="))
        if l2 == 2:
            print("2ND LEVEWL COMPLETED")
            l3=int(input("enter any value="))
            if l3==3:
               print("3RD LEVEWL COMPLETED")
               l4 = int(input("enter any value="))
               if l4 == 4:
                  print("4TH LEVEWL COMPLETED")
                  l5 = int(input("enter any value="))
                  if l5 == 5:
                     print("5TH LEVEWL COMPLETED")
                  else:
                     print("5th level unsuccess")
               else:
                 print("4th level unsuccess")
            else:
                print("3rd level unsuccess")
        else:
           print("2d level unsuccess")
    else:
        print("1st level unsuccess")
else:
    print("login unsuccess")