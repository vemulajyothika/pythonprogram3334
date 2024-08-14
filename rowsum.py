m,n=map(int,input().split())
mat=[]
li=[]
for i in range(m):
    row=list(map(int,input().split()))
    s=sum(row)
    mat.append(row)
    li.append(s)
print(mat)
print(li)
