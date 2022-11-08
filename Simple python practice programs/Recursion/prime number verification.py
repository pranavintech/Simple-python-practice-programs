'''9. Write a program in Python with recursive function
isprime(n) to display whether it is a prime number or not.'''
num=int(input('enter no'))
def prime(num):
    
        if num > 1:
           
           for i in range(2,num):
               if (num % i) == 0:
                   print(num,"is not a prime number")
                   print(i,"times",num//i,"is",num)
                   break
           else:
               print(num,"is a prime number")

        else:
           print(num,"is not a prime number")
prime(num)
