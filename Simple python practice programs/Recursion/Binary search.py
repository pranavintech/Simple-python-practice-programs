'''11Write a program in Python with recursive function BinarySearch(Arr, I, R, X)
to search the given element X to be searched from the List Arr having R elements where
I represent the lower bound and R represent the upper bound.'''
L=[]
n=int(input('enter no of elements:'))
for i in range(1,n+1):
            i=int(input('enter element:'))
            L.append(i)
L.sort()
print(L)
d=n//2            
x=int(input('enter item to be searched:'))    
def binarys():
    global x
    global d
    if x==L[d]:
        print('found at index',d)
    elif x>L[d]:
        d+=1
        binarys()
    else:
        d-=1
        binarys()
binarys()        
        
        
        
