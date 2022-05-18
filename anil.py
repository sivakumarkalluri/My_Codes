size=int(input())
array=[]
for i in range(size):

    array.append(int(input()))
output=[]
zeros=[]
for i in array:
    if i!=0:
        output.append(i)
    else:
        zeros.append(i)
for i in output+zeros:
    print(i,end=" ")