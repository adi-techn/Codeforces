mat=[]
for i in range(5):
     mat.append(list(map(int,input().split())))

r=c=0
for i in range(5):
     for j in range(5):
          if mat[i][j]==1:
               r=i+1
               c=j+1

print(abs(3-r)+abs(3-c))