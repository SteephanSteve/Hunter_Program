n=map(int,raw_input())
n.insert(0,n.pop())
s=0
p=1
if len(n)==1:
     print n[0]**2
else:
     for i in n:
         s+=i**p
         p+=1  
     print s
