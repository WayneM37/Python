# Ask the user to enter the numbers a and b. If the numbers are equal, print "these numbers are equal".\
# Print "you entered negative" if one of the numbers is negative. \
# Otherwise; if a is greater than b the result a-b; If b is greater than a, return the result b-a.
# "\" was used for Pep8 purposes.

 
a = int(input("Entger a number: "))
b = int(input("Enter another number: "))
print("Thease numbers are equal" if a==b else "you entered a negative number" \
      if (a < 0) or (b < 0) else (a-b) if a >b else (b-a))