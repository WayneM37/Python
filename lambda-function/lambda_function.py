# lambda function with if-else condition
list_1= [1, 2, 3, 4, 5, 6, 7]
for i in list_1:
  print(i,":", (lambda x: "odd" if x % 2 !=0 else "even")(i))

# lambda function with map function
listem =[1, 2, 3, 4, 5, 6]
def kare(x):
  return x**2
list(map(kare,listem))

# lambda function with map function 
def myfunc(a, b):
  return a + b
x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))

# lambda function with map() function
number_list = [1, 2, 3, 4, 5]
result =list(map(lambda x: x*3, number_list))
print(result)


#lambda function with filter() function
vowel = ['a', 'e', 'i', 'o', 'u', "ü", "ö", "ı"]
cümle = "yok ya daha neler, olmaz öyle şey"

answ = list(set(filter(lambda x: True if x in vowel else False, cümle)))
print("cümle içerisindeki sesli harfler: ", answ)