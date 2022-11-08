a=int(input('enter='))
ra=0
while a!=0:
    digit=a%10
    ra=ra*10 + digit
    a//=10
    print('revers=',ra)
