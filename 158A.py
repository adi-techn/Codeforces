n,k=map(int,input().split())
arr=list(map(int,input().split()))
score=arr[k-1]
c=0
for x in arr:
     if x>=score and x>0:
          c+=1
print(c)