'''3. Write a program in Python with recursive function recurreverse(n) to calculate
and return the reverse of a number n passed to the parameter.'''
def reverse(number):
   if number<10:
      return number 
   else:
      return reverse(number//10)
def main():
    number=int(input("Enter a number:"))
    print(number%10,end='')
    print(reverse(number))
main()
