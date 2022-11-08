a=int(input('enter taxable income='))
if a<=300000:
    b=0
elif a<=500000:
    b=0+ 0.05*(a-300000)
elif a<=1000000:
    b=0 +200000*0.05 + (a-500000)*0.20
else:
    b= a +200000*0.05 + 500000*0.20 + (a-1000000)*0.30
c=0.03*b
d= b + c
print('income tax=',b)
print('educational cease=',c)
print('total tax=',d)
