input1=[0,3,0,2,0]
# write code here
output=[]
zeros=[]
for i in input1:
    if i!=0:
        output.append(i)
    else:
        zeros.append(0)
return output+zeros