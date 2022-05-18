from itertools import permutations
word=input()
array=[]
for i in word:
    array.append(i)
total= len(list(permutations(array)))
print(total)
