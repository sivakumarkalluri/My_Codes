input1=int(input())
import math
count=0
for i in range(2,input1):
    if math.gcd(i,input1)==1:
        count+=1
print(count+1)

