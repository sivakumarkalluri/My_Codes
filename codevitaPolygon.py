n=int(input())
x=[]
y=[]
for i in range(n):
    a=list(map(int,input().split()))
    x.append(a[0])
    y.append(a[1])
print(max(x)*max(y))
