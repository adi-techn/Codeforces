s=input()
st=""
for i in range(len(s)):
     if i==0:
          st+=s[i].upper()
     else:
          st+=s[i]

print(st)