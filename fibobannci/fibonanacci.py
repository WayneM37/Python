# Create a list consisting of Fibonacci numbers from 1 to 55 using control flow statements and range() function.
j = [0, 1]
[ j := j + [(j[i]+ j[i+1])] for i in range(0,8)]
print(j)