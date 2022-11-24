# Get two nun-digit, nun-equal, positive integer from user and Subtract the larger number from the smaller one.
def num_dif(a,b):
  ans=0
  if a>b:
    ans =b-a
  else:
    ans =a-b
  print(ans, "is the difference between the small and the big number")

while True:
  x = input("Please enter a positive, non-decimal number: ")
  y = input("Please enter another positive, non-decimal number: ")
  if (x.isdigit() == False) or (y.isdigit() == False) or (int(x) == (int(y))) or (int(x) == 0) or (int(y) == 0) :
    print("The numbers you entered are invali6d. Please enter two different positive, non-decimal  numbers:")
  else:
    num_dif(int(x),int(y))
  break