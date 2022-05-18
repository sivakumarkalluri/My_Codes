value=input()
k=int(input())
output=""
for i in range(len(value)):
    if int(value[i])%2!=0:
        
        count=0
        start=i
        for i in range(len(value)):
            element=start%len(value)
            if count<k:
                start+=1
                count+=1
            else:
                break
        output+=value[element]
        
    else:
        output+=value[i]
print(output)