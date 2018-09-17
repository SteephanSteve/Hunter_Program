n=int(input())
a=map(int,raw_input().split(' '))
for i in range(n):
    if i<n-1:
       if a[i]>a[i+1]:
           print a[i+1],
       else:
           print '-1',
    elif i==n-1:
        if a[i]>a[0]:
            print a[0],
        else:
            print '-1',
