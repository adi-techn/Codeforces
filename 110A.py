n=int(input())

cnt=0
while n:
     r=n%10
     if r==4 or r==7:
          cnt+=1
     n//=10

if cnt==4 or cnt==7:
     print("YES")
else:
     print("NO")
