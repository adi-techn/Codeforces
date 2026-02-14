n=int(input())
s=input().lower()

hs=set()
for c in s:
     hs.add(c)

if len(hs)==26:
     print("YES")
else:
     print("NO")