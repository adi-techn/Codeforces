t=int(input())
 
while t:
     n=int(input())
     s=input()
     m=int(input())
     l=input()
     c=input()

     for i in range(m):
          ch=c[i]
          if ch=='V':
               s=l[i]+s
          else:
               s+=l[i]
     
     print(s)
     t-=1


