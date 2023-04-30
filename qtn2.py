input1=input("Enter the string: ")
str=input1.lower()
l=[]
for c in str:
    if c in l:
        continue
    l.append(c)
print("uniqueLetters = ",end="")
for i in l:
    print(i,end=",")