

import math
size=int(input())
array=[]
for i in range(size):
    array.append(int(input()))
count=0
for num in array:
    root = math.sqrt(num)
    if int(root + 0.5) ** 2 == num:
        count+=1
print(count)