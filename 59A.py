s=input()

islow=isup=0
for c in s:
     if c.islower():
          islow+=1
     else:
          isup+=1

if islow<isup:
     s=s.upper()
else:
     s=s.lower()

print(s)