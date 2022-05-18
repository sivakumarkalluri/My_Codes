size=int(input())
array=[]
for i in range(size):
    array.append(int(input()))
number=int(input())
total=0
for i in array:
    total+=i
output=total//number
if total%number==0:
    print(total//number)
else:
    print(output+1)