size=int(input())
array=[]
count=0
for i in range(size):
    array.append(int(input()))
for i in range(len(array)-1):
    for j in range(i+1,len(array)):
        if array[i]==0 and array[j]==1:
            count+=1
print(count)