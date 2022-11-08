'''5. Write a program in Python with recursive
function recurfibo(n) to computer the nth Fibonacci number.'''
def recurfibo(n):
   if n <= 1:
       return n
   else:
       return(recurfibo(n-1) + recurfibo(n-2))

terms = int(input('enter no:.'))


if terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(terms):
       print(recurfibo(i))
