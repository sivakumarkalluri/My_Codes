size=int(input())
array=list(map(int,input().split()))
output=[]
for i in array:
    sum=0
    for j in str(i):
        sum+=int(j)
    output.append(sum)
for i in output:
    print(i,end=" ")