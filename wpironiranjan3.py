import re
from unittest import result


num=int(input())
array=list(map(int,input().split()))
output=[]
for i in array:
    value=bin(i)[2:]
    result=""
    for j in value:
        if j=="0":
            result+="1"
        else:
            result+="0"
    
    output.append(int(result,2))
for i in output:
    print(i,end=" ")