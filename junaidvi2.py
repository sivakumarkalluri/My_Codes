from itertools import permutations
input1="zbk"
input2="zkb"
perms= [''.join(i) for i in permutations(input1)]
print(perms)
if input2 in perms:
    print("yes")
else:
    print("no")