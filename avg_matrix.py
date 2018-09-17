n=int(input())
s=[]
for i in range(n):
     x=map(int,raw_input().split())
     s.append(x)
l=0
for i in range(len(s)):
     l+=len(s[i])
     s[i]=sum(s[i])
print format(sum(s)/float(l),".6f")
     
