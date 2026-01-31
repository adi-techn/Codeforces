l,b=map(int,input().split())
cnt=0
while l<=b:
     l*=3
     b*=2
     cnt+=1
print(cnt)
