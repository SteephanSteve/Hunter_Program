a=list(raw_input())
b=list(raw_input())
while a or b:
     if not a:
          s=b.pop(0)
     elif not b:
          s=a.pop(0)
     else:
          s=b.pop(0)+a.pop(0)
     print s
