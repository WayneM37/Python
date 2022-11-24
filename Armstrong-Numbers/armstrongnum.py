#Armstrong numbers
n = "" 
ans = []
while n.isdigit() == False:
    n = input("Write a positive,  non-decimal  number: ")
if n.isdigit() == True:
    for i in n:
        ans.append(int(i)**len(n))
    if sum(ans) == int(n):
        print(n,"is an Armstrong number")
    else:
        print(n, "is not an Armstrong number") 
else:
    print("It is an invalid entry. Don't use non-numeric, float,\
  or negative values!, Please try again")