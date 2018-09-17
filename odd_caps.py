s=list(raw_input())
x=[]
for i in s:
     if not i==' ':
        x.append(i)
for i in range(len(x)):
     if i%2==0:
          x[i]=x[i].upper()          
for i in range(len(s)):
     if s[i]==' ':
          x.insert(i,' ')
print ''.join(x)
