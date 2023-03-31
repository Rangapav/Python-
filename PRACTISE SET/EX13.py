def fact(ch):
    if ch==65:
        return 1
    else:
        return ch*fact(ch-1)
ch=90
x=fact(ch)
print(x)