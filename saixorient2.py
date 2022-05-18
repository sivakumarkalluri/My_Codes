array=[]
while True:
    a=int(input())
    array.append(a)
    if a<0:
        break
array_2=list(set(array))
result=[]
for i in array_2:
    result.append(array.count(i))
print(sum(result)//len(result))