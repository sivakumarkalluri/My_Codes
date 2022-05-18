input1="goodmorning"
results=[]
output=''
for i in input1:
    if i not in results:
        output+=i
        results.append(i)
return output
