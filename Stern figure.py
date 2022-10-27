n=(int)(input())
for i in range (n):
    for k in range(i):
        print(' ', end =' ')
    for k in range(n):
        if k<n-1:
            print('*', end ='')
        else:
            print('*')
