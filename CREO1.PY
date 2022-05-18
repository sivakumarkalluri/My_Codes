



from itertools import permutations,combinations
import itertools
size=int(input())
array=[]
for i in range(size):
    array.append(int(input()))

k=int(input())
flag=0
result=[]
for r in range(1,size + 1):
    object = itertools.combinations(array, r)
    com_list = list(object)
    result.append(com_list)
for i in result:
    for j in i:
        if sum(j)==k:
            flag=1
            break
if flag:
    print("TRUE")
else:
    print("FALSE")
