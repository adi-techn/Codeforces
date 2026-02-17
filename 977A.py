n,k=map(int,input().split())

for i in range(k):
     r=n%10
     if r==0:
          n//=10
     else:
          n-=1

print(n)