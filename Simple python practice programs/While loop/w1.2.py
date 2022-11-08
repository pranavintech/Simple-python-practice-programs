import math 
def sumOfSeries(n): 
  
    sum = 0
    for i in range(1,n+2): 
        sum = sum + (3 * i - 1) * (3 * i - 1) 
    return sum
       
n= int(input('enter='))
print(sumOfSeries(n)) 
  
