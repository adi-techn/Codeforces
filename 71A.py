t=int(input())

while t>0:
     s=input()
     res=""
     if len(s)>10:
          res+=s[0]
          res+=str(len(s)-2)
          res+=s[-1]
     else:
          res+=s
     
     print(res)
     t-=1