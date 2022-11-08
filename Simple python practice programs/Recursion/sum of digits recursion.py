'''2. Write a program in Python with recursive function recursumdigits(n)
to calculate and return the sum of digits of number n passed to the parameter.'''
number=int(input('enter no:'))
def sumdigits(number):
   
    if number == 0:
        return 0
    else:
        return(number % 10) + sumdigits(number // 10)

print(sumdigits(number))
