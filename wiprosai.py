

value=input()
k=int(input())
output=""
for i in range(len(value)):
    flag=1
    for j in range(2,int(value)):
        if int(i)%j==0:
            if i+k+1<len(value):
                output+=value[i+k]
                flag=0
                break
            else:
                diff=len(value)-i+1
                output+=value[diff]
                flag=0
                break
    if flag:
        output+=value[i]
print(output)

            
        
