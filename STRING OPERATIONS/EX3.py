pun="'';:<>,./?-""_*&??^^%43@![]{}\|"
str=input("ENTER ANY STRING=")
no_punc=""
for char in str:
    if char not in pun:
        no_punc=no_punc+char
print(no_punc)