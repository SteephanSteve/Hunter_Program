s=raw_input().split(' ')
for i in range(len(s)):
     if i%2==0:
          print s[i][::-1],
     else:
          print s[i],
     
