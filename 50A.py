r,c=map(int,input().split())
d=0

d+=(r//2*c)
if r%2==1:
     d+=(c//2)

print(d)