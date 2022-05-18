size=int(input())
array=[]
result=[]
for i in range(size):
    array.append(input())
from itertools import permutations
for x in array:
    data=[''.join(j) for i in range(1,len(x) + 1) for j in  permutations(x, i)]
    palind=[]
    for i in data:
        if i==i[::-1]:
            palind.append(i)
    big=len(sorted(palind,key=len)[-1])
    result.append(big)
print(result)