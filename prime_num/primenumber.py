# takes a number from the user and prints the result to check if it is a prime number.
def primemi(a):
  if a==2 or a==3: return True
  if a%2 ==0 or a<2: return False
  for i in range(3, int(a**0.5)+1, 2):
    if a%i ==0:
      return False
  return True
get_1= int(input("Please enter a number: "))
if primemi(get_1) == True:
  print(get_1,"is a prime number")
else:
  print(get_1, "is not a prime number")