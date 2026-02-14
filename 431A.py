c=list(map(int,input().split()))
s=input()

cal=0
for ch in s:
     cal+=c[int(ch)-1]

print(cal)