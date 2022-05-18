value=input()
k=int(input())
num=ord(value)
small=[chr(i) for i in range(97,123)]
big=[chr(i) for i in range(65,91)]
if value.islower(): 
    count=0
    start=small.index(value)
    for i in range(len(small)):
        element=start%len(small)
        if count<k:
            start+=1
            count+=1
        else:
            break
else:
    start=big.index(value)
    count=0
    for i in range(len(big)):
        element=start%len(big)
        if count<k:
            start+=1
            count+=1
        else:
            break
if value.islower():
    print(small[element])
else:
    print(big[element])
