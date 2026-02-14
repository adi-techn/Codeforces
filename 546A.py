k,n,w=map(int,input().split())
amt=0
for i in range(1,w+1):
     amt+=(i*k)

print(0 if amt<=n else (amt-n))