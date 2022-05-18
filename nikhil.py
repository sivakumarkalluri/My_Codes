input1=int(input())
input2=list(map(int,input().split()))
array=[]
for i in range(input1):
    total=sum(input2[:i+1])
    array.append(total)
print(min(array))