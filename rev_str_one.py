s=raw_input()
a=''
for i in s:
     if i not in a:
          a+=i
print a[::-1]
          
