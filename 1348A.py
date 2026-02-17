t=int(input())

while t:
     n=int(input())

     pow=[]
     for i in range(1,n+1):
          pow.append(2**i)
     
     a=b=0
     for i in range(n//2-1):
          a+=pow.pop(0)
     a+=pow.pop()
     b=sum(pow)
     print(abs(a-b))
     t-=1

