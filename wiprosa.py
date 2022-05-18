size=input()
array=list(map(int,input().split()))
k=int(input())
maximum=0
output=[]
for i in range(len(array)-1):
   
    sum=0
    count=0
    for j in range(i+1,len(array)):
        if count<k:
            sum+=array[j-1]
            count+=1
    if sum>maximum:
        maximum=sum
        output=[]
        for p in range(k):
            output.append(array[i+p])
print(output)