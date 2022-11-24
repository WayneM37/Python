# Task: Birbirinden farklı iki pozitif integer sayıyı oluşturacağınız fonksiyona yollayın. |
# O da onlardan büyük olanı küçük olandan çıkartsın. Sayılar eşit veya negatif ise tekrar input istesin.

def num_dif(a,b):
  ans=0
  if a>b:
    ans =a-b
  else:
    ans =b-a
  print(ans, "is the difference between the small and the big number")

while True:
  x = input("Please enter a positive, non-decimal number: ")
  y = input("Please enter another positive, non-decimal number: ")
  if (x.isdigit() == False) or (y.isdigit() == False) or (int(x) == (int(y))) or (int(x) == 0) or (int(y) == 0) :
    print("The numbers you entered are invali6d. Please enter two different positive, non-decimal  numbers:")
  else:
    num_dif(int(x),int(y))
    break