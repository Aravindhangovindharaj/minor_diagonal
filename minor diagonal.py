a=int(input())
b=int(input())
mat=[]
for i in range(a):
    d=[]
    for j in range(b):
        d.append(int(input()))
    mat.append(d)
i=0
j=b-1
sum=0
while i<a and j>=0:
    sum+=mat[i][j]
    i=i+1
    j=j-1
print(sum) 
