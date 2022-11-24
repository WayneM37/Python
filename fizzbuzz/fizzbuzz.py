#Task : Print the Fizz Buzz numbers.
for i in range(1,100):
  if (i % 3 ==0) and (i%5 ==0):
    print("FizzBuzz")
  elif i % 5 == 0:
    print("Buzz")
  elif i % 3 == 0:
    print("fizz")
  else:
    print(i, end ="\n")

#with list comprehension    
["FizzBuxx" if x%3==0 and x%5==0 else "Fizz" if x%3==0 else "Buzz" if x%5==0 else x for x in range(1,101)]