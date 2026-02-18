t=int(input())

while t:
     n=int(input())
     a=list(map(int,input().split()))

     cnt=0
     neg=a.count(-1)
     pos=n-neg

     if neg>pos:
          need=(neg-pos+1)//2
          cnt+=need
          neg-=need
          pos+=need

     if neg%2!=0:
          cnt+=1
     
     print(cnt)
     t-=1