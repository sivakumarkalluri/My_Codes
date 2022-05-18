size=int(input())
array=[]
output=[]
for i in range(size):
    array.append(int(input()))
if size==1:
    print(array[0])
else:
    for i in range(size-1):
        maximum=array[i]
        for j in range(i+1,size):
            
            if array[j]>array[j-1]:
                maximum+=array[j]
            else:
                break
        output.append(maximum)
    print(max(output))