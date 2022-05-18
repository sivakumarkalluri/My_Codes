size=int(input())
array=list(map(int,input().split()))
k=int(input())
count=0
for i in array:
    if k%i==0:
        count+=1
print(count)