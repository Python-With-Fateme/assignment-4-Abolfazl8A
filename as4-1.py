n=int(input('add:'))
if n<0:
    print("eror")
else:
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
        print('the factorial of {} is : {}'.format(n,factorial))
