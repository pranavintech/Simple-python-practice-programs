'''10. Write a program in Python with recursive function
recseries(N) to display the sum of the series S = 1^2 + 2^2 + 3^2 + …….. N2'''

def sumsquareseries(number):
    if(number == 0):
        return 0
    else:
        return (number * number) + sumsquareseries(number - 1)


num = int(input("Please Enter any Positive Number  : "))
total = sumsquareseries(num)

print("The Sum of Series ", total)



