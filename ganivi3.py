input1="abcdd"
# write code here
l=[]
for i in input1:
    l.append(input1.count(i))
return input1[l.index(max(l))]

