data={(1,2,3,4):"hello",'hai':9,(4,5):90,9:"a"}
res={}
for i in data:
    if type(data[i])==str:
        res[data[i]]=i
    else:
        res[i]=data[i]
print(res)
