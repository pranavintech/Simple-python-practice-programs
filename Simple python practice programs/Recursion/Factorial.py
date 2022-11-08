#1. Write a program in Python with recursive function
#recurfactorial(n) to calculate and return the factorial of number n passed to the parameter.

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = int(input('enter no whose factorial is to be printed:'))

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
