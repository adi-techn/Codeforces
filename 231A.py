n=int(input())
cnt=0
while n:
     arr=list(map(int,input().split()))
     
     if sum(arr)>=2:
          cnt+=1
     n-=1
print(cnt)