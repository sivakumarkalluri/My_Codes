first=int(input())
last=int(input())
array=[]
for i in range(first, last + 1):
    if i**(.5)==int(i**(.5)) and i!=1:
        array.append(i)
print(sum(array))
        
 