data=[12,'a',90,'the',(1,2),8]
res={}
for i in range(len(data)):
    if type(data[i])==int:
        res[data[i]]=i
print(res)