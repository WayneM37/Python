#Task: Print the prime numbers which are between 1 to entered limit number (n).
def primemi(a):
  if a==2 or a==3: return True
  if a%2 ==0 or a<2: return False
  for i in range(3, int(a**0.5)+1, 2):
    if a%i ==0:
      return False
  return True
n =  int(input("Please enter a number bigger than 1: "))
ans = []
for i in range(2,n+1):
  if primemi(i):
    ans.append(i)
print(ans)
