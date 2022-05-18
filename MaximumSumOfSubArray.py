array=list(map(int,input().split()))
l=[]
for i in range(len(array)-1):
    sum=0
    for j in range(i+1,len(array)+1):
        sum+=array[j-1]      
        l.append(sum)
print(max(l))