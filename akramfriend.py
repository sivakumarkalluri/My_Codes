size,value=map(int,input().split())
array=list(map(int,input().split()))
flag=True
for i in range(size-1):
    for j in range(i+1,size):
        if array[i]+array[j]==value:
            flag=False
            print(i,j)
            break
if flag:
    print(-1)
