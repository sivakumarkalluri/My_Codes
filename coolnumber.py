def cool(binary,k):
    repeat=0
    for i in range(len(binary)-2):
        if binary[i]+binary[i+1]+binary[i+2]=="101":
            repeat+=1
    if repeat>=k:
        return True
number,k=map(int,input().split())
count=0
for i in range(1,number+1):
    binary=str(bin(i))[2:]
    if cool(binary,k):
        count+=1
print(count)



    
