''''4. Write a program in Python with recursive
function recursum(L) to calculate and return the
sum of all the elements in a list.'''
L=[]
N=int(input("enter list size: "))
for i in range(0,N):
   n=int(input('enter the list elements: '))
   L.append(n)
def getSum(L):
    if len(L)==0:
        return 0
    else:
        return L[0] + getSum(L[1:]) 
print (getSum(L))
