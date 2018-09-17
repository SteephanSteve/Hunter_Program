s=raw_input()
d={}
for i in s:
     if i not in d:
          d[i]=0
for i in s:
     d[i]+=1
print max(d,key=d.get),d[max(d,key=d.get)]
