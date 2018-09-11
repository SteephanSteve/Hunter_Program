n=map(int,raw_input())
s=0
for _ in range(len(n)):
     s+=sum(n)
     n.pop()
print s
