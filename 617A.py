d=int(input())
cnt=0

if d>=5:
     cnt+=(d//5)
     d%=5
if d>0 and d<5:
     cnt+=1
print(cnt)