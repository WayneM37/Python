# In a given text you need to sum the numbers while excluding any digits that form part of a word.

sum_numbers = ('This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year')
tak = sum_numbers.split(" ")
say = 0
[say := say + int(i) for i in tak if i.isdigit()]
print(say)