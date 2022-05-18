candies=int(input())
childs=int(input())
output=[]
sum=0
total=0
remaining=candies
temp=candies
while temp>0:
    for i in range(1,childs+1):
        if temp>0:
            sum=0
            sum+=i
            
            if total<=temp:
                total+=sum
                temp=candies-total
                output.append(sum)
            else:
                sum=candies-total
                temp=candies-total
                output.append(sum)
        else:
            break
print(output)

