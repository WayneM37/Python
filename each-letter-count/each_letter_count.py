# Count the number of each letter in a sentence.
get_1 = input("Write a sentence to see how many words it has: ")
ans = {}
for i in get_1:
  ans[i] = get_1.count(i)
print(ans)