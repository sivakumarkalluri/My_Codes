size=int(input())
array=[]
for i in range(size):
    array.append(int(input()))
c=int(input())
total=0
count=0
i=0
while i<size-1:
    j=i+1
    total=0
    while j<size:
        total+=array[j-1]
        if total<=c:
            i=i+1
            j=j+1
            pass
        else:
            count+=1
print(count)




