s1=input().lower()
s2=input().lower()
s=0

for i in range(len(s1)):
     if ord(s1[i])<ord(s2[i]):
          s=-1
          break
     elif ord(s1[i])>ord(s2[i]):
          s=1
          break
print(s)
     